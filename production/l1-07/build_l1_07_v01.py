# SPDX-License-Identifier: GPL-2.0-or-later
#
# Canon RP kurs — L1-07-V01: ta sama scena przy f/1.8 i f/5.6 (D-083, D-084).
# Para renderów: kubek z napisem, wyraźne tło (regał z książkami) 2–3 m za
# kubkiem, aparat ok. 1 m od kubka, ostrość na napisie. Między ujęciami zmienia
# się wyłącznie przysłona; obie klatki powstają w jednym uruchomieniu z tej
# samej sceny i z tą samą ekspozycją, więc jasność obu zdjęć jest taka sama
# (przysłona w Blenderze zmienia tylko rozmycie, nie jasność).
#
# Scena, kubek, materiały, światło i aparat (50 mm, matryca 36 × 24 mm)
# pochodzą bez zmian ze skryptu L1-03 (production/l1-03/scene/build_v04a_scene.py):
# kubek 1 z kalibracją koloru shot-1.json. Ten skrypt zmienia tylko tło:
# ściana za kubkiem odsunięta na WALL_Y_L107, przy niej prosty regał z książkami
# (własne bryły, bez gotowych modeli — D-051); lampa stojąca i obraz zdjęte, bo
# stałyby przed regałem / za nim.
#
# Przykład (podgląd: dłuższy bok 1200 px):
#   B=/Applications/Blender.app/Contents/MacOS/Blender
#   S=production/l1-07/build_l1_07_v01.py
#   $B -b --factory-startup --python $S -- --res 1200 --samples 128 \
#      --out-dir production/l1-07/renders/podglad

import argparse
import json
import math
import os
import random
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
F_STOPS = (("f18", 1.8), ("f56", 5.6))
LUMA = np.array((0.2126, 0.7152, 0.0722), dtype=np.float32)

# ---------------------------------------------------------------------------
# Tło (wybór produkcyjny, nie pomiar): ściana 2,75 m za osią kubka, regał
# 0,30 m głębokości stoi przy ścianie, więc grzbiety książek są ok. 2,45 m
# za kubkiem (w zakresie 2–3 m z karty L1-07).
# ---------------------------------------------------------------------------

WALL_Y_L107 = 2.75
SHELF = {"width": 1.80, "depth": 0.30, "height": 1.90, "board": 0.022,
         "levels": (0.08, 0.46, 0.84, 1.22, 1.60), "hex": "#ece9e3"}
BOOK_HEX = ("#5f7482", "#8a4b3c", "#c9a66b", "#3f5a4a", "#d8cfc0", "#7a6a8f",
            "#b5523b", "#2f3e57", "#9aa58b", "#e0b5a0", "#6b4f38", "#c7c2b8")
BOOK_SEED = 7

# Aparat: ok. 1 m od kubka, oczy osoby siedzącej nieco niżej niż w V04A,
# lekko w dół, kubek w dolnej części kadru, nad nim regał.
CAMERA = Vector((0.0, -0.95, base.TABLE_TOP_Z + 0.22))
PITCH_DEG = -5.0
FOCUS = base.V06_TEXT          # napis na przedniej ściance kubka


def remove(names):
    for name in names:
        obj = bpy.data.objects.get(name)
        if obj is not None:
            mesh = obj.data
            bpy.data.objects.remove(obj)
            bpy.data.meshes.remove(mesh)


def move_back_wall():
    """Odsuwa ścianę w tle i listwę na WALL_Y_L107; wydłuża prawą ścianę."""
    bpy.data.objects["Sciana_tyl"].location.y = WALL_Y_L107 + 0.025
    bpy.data.objects["Listwa"].location.y = WALL_Y_L107 - 0.0075
    right = bpy.data.objects["Sciana_prawa"]
    y0, y1 = -4.0, WALL_Y_L107 + 0.05            # w L1-03: od -4,0 do 2,0 m
    right.scale.y = (y1 - y0) / 6.0
    right.location.y = (y0 + y1) / 2
    print(f"TLO: sciana za kubkiem {WALL_Y_L107:.2f} m od osi kubka")


