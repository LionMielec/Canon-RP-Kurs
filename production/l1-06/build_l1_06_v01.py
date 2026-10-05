# SPDX-License-Identifier: GPL-2.0-or-later
#
# Canon RP kurs — L1-06-V01 i L1-06-V03: ten sam kubek w świetle z okna (D-075).
# Trzy wersje V01: okno z przodu, z boku, od tyłu. V03: wersja „od tyłu”
# przy 0 i przy plus 1 (ta sama scena, ekspozycja o 1 EV wyżej).
#
# Scena, kubek, materiały i aparat pochodzą bez zmian ze skryptu L1-03
# (production/l1-03/scene/build_v04a_scene.py): kubek 1 z kalibracją koloru
# shot-1.json, aparat w położeniu V04A pozycja 1 (50 mm, f/8). Ten skrypt
# zastępuje światło: zamiast światła z lewej z przodu jest jedno prostokątne
# okno z rozproszonym światłem dnia i jest to jedyne źródło światła (światło
# otoczenia sceny wyłączone, ściany odbijają tylko światło okna). Z kadru
# usunięta jest lampa stojąca za kubkiem, bo sugerowała inne źródło światła.
#
# Przykład:
#   B=/Applications/Blender.app/Contents/MacOS/Blender
#   S=production/l1-06/build_l1_06_v01.py
#   $B -b --factory-startup --python $S -- --window bok \
#      --out production/l1-06/renders/l1-06-v01-bok-proba1.png
#   $B -b --factory-startup --python $S -- --window bok --dark-wall \
#      --out production/l1-06/renders/l1-06-v01-bok-proba2.png
#   $B -b --factory-startup --python $S -- --window tyl --dark-wall \
#      --out production/l1-06/renders/l1-06-v01-tyl.png \
#      --plus1-out production/l1-06/renders/l1-06-v03-tyl-plus1.png

import argparse
import json
import math
import os
import sys

import bpy
import numpy as np
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
SCENE_DIR = os.path.join(HERE, "..", "l1-03", "scene")
sys.path.insert(0, SCENE_DIR)
import build_v04a_scene as base  # noqa: E402

DESIGN = 1
CALIBRATION = os.path.join(SCENE_DIR, "calibration", "shot-1.json")

# ---------------------------------------------------------------------------
# Okno (wybór produkcyjny, nie pomiar): prostokąt 1,0 m szerokości i 1,2 m
# wysokości, parapet 0,85 m nad podłogą (środek okna 1,45 m nad podłogą,
# 0,64 m nad blatem), płaszczyzna okna pionowa, 1,0 m od osi kubka.
# Moc i barwa jak okno w scenie L1-03 (160 W, lekko ciepła biel), żeby
# kalibracja koloru kubka z L1-03 nadal pasowała.
# Kierunek okna podaje kąt w poziomie względem osi aparatu (od kubka):
#   0° = okno za aparatem (z przodu), 90° = okno z lewej strony kubka (z boku),
#   180° = okno w ścianie za kubkiem, w kadrze (od tyłu).
# We wszystkich wersjach jest to ten sam prostokąt świecący (szyba 1,0 × 1,2 m,
# 160 W, dolna krawędź szyby 0,85 m nad podłogą); zmienia się tylko położenie.
# ---------------------------------------------------------------------------

WINDOW_SIZE = (1.0, 1.2)        # szerokość, wysokość [m]
WINDOW_SILL_Z = 0.85            # parapet nad podłogą [m]
WINDOW_DISTANCE = 1.0           # od osi kubka do płaszczyzny okna [m]
WINDOW_POWER_W = 160.0
WINDOW_COLOR = (1.0, 0.98, 0.95)

LUMA = np.array((0.2126, 0.7152, 0.0722), dtype=np.float32)
SIDE_DEG = 60.0       # łaty pomiaru: 60° od osi aparatu w lewo i w prawo, 3 cm nad dnem kubka

WINDOWS = {
    # exposure "glaze": strona kubka zwrócona do okna (łata lit_deg) ma jasność
    # szkliwa z palety; "mean": średnia jasność całego kadru jak średnia szarość
    "przod": {"azimuth_deg": 0.0, "exposure": "glaze", "lit_deg": 0.0},
    "bok": {"azimuth_deg": 90.0, "exposure": "glaze", "lit_deg": -SIDE_DEG},
    "tyl": {"azimuth_deg": 180.0, "exposure": "mean"},
}

