# SPDX-License-Identifier: GPL-2.0-or-later
#
# Canon RP kurs — L1-08-V01: ta sama scena przy f/1.8, f/4.0 i f/8 (D-089, D-090).
# Trzy przedmioty jeden za drugim: przedni kubek (wzór 2), środkowy kubek
# (wzór 1, napis „Amore Mio”, w miejscu kubka z L1-07) i stojąca książka
# z napisem „Notatki”. Ostrość na napisie środkowego kubka. Między klatkami
# zmienia się wyłącznie przysłona; wszystkie klatki powstają w jednym
# uruchomieniu z tą samą ekspozycją (przysłona w Blenderze zmienia tylko
# rozmycie, nie jasność).
#
# Scena bazowa, regał w tle i aparat (50 mm, matryca 36 × 24 mm, położenie
# i nachylenie) pochodzą bez zmian ze skryptów L1-03 i L1-07:
#   production/l1-03/scene/build_v04a_scene.py
#   production/l1-07/build_l1_07_v01.py
# Środkowy kubek: wzór 1 z kalibracją koloru shot-1.json (jak L1-07).
# Ten skrypt dokłada tylko przedni kubek i stojącą książkę; żadnego z tamtych
# skryptów nie zmienia.
#
# Przykład (podgląd: dłuższy bok 1200 px):
#   B=/Applications/Blender.app/Contents/MacOS/Blender
#   S=production/l1-08/build_l1_08_v01.py
#   $B -b --factory-startup --python $S -- --res 1200 --samples 128 \
#      --out-dir production/l1-08/renders/podglad

import argparse
import json
import math
import os
import sys

import bpy
from mathutils import Euler, Vector

HERE = os.path.dirname(os.path.abspath(__file__))
SCENE_DIR = os.path.join(HERE, "..", "l1-03", "scene")
L107_DIR = os.path.join(HERE, "..", "l1-07")
sys.path.insert(0, SCENE_DIR)
sys.path.insert(0, L107_DIR)
import build_v04a_scene as base  # noqa: E402
import build_l1_07_v01 as l107  # noqa: E402

DESIGN = 1                                     # środkowy kubek, jak w L1-07
FRONT_DESIGN = 2                               # przedni kubek
CALIBRATION = os.path.join(SCENE_DIR, "calibration", "shot-1.json")
# Kolory bazowe przedniego kubka: kalibracja wzoru 2 z L1-03 (bez jej ekspozycji;
# ekspozycja całego obrazu pochodzi z shot-1.json).
FRONT_COLORS = os.path.join(SCENE_DIR, "calibration", "closeup-2.json")
F_STOPS = (("f18", 1.8), ("f40", 4.0), ("f80", 8.0))

# ---------------------------------------------------------------------------
# Rozstawienie (wybór produkcyjny, nie pomiar). Środkowy kubek stoi tam, gdzie
# kubek z L1-07 (oś w x = 0, y = 0). Przedni kubek ok. 0,20 m bliżej aparatu,
# z lewej; książka ok. 0,20 m dalej, z prawej. Odstępy liczone między
# powierzchniami z napisami, wzdłuż osi patrzenia. Przedni kubek i książka
# obrócone napisem do aparatu.
# ---------------------------------------------------------------------------

FRONT_MUG_XY = (-0.15, -0.20)
BOOK = {"x": 0.17, "front_y": 0.153, "rot": None, "text_z": 0.105,
        "text": "Notatki", "text_width": 0.095}
CAMERA = l107.CAMERA
PITCH_DEG = l107.PITCH_DEG
FOCUS = base.V06_TEXT                          # napis na przedniej ściance środkowego kubka


def facing_angle(x, y):
    """Obrót wokół osi pionowej, po którym przód (strona -Y) patrzy na aparat."""
    return math.atan2(CAMERA.x - x, y - CAMERA.y)


def build_front_mug():
    """Drugi kubek z tych samych funkcji sceny L1-03. Funkcje kubka stawiają go
    w base.MUG_BASE, więc na czas budowy przestawiamy to położenie, a potem
    przywracamy (pomiary koloru środkowego kubka z niego korzystają)."""
    with open(FRONT_COLORS) as f:
        cal = json.load(f)
    d = base.MUG_DESIGNS[FRONT_DESIGN]
    mats = {
        "glaze": base.glaze_material("Szkliwo_przod", tuple(cal["glaze"])),
        "inner": base.glaze_material("Szkliwo_wnetrze_przod", tuple(cal["inner"])),
        "print": base.principled("Nadruk_przod", tuple(cal["text"]), roughness=0.22,
                                 Coat_Weight=0.35, Coat_Roughness=0.06),
    }
    if d["accent"]:
        mats["accent"] = base.glaze_material("Akcent_przod", base.hex_to_linear(base.PALETTE[d["accent"]]))

    saved = base.MUG_BASE
    before = set(bpy.data.objects)
    pivot = Vector((*FRONT_MUG_XY, base.TABLE_TOP_Z))
    base.MUG_BASE = pivot
    try:
        base.build_mug(mats, FRONT_DESIGN)
        text = base.build_mug_text(mats, FRONT_DESIGN)
    finally:
        base.MUG_BASE = saved
    text.name = "Napis_przod"
    angle = facing_angle(*FRONT_MUG_XY)
    for obj in set(bpy.data.objects) - before:
        if obj.name.startswith("Kubek"):
            obj.name = obj.name.split(".")[0] + "_przod"
        offset = obj.location - pivot
        offset.rotate(Euler((0.0, 0.0, angle)))
        obj.location = pivot + offset
        obj.rotation_euler.z += angle
    print(f"PRZEDNI KUBEK: wzor {FRONT_DESIGN}, os w ({FRONT_MUG_XY[0]:.2f}, {FRONT_MUG_XY[1]:.2f}) m, "
          f"obrot {math.degrees(angle):.1f} st.")


