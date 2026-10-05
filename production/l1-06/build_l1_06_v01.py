# SPDX-License-Identifier: GPL-2.0-or-later
#
# Canon RP kurs — L1-06-V01: ten sam kubek w świetle z okna (D-075).
# Ujęcie próbne: tylko wersja „z boku”.
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
#   0° = okno za aparatem (z przodu), 90° = okno z lewej strony kubka (z boku).
# Na razie zdefiniowana jest tylko wersja „bok” (D-075: najpierw ujęcie próbne).
# ---------------------------------------------------------------------------

WINDOW_SIZE = (1.0, 1.2)        # szerokość, wysokość [m]
WINDOW_SILL_Z = 0.85            # parapet nad podłogą [m]
WINDOW_DISTANCE = 1.0           # od osi kubka do płaszczyzny okna [m]
WINDOW_POWER_W = 160.0
WINDOW_COLOR = (1.0, 0.98, 0.95)

LUMA = np.array((0.2126, 0.7152, 0.0722), dtype=np.float32)
SIDE_DEG = 60.0       # łaty pomiaru: 60° od osi aparatu w lewo i w prawo, 3 cm nad dnem kubka

WINDOWS = {
    # lit_deg: łata pomiaru ekspozycji po stronie okna
    "bok": {"azimuth_deg": 90.0, "lit_deg": -SIDE_DEG},
}


def build_window(azimuth_deg, distance=WINDOW_DISTANCE):
    """Usuwa światło sceny L1-03 i stawia jedno okno w podanym kierunku."""
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
    side = "lewo" if direction.x < 0 else "prawo"
    print(f"OKNO: odleglosc od osi kubka {distance:.2f} m, srodek ({location.x:.3f}, {location.y:.3f}, {location.z:.3f}) m, "
          f"{WINDOW_SIZE[0]:.2f} x {WINDOW_SIZE[1]:.2f} m, {WINDOW_POWER_W:g} W, "
          f"kat od osi aparatu {azimuth_deg:g} st. (w {side})")
    return obj


LAMP_OBJECTS = ("Lampa_podstawa", "Lampa_slup", "Lampa_abazur")
# Ściana naprzeciw okna (prawa, poza kadrem) w wariancie --dark-wall: matowa farba
# w ciepłym szarobeżowym kolorze, jaki bywa w domu (wybór produkcyjny, nie pomiar).
DARK_WALL_HEX = "#8c8378"


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
    args = parser.parse_args(argv)
    out = os.path.abspath(args.out)
    os.makedirs(os.path.dirname(out), exist_ok=True)

    base.build_scene(DESIGN)
    prepare_room(args.dark_wall)
    base.make_camera(base.camera_location(1, base.SIDE_STEP), base.AIM_POINT, base.CAMERA_PITCH_DEG)
    build_window(WINDOWS[args.window]["azimuth_deg"], args.distance)
    if args.frame_report:
        base.frame_report()
        return
    base.configure_render(out, args.scale, args.samples, 0.0)
    with open(CALIBRATION) as f:
        base.apply_calibration(json.load(f))
    auto_exposure(out, WINDOWS[args.window]["lit_deg"])
    bpy.ops.render.render(write_still=True)
    glaze, text = base.measure_colors(out, DESIGN)
    print(f"POMIAR: szkliwo {base.linear_to_hex(glaze)}, napis {base.linear_to_hex(text)}")
    side_report(out)


if __name__ == "__main__":
    main()