# Średnia szarość: średnia jasność liniowa kadru 0,18 (18 % odbicia). Przybliżenie
# pomiaru wielosegmentowego w trybie P — wybór produkcyjny, nie odwzorowanie
# algorytmu Canon.
MEAN_TARGET = 0.18

# Okno w ścianie za kubkiem (wersja „od tyłu”); wybór produkcyjny, nie pomiar.
# Szyba = ten sam prostokąt świecący 1,0 × 1,2 m. Wokół niej biała rama
# 8 cm (profil 7 cm głębokości), osadzona w połowie grubości muru; mur 30 cm
# (w scenie L1-03 ściana ma 5 cm, więc ościeża dobudowane są za ścianą);
# parapet wewnętrzny 2,5 cm grubości, wystaje 5 cm przed ścianę i 5 cm poza
# otwór z każdej strony. Za szybą nie ma niczego poza światłem dnia.
WALL_THICKNESS = 0.30
FRAME_FACE = 0.08
FRAME_DEPTH = 0.07
SILL_THICKNESS = 0.025
SILL_OVERHANG = 0.05
FRAME_HEX = "#eeece8"
SILL_HEX = "#ece9e3"
PAINTING_OBJECTS = ("Rama", "Obraz")


def build_window(azimuth_deg, distance=WINDOW_DISTANCE, visible=False):
    """Usuwa światło sceny L1-03 i stawia jedno okno w podanym kierunku.
    visible: szyba widoczna dla aparatu (okno w kadrze)."""
    old = bpy.data.objects.get("Okno")
    if old is not None:
        light = old.data
        bpy.data.objects.remove(old)
        bpy.data.lights.remove(light)

    cam = bpy.context.scene.camera
    to_cam = cam.location - base.MUG_BASE
    to_cam.z = 0.0
    to_cam.normalize()
    a = math.radians(azimuth_deg)
    # obrót wektora „do aparatu” o kąt a w lewo (patrząc z góry, aparat patrzy na kubek)
    direction = Vector((to_cam.x * math.cos(a) + to_cam.y * math.sin(a),
                        -to_cam.x * math.sin(a) + to_cam.y * math.cos(a), 0.0))
    center_z = WINDOW_SILL_Z + WINDOW_SIZE[1] / 2
    location = Vector((base.MUG_BASE.x, base.MUG_BASE.y, 0.0)) + direction * distance
    location.z = center_z

    data = bpy.data.lights.new("Okno", "AREA")
    data.shape = "RECTANGLE"
    data.size = WINDOW_SIZE[0]
    data.size_y = WINDOW_SIZE[1]
    data.energy = WINDOW_POWER_W
    data.color = WINDOW_COLOR
    obj = base.link(bpy.data.objects.new("Okno", data))
    obj.location = location
    # okno pionowe: świeci poziomo w stronę kubka, lokalna oś Y w górę
    obj.rotation_euler = (-direction).to_track_quat("-Z", "Y").to_euler()
    obj.visible_camera = visible
    side = "lewo" if direction.x < 0 else "prawo"
    print(f"OKNO: odleglosc od osi kubka {distance:.2f} m, srodek ({location.x:.3f}, {location.y:.3f}, {location.z:.3f}) m, "
          f"{WINDOW_SIZE[0]:.2f} x {WINDOW_SIZE[1]:.2f} m, {WINDOW_POWER_W:g} W, "
          f"kat od osi aparatu {azimuth_deg:g} st. (w {side})")
    return obj


LAMP_OBJECTS = ("Lampa_podstawa", "Lampa_slup", "Lampa_abazur")
# Ściana naprzeciw okna (prawa, poza kadrem) w wariancie --dark-wall: matowa farba
# w ciepłym szarobeżowym kolorze, jaki bywa w domu (wybór produkcyjny, nie pomiar).
DARK_WALL_HEX = "#8c8378"