def text_box(name):
    """Prostokąt napisu w kadrze (ułamki, od dołu), z 10 % zapasem."""
    scene = bpy.context.scene
    obj = bpy.data.objects[name]
    pts = [base.world_to_camera_view(scene, scene.camera, obj.matrix_world @ v.co) for v in obj.data.vertices]
    xs, ys = [p.x for p in pts], [p.y for p in pts]
    mx, my = (max(xs) - min(xs)) * 0.1, (max(ys) - min(ys)) * 0.1
    return (min(xs) - mx, min(ys) - my, max(xs) + mx, max(ys) + my)


def text_distance(name):
    """Odległość aparatu od środka napisu (m)."""
    obj = bpy.data.objects[name]
    pts = [obj.matrix_world @ v.co for v in obj.data.vertices]
    center = sum(pts, Vector()) / len(pts)
    return (center - CAMERA).length


def main():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--res", type=int, default=base.RES_X, help="dłuższy bok w pikselach")
    parser.add_argument("--samples", type=int, default=256)
    parser.add_argument("--frame-report", action="store_true")
    args = parser.parse_args(argv)
    out_dir = os.path.abspath(args.out_dir)
    os.makedirs(out_dir, exist_ok=True)

    book = dict(BOOK, rot=math.degrees(facing_angle(BOOK["x"], BOOK["front_y"])))
    base.build_scene(DESIGN, standing_book=book)
    l107.remove(("Lampa_podstawa", "Lampa_slup", "Lampa_abazur", "Rama", "Obraz"))
    print("TLO: lampa stojaca i obraz zdjete (jak L1-07)")
    l107.move_back_wall()
    l107.build_shelf()
    build_front_mug()
    print(f"KSIAZKA: x {book['x']:.2f} m, okladka y {book['front_y']:.3f} m, obrot {book['rot']:.1f} st.")
    cam = base.make_camera(CAMERA, base.AIM_POINT, pitch_deg=PITCH_DEG,
                           f_stop=F_STOPS[0][1], focus_point=FOCUS)
    bpy.context.view_layer.update()
    names = (("przedni kubek", "Napis_przod"), ("srodkowy kubek", "Napis"), ("ksiazka", "Napis_ksiazka"))
    for label, name in names:
        print(f"ODLEGLOSC napisu ({label}): {text_distance(name):.3f} m od aparatu")
    if args.frame_report:
        base.frame_report()
        for label, name in names:
            print(f"KADR napis ({label}): {tuple(round(v, 3) for v in text_box(name))}")
        for name in ("Kubek_przod", "Kubek_ucho_przod"):
            obj = bpy.data.objects[name]
            pts = [base.world_to_camera_view(bpy.context.scene, cam, obj.matrix_world @ Vector(c))
                   for c in obj.bound_box]
            print(f"KADR {name}: x {min(p.x for p in pts):.3f}..{max(p.x for p in pts):.3f}  "
                  f"y {min(p.y for p in pts):.3f}..{max(p.y for p in pts):.3f}")
        return

    scale = round(100 * args.res / base.RES_X)
    base.configure_render(os.path.join(out_dir, "x.png"), scale, args.samples, 0.0)
    with open(CALIBRATION) as f:
        base.apply_calibration(json.load(f))
    bpy.context.view_layer.update()
    boxes = [(label, text_box(name)) for label, name in names]
    bg_box = (0.15, 0.75, 0.85, 0.95)          # górna część kadru: regał nad przedmiotami
    results = []
    for label, fstop in F_STOPS:
        cam.data.dof.aperture_fstop = fstop
        path = os.path.join(out_dir, f"l1-08-v01-{label}.png")
        bpy.context.scene.render.filepath = path
        bpy.ops.render.render(write_still=True)
        lum = l107.luminance(path)
        glaze, text = base.measure_colors(path, DESIGN)
        results.append((fstop, float(lum.mean()),
                        [(name, l107.sharpness(lum, box)) for name, box in boxes],
                        l107.sharpness(lum, bg_box)))
        print(f"RENDER f/{fstop:g}: {path}; szkliwo {base.linear_to_hex(glaze)}, napis {base.linear_to_hex(text)}")
    for fstop, mean, sharp, s_bg in results:
        parts = "; ".join(f"ostrosc napisu ({name}) {s:.3e}" for name, s in sharp)
        print(f"POMIAR f/{fstop:g}: srednia jasnosc kadru {mean:.4f}; {parts}; ostrosc tla {s_bg:.3e}")


if __name__ == "__main__":
    main()