def build_shelf():
    """Prosty regał: boki, półki, plecy; na półkach książki z prostopadłościanów
    o różnych wysokościach i kolorach (stałe ziarno losowania)."""
    s = SHELF
    w, d, h, t = s["width"], s["depth"], s["height"], s["board"]
    back_y = WALL_Y_L107 - 0.005
    cy = back_y - d / 2
    mat = base.principled("Regal", base.hex_to_linear(s["hex"]), roughness=0.6)
    base.box("Regal_lewy", (t, d, h), (-w / 2 + t / 2, cy, h / 2), mat, bevel=0.002)
    base.box("Regal_prawy", (t, d, h), (w / 2 - t / 2, cy, h / 2), mat, bevel=0.002)
    base.box("Regal_plecy", (w, 0.008, h), (0.0, back_y - 0.004, h / 2), mat)
    for i, z in enumerate(s["levels"] + (h - t / 2,)):
        base.box(f"Regal_polka_{i}", (w - 2 * t, d, t), (0.0, cy, z), mat, bevel=0.002)

    rnd = random.Random(BOOK_SEED)
    mats = [base.principled(f"Ksiazka_{i}", base.hex_to_linear(c), roughness=0.7)
            for i, c in enumerate(BOOK_HEX)]
    front_y = back_y - d
    count = 0
    for li, z in enumerate(s["levels"]):
        x = -w / 2 + t + 0.02
        x_end = w / 2 - t - 0.02
        gap = s["levels"][li + 1] - z - t if li + 1 < len(s["levels"]) else h - z - 2 * t
        while True:
            bw = rnd.uniform(0.022, 0.050)
            if x + bw > x_end:
                break
            bh = min(gap - 0.03, rnd.uniform(0.20, 0.31))
            bd = rnd.uniform(0.17, 0.23)
            if rnd.random() < 0.06:          # przerwa między grupami książek
                x += rnd.uniform(0.06, 0.14)
                continue
            base.box(f"Ksiazka_regal_{count}", (bw, bd, bh),
                     (x + bw / 2, front_y + 0.02 + bd / 2, z + t / 2 + bh / 2),
                     mats[rnd.randrange(len(mats))], bevel=0.0015)
            x += bw + 0.002
            count += 1
    print(f"REGAL: {w:.2f} x {d:.2f} x {h:.2f} m, {count} ksiazek, "
          f"grzbiety {front_y + 0.02:.2f} m od osi kubka")


def luminance(path):
    img = bpy.data.images.load(path, check_existing=False)
    w, h = img.size
    px = np.array(img.pixels[:], dtype=np.float32).reshape(h, w, 4)[:, :, :3]
    bpy.data.images.remove(img)
    return np.where(px <= 0.04045, px / 12.92, ((px + 0.055) / 1.055) ** 2.4) @ LUMA


def sharpness(lum, box_frac):
    """Wariancja laplasjanu w prostokącie (ułamki kadru: x0, y0, x1, y1, od dołu)."""
    h, w = lum.shape
    x0, y0, x1, y1 = (int(box_frac[0] * w), int(box_frac[1] * h),
                      int(box_frac[2] * w), int(box_frac[3] * h))
    a = lum[y0:y1, x0:x1]
    lap = (-4 * a[1:-1, 1:-1] + a[:-2, 1:-1] + a[2:, 1:-1] + a[1:-1, :-2] + a[1:-1, 2:])
    return float(lap.var())


def text_box():
    """Prostokąt napisu kubka w kadrze (ułamki), z 10 % zapasem."""
    scene = bpy.context.scene
    obj = bpy.data.objects["Napis"]
    pts = [base.world_to_camera_view(scene, scene.camera, obj.matrix_world @ v.co) for v in obj.data.vertices]
    xs, ys = [p.x for p in pts], [p.y for p in pts]
    mx, my = (max(xs) - min(xs)) * 0.1, (max(ys) - min(ys)) * 0.1
    return (min(xs) - mx, min(ys) - my, max(xs) + mx, max(ys) + my)


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

    base.build_scene(DESIGN)
    remove(("Lampa_podstawa", "Lampa_slup", "Lampa_abazur", "Rama", "Obraz"))
    print("TLO: lampa stojaca i obraz zdjete")
    move_back_wall()
    build_shelf()
    cam = base.make_camera(CAMERA, base.AIM_POINT, pitch_deg=PITCH_DEG,
                           f_stop=F_STOPS[0][1], focus_point=FOCUS)
    print(f"APARAT: {CAMERA.x:.2f}, {CAMERA.y:.2f}, {CAMERA.z:.2f} m; do napisu "
          f"{(Vector(FOCUS) - CAMERA).length:.3f} m; do osi kubka "
          f"{(base.AIM_POINT - CAMERA).length:.3f} m; nachylenie {PITCH_DEG:g} st.")
    if args.frame_report:
        base.frame_report()
        return

    scale = round(100 * args.res / base.RES_X)
    base.configure_render(os.path.join(out_dir, "x.png"), scale, args.samples, 0.0)
    with open(CALIBRATION) as f:
        base.apply_calibration(json.load(f))
    bpy.context.view_layer.update()
    tb = text_box()
    bg_box = (0.15, 0.62, 0.85, 0.95)          # górna część kadru: regał
    results = []
    for label, fstop in F_STOPS:
        cam.data.dof.aperture_fstop = fstop
        path = os.path.join(out_dir, f"l1-07-v01-{label}.png")
        bpy.context.scene.render.filepath = path
        bpy.ops.render.render(write_still=True)
        lum = luminance(path)
        glaze, text = base.measure_colors(path, DESIGN)
        results.append((label, fstop, float(lum.mean()), sharpness(lum, tb), sharpness(lum, bg_box)))
        print(f"RENDER f/{fstop:g}: {path}; szkliwo {base.linear_to_hex(glaze)}, napis {base.linear_to_hex(text)}")
    for label, fstop, mean, s_text, s_bg in results:
        print(f"POMIAR f/{fstop:g}: srednia jasnosc kadru {mean:.4f}; ostrosc napisu {s_text:.3e}; "
              f"ostrosc tla {s_bg:.3e}")


if __name__ == "__main__":
    main()