def build_wall_window():
    """Wersja „od tyłu”: otwór w ścianie za kubkiem, ościeża, rama i parapet.
    Zwraca odległość szyby od osi kubka. Obraz na tej ścianie zostaje zdjęty,
    bo wypadałby w miejscu okna."""
    for name in PAINTING_OBJECTS:
        obj = bpy.data.objects[name]
        mesh = obj.data
        bpy.data.objects.remove(obj)
        bpy.data.meshes.remove(mesh)
    gw, gh = WINDOW_SIZE
    x0 = base.MUG_BASE.x
    glass_z0 = WINDOW_SILL_Z
    ow, oh = gw + 2 * FRAME_FACE, gh + 2 * FRAME_FACE          # otwór w murze
    oz0 = glass_z0 - FRAME_FACE
    oz = oz0 + oh / 2
    inner = base.WALL_Y                                          # lico ściany od strony pokoju
    glass_y = inner + WALL_THICKNESS / 2

    wall = bpy.data.objects["Sciana_tyl"]
    wall_mat = wall.data.materials[0]
    cutter = base.box("Otwor", (ow, 1.0, oh), (x0, inner, oz), wall_mat)
    mod = wall.modifiers.new("Otwor", "BOOLEAN")
    mod.operation = "DIFFERENCE"
    mod.solver = "EXACT"
    mod.object = cutter
    cutter.hide_render = True
    cutter.hide_viewport = True

    # ościeża (boki otworu w murze), tynk jak ściana
    # (lico ościeży 2 mm za licem ściany, żeby powierzchnie się nie nakładały)
    t, depth = 0.04, WALL_THICKNESS - 0.002
    yc = inner + 0.002 + depth / 2
    base.box("Ociez_lewa", (t, depth, oh), (x0 - ow / 2 - t / 2, yc, oz), wall_mat)
    base.box("Ociez_prawa", (t, depth, oh), (x0 + ow / 2 + t / 2, yc, oz), wall_mat)
    base.box("Ociez_gora", (ow + 2 * t, depth, t), (x0, yc, oz0 + oh + t / 2), wall_mat)
    base.box("Ociez_dol", (ow + 2 * t, depth, t), (x0, yc, oz0 - t / 2), wall_mat)

    frame_mat = base.principled("Rama_okna", base.hex_to_linear(FRAME_HEX), roughness=0.4)
    f, dy = FRAME_FACE, FRAME_DEPTH
    base.box("Rama_okna_lewa", (f, dy, oh), (x0 - gw / 2 - f / 2, glass_y, oz), frame_mat)
    base.box("Rama_okna_prawa", (f, dy, oh), (x0 + gw / 2 + f / 2, glass_y, oz), frame_mat)
    base.box("Rama_okna_gora", (gw, dy, f), (x0, glass_y, glass_z0 + gh + f / 2), frame_mat)
    base.box("Rama_okna_dol", (gw, dy, f), (x0, glass_y, glass_z0 - f / 2), frame_mat)

    sill_mat = base.principled("Parapet", base.hex_to_linear(SILL_HEX), roughness=0.5)
    sill_y0 = inner - SILL_OVERHANG
    sill_y1 = glass_y - dy / 2
    base.box("Parapet", (ow + 2 * SILL_OVERHANG, sill_y1 - sill_y0, SILL_THICKNESS),
             (x0, (sill_y0 + sill_y1) / 2, oz0 - SILL_THICKNESS / 2), sill_mat, bevel=0.003)
    distance = glass_y + dy / 2 - base.MUG_BASE.y - 0.002
    print(f"OKNO W SCIANIE: otwor {ow:.2f} x {oh:.2f} m, dol otworu {oz0:.2f} m nad podloga, "
          f"mur {WALL_THICKNESS:.2f} m, rama {FRAME_FACE * 100:.0f} cm {FRAME_HEX}, "
          f"parapet {ow + 2 * SILL_OVERHANG:.2f} x {sill_y1 - sill_y0:.3f} x {SILL_THICKNESS:.3f} m {SILL_HEX}; "
          f"obraz na scianie zdjety")
    return distance


def prepare_room(dark_wall=False):
    """Usuwa lampę stojącą i wyłącza światło otoczenia sceny L1-03; opcjonalnie
    przyciemnia ścianę naprzeciw okna, która odbija światło na stronę w cieniu."""
    for name in LAMP_OBJECTS:
        obj = bpy.data.objects[name]
        mesh = obj.data
        bpy.data.objects.remove(obj)
        bpy.data.meshes.remove(mesh)
    bpy.context.scene.world.node_tree.nodes["Background"].inputs["Strength"].default_value = 0.0
    print("POKOJ: bez lampy stojacej, bez swiatla otoczenia (jedyne zrodlo: okno)")
    if dark_wall:
        wall = bpy.data.objects["Sciana_prawa"]
        wall.data.materials[0] = base.principled("Sciana_prawa_ciemna", base.hex_to_linear(DARK_WALL_HEX), roughness=1.0)
        print(f"POKOJ: sciana naprzeciw okna {DARK_WALL_HEX}, matowa")


def glaze_luminance(path, offsets_deg, z=0.030):
    """Jasność (liniowo) szkliwa w łatach na ściance kubka, obróconych o podane
    kąty od kierunku do aparatu (ujemny kąt = lewa strona w kadrze)."""
    scene = bpy.context.scene
    cam = scene.camera
    img = bpy.data.images.load(path, check_existing=False)
    w, h = img.size
    px = np.array(img.pixels[:], dtype=np.float32).reshape(h, w, 4)[:, :, :3]
    bpy.data.images.remove(img)
    lum = np.where(px <= 0.04045, px / 12.92, ((px + 0.055) / 1.055) ** 2.4) @ LUMA
    view = cam.location - base.MUG_BASE
    rad = base.MUG_DESIGNS[DESIGN]["radius"](z)
    half = max(2, w // 200)
    values = []
    for offset in offsets_deg:
        theta = math.atan2(view.x, -view.y) + math.radians(offset)
        c = base.world_to_camera_view(
            scene, cam, base.MUG_BASE + Vector((rad * math.sin(theta), -rad * math.cos(theta), z)))
        x, y = int(c.x * w), int(c.y * h)
        values.append(float(np.median(lum[y - half:y + half + 1, x - half:x + half + 1])))
    return values


def auto_exposure(out_path, lit_deg, iterations=3):
    """Dobiera ekspozycję całego obrazu tak, żeby strona kubka zwrócona do okna
    miała jasność koloru szkliwa z palety; strona w cieniu wychodzi wtedy ciemniej.
    Kolory materiałów zostają z kalibracji shot-1.json."""
    scene = bpy.context.scene
    target = float(np.array(base.hex_to_linear(base.PALETTE[base.MUG_DESIGNS[DESIGN]["glaze"]])) @ LUMA)
    pct, samples = scene.render.resolution_percentage, scene.cycles.samples
    scene.render.resolution_percentage, scene.cycles.samples = 25, 64
    i = attempts = 0
    while i < iterations and attempts < iterations + 6:
        attempts += 1
        bpy.ops.render.render(write_still=True)
        (lit,) = glaze_luminance(out_path, (lit_deg,))
        print(f"EKSPOZYCJA {attempts}: {scene.view_settings.exposure:.3f}, jasna strona {lit:.3f} (cel {target:.3f})")
        if lit >= 0.97:
            # przepalona łata nie mówi, ile światła pada; najpierw zmniejsz ekspozycję
            scene.view_settings.exposure -= 1.0
            continue
        i += 1
        scene.view_settings.exposure += math.log2(target / max(1e-6, lit))
    scene.render.resolution_percentage, scene.cycles.samples = pct, samples
    print(f"EKSPOZYCJA: {scene.view_settings.exposure:.3f}")


def frame_mean(path):
    img = bpy.data.images.load(path, check_existing=False)
    w, h = img.size
    px = np.array(img.pixels[:], dtype=np.float32).reshape(h, w, 4)[:, :, :3]
    bpy.data.images.remove(img)
    lum = np.where(px <= 0.04045, px / 12.92, ((px + 0.055) / 1.055) ** 2.4) @ LUMA
    return float(lum.mean())


def auto_exposure_mean(out_path, iterations=4):
    """Dobiera ekspozycję tak, żeby średnia jasność liniowa całego kadru była
    równa MEAN_TARGET (średnia szarość)."""
    scene = bpy.context.scene
    pct, samples = scene.render.resolution_percentage, scene.cycles.samples
    scene.render.resolution_percentage, scene.cycles.samples = 25, 64
    for i in range(iterations):
        bpy.ops.render.render(write_still=True)
        mean = frame_mean(out_path)
        print(f"EKSPOZYCJA {i + 1}: {scene.view_settings.exposure:.3f}, srednia kadru {mean:.3f} (cel {MEAN_TARGET:.3f})")
        scene.view_settings.exposure += math.log2(MEAN_TARGET / max(1e-6, mean))
    scene.render.resolution_percentage, scene.cycles.samples = pct, samples
    print(f"EKSPOZYCJA: {scene.view_settings.exposure:.3f}")


def glass_luminance(path):
    """Mediana jasności (liniowo) szyby w widocznej części okna: prostokąt
    10 cm nad dolną krawędzią szyby, od 0,2 do 0,8 jej szerokości, przycięty do kadru."""
    scene = bpy.context.scene
    cam = scene.camera
    light = bpy.data.objects["Okno"]
    img = bpy.data.images.load(path, check_existing=False)
    w, h = img.size
    px = np.array(img.pixels[:], dtype=np.float32).reshape(h, w, 4)[:, :, :3]
    bpy.data.images.remove(img)
    lum = np.where(px <= 0.04045, px / 12.92, ((px + 0.055) / 1.055) ** 2.4) @ LUMA
    gw = WINDOW_SIZE[0]
    y = light.location.y
    pts = [base.world_to_camera_view(scene, cam, Vector((light.location.x + gw * k, y, WINDOW_SILL_Z + dz)))
           for k in (-0.3, 0.3) for dz in (0.01, 0.10)]
    x0, x1 = (int(min(p.x for p in pts) * w), int(max(p.x for p in pts) * w))
    y0 = max(0, int(min(p.y for p in pts) * h))
    y1 = min(h - 1, int(max(p.y for p in pts) * h))
    if y1 <= y0:
        return float("nan")
    return float(np.median(lum[y0:y1 + 1, x0:x1 + 1]))


def back_report(path, label):
    front, left, right = glaze_luminance(path, (0.0, -SIDE_DEG, SIDE_DEG))
    glass = glass_luminance(path)
    print(f"OD TYLU {label}: kubek przod {front:.4f}, lewa {left:.4f}, prawa {right:.4f} (liniowo); "
          f"szyba {glass:.3f}; srednia kadru {frame_mean(path):.3f}; "
          f"szyba/kubek {math.log2(glass / max(1e-6, front)):.2f} EV")


def front_report(path):
    front, left, right = glaze_luminance(path, (0.0, -SIDE_DEG, SIDE_DEG))
    print(f"Z PRZODU: kubek przod {front:.3f}, lewa {left:.3f}, prawa {right:.3f} (liniowo); "
          f"przod/lewa {math.log2(front / max(1e-6, left)):.2f} EV, "
          f"przod/prawa {math.log2(front / max(1e-6, right)):.2f} EV, "
          f"lewa/prawa {math.log2(left / max(1e-6, right)):.2f} EV")


def side_report(path):
    lit, shade = glaze_luminance(path, (-SIDE_DEG, SIDE_DEG))
    print(f"STRONY KUBKA: lewa {lit:.3f}, prawa {shade:.3f} (liniowo), "
          f"roznica {math.log2(lit / max(1e-6, shade)):.2f} EV")


def main():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    parser = argparse.ArgumentParser()
    parser.add_argument("--window", choices=sorted(WINDOWS), required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--samples", type=int, default=256)
    parser.add_argument("--scale", type=int, default=100)
    parser.add_argument("--distance", type=float, default=WINDOW_DISTANCE,
                        help="odległość okna od osi kubka [m]")
    parser.add_argument("--dark-wall", action="store_true",
                        help="ściana naprzeciw okna ciemniejsza i matowa")
    parser.add_argument("--frame-report", action="store_true")
    parser.add_argument("--plus1-out", help="(od tyłu) drugi obraz tej samej sceny o 1 EV jaśniej")
    args = parser.parse_args(argv)
    spec = WINDOWS[args.window]
    out = os.path.abspath(args.out)
    os.makedirs(os.path.dirname(out), exist_ok=True)

    base.build_scene(DESIGN)
    prepare_room(args.dark_wall)
    base.make_camera(base.camera_location(1, base.SIDE_STEP), base.AIM_POINT, base.CAMERA_PITCH_DEG)
    distance, visible = args.distance, False
    if args.window == "tyl":
        distance, visible = build_wall_window(), True
    build_window(spec["azimuth_deg"], distance, visible)
    if args.frame_report:
        base.frame_report()
        return
    base.configure_render(out, args.scale, args.samples, 0.0)
    with open(CALIBRATION) as f:
        base.apply_calibration(json.load(f))
    if spec["exposure"] == "mean":
        auto_exposure_mean(out)
    else:
        auto_exposure(out, spec["lit_deg"])
    bpy.ops.render.render(write_still=True)
    glaze, text = base.measure_colors(out, DESIGN)
    print(f"POMIAR: szkliwo {base.linear_to_hex(glaze)}, napis {base.linear_to_hex(text)}")
    if args.window == "bok":
        side_report(out)
    elif args.window == "przod":
        front_report(out)
    else:
        back_report(out, "przy 0")
        if args.plus1_out:
            plus1 = os.path.abspath(args.plus1_out)
            scene = bpy.context.scene
            scene.view_settings.exposure += 1.0
            scene.render.filepath = plus1
            print(f"EKSPOZYCJA plus 1: {scene.view_settings.exposure:.3f}")
            bpy.ops.render.render(write_still=True)
            back_report(plus1, "przy plus 1")


if __name__ == "__main__":
    main()
