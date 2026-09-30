# SPDX-License-Identifier: GPL-2.0-or-later
#
# Canon RP kurs — L1-03-V04A: scena 3D do ujęcia próbnego (D-050, D-051).
# Wersja 2: kadr z wysokości oczu osoby siedzącej, naturalniejsze materiały,
# trzy projekty kubka w kolorach palety aplikacji.
#
# Buduje od zera jedną scenę (stół, ściana z tynkiem, kubek „Amore Mio”,
# lampa stojąca, obraz na ścianie, książka, pilot, światło z okna) i renderuje
# jedno ujęcie. Między ujęciami zmienia się wyłącznie położenie aparatu.
#
# Przykłady (bez okna):
#   B=/Applications/Blender.app/Contents/MacOS/Blender
#   S=production/l1-03/scene/build_v04a_scene.py
#   # zbliżenie kubka nr 2 z kalibracją koloru:
#   $B -b --factory-startup --python $S -- --view closeup --design 2 \
#      --calibrate production/l1-03/scene/calibration/closeup-2.json --out out.png
#   # ujęcie 1 i 2 z tą samą kalibracją (zmienia się tylko aparat):
#   $B -b --factory-startup --python $S -- --view shot --position 1 --design 2 \
#      --calibrate production/l1-03/scene/calibration/shot-2.json --out p1.png
#   $B -b --factory-startup --python $S -- --view shot --position 2 --design 2 \
#      --use-calibration production/l1-03/scene/calibration/shot-2.json --out p2.png
#   # odstęp słupa lampy od kubka w obrazie dla różnych przesunięć w bok:
#   $B -b --factory-startup --python $S -- --geometry-report
#
# Wszystkie bryły i materiały powstają w tym skrypcie (bez pobranych modeli
# i tekstur). Czcionki: production/l1-03/scene/fonts/ (SIL Open Font License 1.1,
# pliki licencji obok czcionek).

import argparse
import json
import math
import os
import sys

import bmesh
import bpy
import mathutils
import numpy as np
from bpy_extras.object_utils import world_to_camera_view
from mathutils import Euler, Vector

SCENE_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(SCENE_DIR, "fonts")

# ---------------------------------------------------------------------------
# Paleta aplikacji (app/dist/style.css), wartości sRGB
# ---------------------------------------------------------------------------

PALETTE = {
    "lavender": "#ece2f7",
    "pink": "#f6e2ee",
    "bg": "#f8f3fc",
    "violet": "#70429b",
    "violet-dark": "#51316f",
    "focus": "#a33284",
}

# ---------------------------------------------------------------------------
# Parametry sceny (metry)
# ---------------------------------------------------------------------------

TABLE_TOP_Z = 0.75
TABLE_THICKNESS = 0.032
TABLE_X = (-0.80, 0.80)
TABLE_Y = (-0.70, 0.25)       # osoba siedzi przy przedniej krawędzi
WALL_Y = 1.35                 # ściana w tle
LAMP_XY = (0.0, 0.90)         # lampa stojąca między stołem a ścianą, dokładnie za kubkiem
PAINTING = {"x": 0.42, "z": 0.85, "w": 0.32, "h": 0.22}
REMOTE = (0.62, -0.28, -22.0)  # x, y, obrót w stopniach; przy prawym brzegu stołu (rozpraszacz w V02),
                                # poza obszarem blatu odbijanym przez kubek w obu ujęciach V04A

MUG_BASE = Vector((0.0, 0.0, TABLE_TOP_Z))
AIM_POINT = Vector((0.0, 0.0, TABLE_TOP_Z + 0.055))  # środek kubka

# Aparat: Canon EOS RP + RF 50 mm. Matryca ok. 36,0 × 24,0 mm
# (instrukcja EOS RP, PL i EN, s. 119).
SENSOR_WIDTH_MM = 36.0
SENSOR_HEIGHT_MM = 24.0
FOCAL_LENGTH_MM = 50.0
CAMERA_DISTANCE = 0.70        # od środka kubka
EYE_HEIGHT = 0.30             # nad blatem (osoba siedząca)
CAMERA_PITCH_DEG = -16.0      # lekko w dół; kubek w dolnej części kadru
SIDE_STEP = 0.25              # przesunięcie w bok w ujęciu 2: mały krok (lekcja, krok S04)
F_STOP = 8.0
RES_X, RES_Y = 2400, 1600     # kadr 3:2

CLOSEUP_RES = (640, 760)


def srgb_to_linear(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def linear_to_srgb(c):
    c = max(0.0, min(1.0, c))
    return c * 12.92 if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def hex_to_linear(h):
    h = h.lstrip("#")
    return tuple(srgb_to_linear(int(h[i:i + 2], 16) / 255) for i in (0, 2, 4))


def linear_to_hex(rgb):
    return "#" + "".join(f"{round(linear_to_srgb(c) * 255):02x}" for c in rgb)


# ---------------------------------------------------------------------------
# Projekty kubka
# ---------------------------------------------------------------------------

def _rounded(z):
    if z < 0.03:
        return 0.047 - 0.011 * (1 - z / 0.03) ** 2
    return 0.047 - 0.0035 * ((z - 0.03) / 0.08) ** 1.5


def _flared(z):
    if z < 0.009:
        return 0.034
    return 0.037 + (z - 0.009) / 0.101 * 0.013


def _barrel(z):
    return 0.042 + 0.0042 * math.sin(math.pi * z / 0.105)


MUG_DESIGNS = {
    1: {
        "name": "Zaokrąglony dół",
        "radius": _rounded, "height": 0.110, "foot": 0.0,
        "glaze": "lavender", "inner": "lavender", "text": "violet", "accent": None,
        "font": "playfairdisplay/PlayfairDisplay-Italic[wght].ttf",
        "lines": 2, "text_width": 0.050, "text_z": 0.068,
        "handle": {"major": 0.027, "minor": 0.0062, "scale": (0.80, 1.0, 1.10), "z": 0.060},
    },
    2: {
        "name": "Stożek na nóżce",
        "radius": _flared, "height": 0.110, "foot": 0.009,
        "glaze": "pink", "inner": "pink", "text": "violet-dark", "accent": "focus",
        "font": "cormorantgaramond/CormorantGaramond-Italic[wght].ttf",
        "lines": 1, "text_width": 0.060, "text_z": 0.064,
        "handle": {"major": 0.030, "minor": 0.0058, "scale": (0.62, 1.0, 1.22), "z": 0.062},
    },
    3: {
        "name": "Beczułka",
        "radius": _barrel, "height": 0.105, "foot": 0.0,
        "glaze": "bg", "inner": "pink", "text": "violet", "accent": None,
        "font": "greatvibes/GreatVibes-Regular.ttf",
        "lines": 1, "word_space": 2.6, "text_width": 0.064, "text_z": 0.055,
        "handle": {"major": 0.028, "minor": 0.0075, "scale": (0.58, 1.0, 1.28), "z": 0.054},
    },
}
MUG_TEXT = "Amore Mio"


# ---------------------------------------------------------------------------
# Narzędzia
# ---------------------------------------------------------------------------

def link(obj):
    bpy.context.scene.collection.objects.link(obj)
    return obj


def socket(sockets, identifier):
    """Gniazdo węzła po identyfikatorze (węzeł Mix ma kilka gniazd o tej samej nazwie)."""
    return next(s for s in sockets if s.identifier == identifier)


def box(name, size, location, material, rotation_z=0.0, bevel=0.0):
    mesh = bpy.data.meshes.new(name)
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bmesh.ops.scale(bm, vec=Vector(size), verts=bm.verts)
    bm.to_mesh(mesh)
    bm.free()
    obj = link(bpy.data.objects.new(name, mesh))
    obj.location = location
    obj.rotation_euler[2] = rotation_z
    obj.data.materials.append(material)
    if bevel > 0:
        mod = obj.modifiers.new("Bevel", "BEVEL")
        mod.width = bevel
        mod.segments = 3
        mod.limit_method = "ANGLE"
        obj.data.shade_smooth()
        obj.modifiers.new("Smooth", "WEIGHTED_NORMAL").keep_sharp = True
    return obj


def cylinder(name, radius, depth, location, material, vertices=64):
    mesh = bpy.data.meshes.new(name)
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=vertices,
                          radius1=radius, radius2=radius, depth=depth)
    bm.to_mesh(mesh)
    bm.free()
    obj = link(bpy.data.objects.new(name, mesh))
    obj.location = location
    obj.data.materials.append(material)
    mod = obj.modifiers.new("Bevel", "BEVEL")
    mod.width = min(radius, depth) * 0.15
    mod.segments = 2
    mod.limit_method = "ANGLE"
    obj.data.shade_smooth()
    obj.modifiers.new("Smooth", "WEIGHTED_NORMAL").keep_sharp = True
    return obj


def lathe(name, profile, location, materials, material_split=None, steps=160):
    """Bryła obrotowa z profilu [(r, z), ...] wokół osi Z. Ściany profilu od
    indeksu material_split dostają drugi materiał (wnętrze kubka)."""
    mesh = bpy.data.meshes.new(name)
    bm = bmesh.new()
    rings = []
    for i in range(steps):
        a = 2 * math.pi * i / steps
        rings.append([bm.verts.new((r * math.cos(a), r * math.sin(a), z)) for r, z in profile])
    for i in range(steps):
        r0, r1 = rings[i], rings[(i + 1) % steps]
        for j in range(len(profile) - 1):
            f = bm.faces.new((r0[j], r1[j], r1[j + 1], r0[j + 1]))
            f.material_index = 1 if material_split is not None and j >= material_split else 0
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-6)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(mesh)
    bm.free()
    obj = link(bpy.data.objects.new(name, mesh))
    obj.location = location
    for m in materials:
        obj.data.materials.append(m)
    obj.data.shade_smooth()
    return obj


# ---------------------------------------------------------------------------
# Materiały (wyłącznie proceduralne)
# ---------------------------------------------------------------------------

def principled(name, color, roughness=0.5, **inputs):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = (*color, 1.0)
    bsdf.inputs["Roughness"].default_value = roughness
    for key, value in inputs.items():
        bsdf.inputs[key.replace("_", " ")].default_value = value
    return mat


def noise_node(nt, scale, detail=2.0, roughness=0.5, vector=None):
    n = nt.nodes.new("ShaderNodeTexNoise")
    n.inputs["Scale"].default_value = scale
    n.inputs["Detail"].default_value = detail
    n.inputs["Roughness"].default_value = roughness
    if vector is not None:
        nt.links.new(vector, n.inputs["Vector"])
    return n


def map_range(nt, value, to_min, to_max, from_min=0.0, from_max=1.0):
    m = nt.nodes.new("ShaderNodeMapRange")
    m.inputs["From Min"].default_value = from_min
    m.inputs["From Max"].default_value = from_max
    m.inputs["To Min"].default_value = to_min
    m.inputs["To Max"].default_value = to_max
    nt.links.new(value, m.inputs["Value"])
    return m.outputs["Result"]


def wood_material(name, light, dark):
    """Drewno: słoje z pasm fali (okres ok. 6 mm) wygiętych szumem, szersze
    pasma przyrostów, wolna zmiana tonu, zmienna chropowatość (ślady użytkowania)."""
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    nt = mat.node_tree
    bsdf = nt.nodes["Principled BSDF"]
    coord = nt.nodes.new("ShaderNodeTexCoord").outputs["Object"]

    # wygięcie słojów: przesunięcie X o szum zależny od położenia
    warp = noise_node(nt, 2.5, detail=3.0, vector=coord)
    sep = nt.nodes.new("ShaderNodeSeparateXYZ")
    nt.links.new(coord, sep.inputs["Vector"])
    offset = nt.nodes.new("ShaderNodeMath")
    offset.operation = "MULTIPLY_ADD"
    nt.links.new(warp.outputs["Fac"], offset.inputs[0])
    offset.inputs[1].default_value = 0.035
    nt.links.new(sep.outputs["X"], offset.inputs[2])
    comb = nt.nodes.new("ShaderNodeCombineXYZ")
    nt.links.new(offset.outputs["Value"], comb.inputs["X"])
    nt.links.new(sep.outputs["Y"], comb.inputs["Y"])
    nt.links.new(sep.outputs["Z"], comb.inputs["Z"])
    warped = comb.outputs["Vector"]

    fine = nt.nodes.new("ShaderNodeTexWave")
    fine.wave_type = "BANDS"
    fine.bands_direction = "X"
    fine.inputs["Scale"].default_value = 52.0
    fine.inputs["Distortion"].default_value = 1.5
    fine.inputs["Detail"].default_value = 3.0
    nt.links.new(warped, fine.inputs["Vector"])
    # nieregularne włókna: szum rozciągnięty wzdłuż słojów
    stretch = nt.nodes.new("ShaderNodeMapping")
    stretch.inputs["Scale"].default_value = (22.0, 0.9, 1.0)
    nt.links.new(warped, stretch.inputs["Vector"])
    broad = noise_node(nt, 1.0, detail=6.0, roughness=0.6, vector=stretch.outputs["Vector"])

    lines = map_range(nt, fine.outputs["Fac"], 0.0, 0.22, from_min=0.6, from_max=1.0)
    rings = map_range(nt, broad.outputs["Fac"], 0.0, 0.7, from_min=0.4, from_max=0.7)
    grain = nt.nodes.new("ShaderNodeMath")
    grain.operation = "MAXIMUM"
    nt.links.new(lines, grain.inputs[0])
    nt.links.new(rings, grain.inputs[1])

    ramp = nt.nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].color = (*light, 1.0)
    ramp.color_ramp.elements[1].color = (*dark, 1.0)
    nt.links.new(grain.outputs["Value"], ramp.inputs["Fac"])

    tone = noise_node(nt, 1.8, detail=2.0, vector=coord)
    mix = nt.nodes.new("ShaderNodeMix")
    mix.data_type = "RGBA"
    mix.blend_type = "MULTIPLY"
    mix.inputs["Factor"].default_value = 0.18
    nt.links.new(ramp.outputs["Color"], socket(mix.inputs, "A_Color"))
    nt.links.new(tone.outputs["Color"], socket(mix.inputs, "B_Color"))
    nt.links.new(socket(mix.outputs, "Result_Color"), bsdf.inputs["Base Color"])

    # ślady użytkowania: plamy o innym połysku i drobne rysy
    smudge = noise_node(nt, 6.0, detail=4.0, roughness=0.6, vector=coord)
    rough = map_range(nt, smudge.outputs["Fac"], 0.38, 0.62, from_min=0.35, from_max=0.65)
    nt.links.new(rough, bsdf.inputs["Roughness"])
    bump = nt.nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.04
    bump.inputs["Distance"].default_value = 0.0003
    nt.links.new(grain.outputs["Value"], bump.inputs["Height"])
    nt.links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    bsdf.inputs["Specular IOR Level"].default_value = 0.4
    return mat


def plaster_material():
    """Tynk: ciepła biel z łagodną zmianą tonu i nierówną, drobną fakturą."""
    mat = bpy.data.materials.new("Tynk")
    mat.use_nodes = True
    nt = mat.node_tree
    bsdf = nt.nodes["Principled BSDF"]
    coord = nt.nodes.new("ShaderNodeTexCoord").outputs["Object"]
    tone = noise_node(nt, 2.5, detail=3.0, vector=coord)
    ramp = nt.nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].position = 0.35
    ramp.color_ramp.elements[0].color = (*hex_to_linear("#cfc7bb"), 1.0)
    ramp.color_ramp.elements[1].position = 0.65
    ramp.color_ramp.elements[1].color = (*hex_to_linear("#d9d2c7"), 1.0)
    nt.links.new(tone.outputs["Fac"], ramp.inputs["Fac"])
    nt.links.new(ramp.outputs["Color"], bsdf.inputs["Base Color"])
    bsdf.inputs["Roughness"].default_value = 0.95

    coarse = noise_node(nt, 45.0, detail=8.0, roughness=0.65, vector=coord)
    fine = noise_node(nt, 420.0, detail=4.0, vector=coord)
    add = nt.nodes.new("ShaderNodeMath")
    add.operation = "MULTIPLY_ADD"
    nt.links.new(fine.outputs["Fac"], add.inputs[0])
    add.inputs[1].default_value = 0.35
    nt.links.new(coarse.outputs["Fac"], add.inputs[2])
    bump = nt.nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.22
    bump.inputs["Distance"].default_value = 0.0012
    nt.links.new(add.outputs["Value"], bump.inputs["Height"])
    nt.links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    return mat


def glaze_material(name, color):
    """Szkliwo: gładkie, z bardzo delikatną nierównością połysku i powierzchni."""
    mat = principled(name, color, roughness=0.12, Coat_Weight=0.35, Coat_Roughness=0.06)
    nt = mat.node_tree
    bsdf = nt.nodes["Principled BSDF"]
    coord = nt.nodes.new("ShaderNodeTexCoord").outputs["Object"]
    var = noise_node(nt, 90.0, detail=3.0, vector=coord)
    nt.links.new(map_range(nt, var.outputs["Fac"], 0.08, 0.18, 0.35, 0.65), bsdf.inputs["Roughness"])
    ripple = noise_node(nt, 260.0, detail=2.0, vector=coord)
    bump = nt.nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.025
    bump.inputs["Distance"].default_value = 0.0002
    nt.links.new(ripple.outputs["Fac"], bump.inputs["Height"])
    nt.links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    return mat


def painting_material():
    """Jasny, abstrakcyjny obraz: miękkie plamy w ciepłych pastelach."""
    mat = bpy.data.materials.new("Obraz")
    mat.use_nodes = True
    nt = mat.node_tree
    bsdf = nt.nodes["Principled BSDF"]
    bsdf.inputs["Roughness"].default_value = 0.85
    coord = nt.nodes.new("ShaderNodeTexCoord").outputs["Generated"]
    noise = noise_node(nt, 2.2, detail=1.5, vector=coord)
    ramp = nt.nodes.new("ShaderNodeValToRGB")
    els = ramp.color_ramp.elements
    els[0].position = 0.35
    els[0].color = (*hex_to_linear("#efe6d6"), 1.0)
    els[1].position = 0.62
    els[1].color = (*hex_to_linear("#b9cdd6"), 1.0)
    mid = els.new(0.50)
    mid.color = (*hex_to_linear("#e8c6ab"), 1.0)
    nt.links.new(noise.outputs["Fac"], ramp.inputs["Fac"])
    nt.links.new(ramp.outputs["Color"], bsdf.inputs["Base Color"])
    return mat


def build_materials(design):
    d = MUG_DESIGNS[design]
    mats = {
        "table": wood_material("Stol", light=hex_to_linear("#b89878"), dark=hex_to_linear("#7e5f45")),
        "floor": wood_material("Podloga", light=hex_to_linear("#9c7a5c"), dark=hex_to_linear("#6b4f38")),
        "frame": wood_material("Rama", light=hex_to_linear("#e0cfb6"), dark=hex_to_linear("#bfa888")),
        "wall": plaster_material(),
        "ceiling": principled("Sufit", hex_to_linear("#ece8e2"), roughness=0.95),
        "trim": principled("Listwa", hex_to_linear("#ece9e3"), roughness=0.6),
        "glaze": glaze_material("Szkliwo", hex_to_linear(PALETTE[d["glaze"]])),
        "inner": glaze_material("Szkliwo_wnetrze", hex_to_linear(PALETTE[d["inner"]])),
        "print": principled("Nadruk", hex_to_linear(PALETTE[d["text"]]), roughness=0.22,
                            Coat_Weight=0.35, Coat_Roughness=0.06),
        "lamp_metal": principled("Lampa_metal", (0.04, 0.04, 0.04), roughness=0.4, Metallic=1.0),
        "lamp_shade": principled("Lampa_tkanina", hex_to_linear("#ece4d6"), roughness=0.95),
        "painting": painting_material(),
        "book_cover": principled("Ksiazka_okladka", hex_to_linear("#5f7482"), roughness=0.7),
        "book_pages": principled("Ksiazka_kartki", hex_to_linear("#efe8da"), roughness=0.9),
        "remote": principled("Pilot", hex_to_linear("#e9e8e4"), roughness=0.35),
        "remote_buttons": principled("Pilot_przyciski", hex_to_linear("#b5b7ba"), roughness=0.5),
    }
    if d["accent"]:
        mats["accent"] = glaze_material("Akcent", hex_to_linear(PALETTE[d["accent"]]))
    return mats


# ---------------------------------------------------------------------------
# Elementy sceny
# ---------------------------------------------------------------------------

def build_room(mats):
    box("Podloga", (8.0, 8.0, 0.02), (0.0, 0.0, -0.01), mats["floor"])
    box("Sciana_tyl", (8.0, 0.05, 2.8), (0.0, WALL_Y + 0.025, 1.4), mats["wall"])
    box("Sciana_prawa", (0.05, 6.0, 2.8), (2.2, -1.0, 1.4), mats["wall"])
    box("Sciana_przod", (8.0, 0.05, 2.8), (0.0, -3.2, 1.4), mats["wall"])
    box("Sufit", (8.0, 8.0, 0.02), (0.0, 0.0, 2.7), mats["ceiling"])
    box("Listwa", (8.0, 0.015, 0.08), (0.0, WALL_Y - 0.0075, 0.04), mats["trim"])


def build_table(mats):
    cx, cy = sum(TABLE_X) / 2, sum(TABLE_Y) / 2
    sx, sy = TABLE_X[1] - TABLE_X[0], TABLE_Y[1] - TABLE_Y[0]
    box("Blat", (sx, sy, TABLE_THICKNESS), (cx, cy, TABLE_TOP_Z - TABLE_THICKNESS / 2),
        mats["table"], bevel=0.004)
    leg_h = TABLE_TOP_Z - TABLE_THICKNESS
    for i, (x, y) in enumerate([(TABLE_X[0] + 0.06, TABLE_Y[0] + 0.06),
                                (TABLE_X[1] - 0.06, TABLE_Y[0] + 0.06),
                                (TABLE_X[0] + 0.06, TABLE_Y[1] - 0.06),
                                (TABLE_X[1] - 0.06, TABLE_Y[1] - 0.06)]):
        box(f"Noga_{i}", (0.055, 0.055, leg_h), (x, y, leg_h / 2), mats["table"], bevel=0.003)


def mug_profile(d, wall=0.0042, bottom=0.009, samples=44):
    """Profil kubka: dno z zaokrągleniem, ścianka zewnętrzna według r(z),
    zaokrąglona krawędź, ścianka wewnętrzna, dno wewnętrzne.
    Zwraca (profil, indeks pierwszej ściany wnętrza)."""
    r, h, foot = d["radius"], d["height"], d["foot"]
    outer = [(0.0, 0.0), (r(0.0) - 0.005, 0.0), (r(0.0) - 0.0015, 0.0012), (r(0.0) - 0.0002, 0.004)]
    if foot:
        outer += [(r(foot - 0.0005), foot - 0.0005), (r(foot) - 0.0012, foot),
                  (r(foot + 0.0015), foot + 0.0015)]
        start = foot + 0.003
    else:
        start = 0.006
    for i in range(samples + 1):
        z = start + (h - 0.003 - start) * i / samples
        outer.append((r(z), z))
    rim_r = r(h)
    outer += [(rim_r - 0.0006, h - 0.0008), (rim_r - wall / 2, h)]
    split = len(outer) - 1
    inner = [(rim_r - wall + 0.0006, h - 0.0008)]
    for i in range(samples, -1, -1):
        z = bottom + 0.006 + (h - 0.003 - bottom - 0.006) * i / samples
        inner.append((r(z) - wall, z))
    inner += [(r(bottom) - wall - 0.004, bottom + 0.001), (0.0, bottom)]
    return outer + inner, split


def build_mug(mats, design):
    d = MUG_DESIGNS[design]
    profile, split = mug_profile(d)
    mug = lathe("Kubek", profile, MUG_BASE, [mats["glaze"], mats["inner"]], material_split=split)

    hd = d["handle"]
    bpy.ops.mesh.primitive_torus_add(major_radius=hd["major"], minor_radius=hd["minor"],
                                     major_segments=72, minor_segments=24)
    handle = bpy.context.active_object
    handle.name = "Kubek_ucho"
    handle.rotation_euler = (math.radians(90), 0.0, 0.0)
    handle.scale = hd["scale"]
    reach = hd["major"] * hd["scale"][0]
    # ucho po lewej stronie (-X), żeby słup lampy w ujęciu 2 odsłaniał się po prawej
    handle.location = (MUG_BASE.x - d["radius"](hd["z"]) - reach + hd["minor"] * 1.2,
                       MUG_BASE.y, MUG_BASE.z + hd["z"])
    handle.data.materials.append(mats["glaze"])
    handle.data.shade_smooth()

    if d["accent"]:
        # cienka linia akcentu na krawędzi
        bpy.ops.mesh.primitive_torus_add(major_radius=d["radius"](d["height"]) - 0.0021,
                                         minor_radius=0.0014, major_segments=160, minor_segments=12)
        rim = bpy.context.active_object
        rim.name = "Kubek_akcent"
        rim.location = (MUG_BASE.x, MUG_BASE.y, MUG_BASE.z + d["height"] - 0.0002)
        rim.data.materials.append(mats["accent"])
        rim.data.shade_smooth()
    return mug


def fill_glyph_outlines(outline):
    """Wypełnia kontury liter regułą niezerowego nawinięcia (jak w czcionkach
    TrueType). Wbudowane wypełnianie Blendera stosuje regułę parzystości, która
    robi dziury tam, gdzie kontury liter na siebie nachodzą."""
    pts = [(v.co.x, v.co.y) for v in outline.vertices]
    directed = [(pts[e.vertices[0]], pts[e.vertices[1]]) for e in outline.edges]
    cdt_verts, _, cdt_faces, *_ = mathutils.geometry.delaunay_2d_cdt(
        pts, [tuple(e.vertices) for e in outline.edges], [], 0, 1e-7)

    def winding(px, py):
        w = 0
        for (ax, ay), (bx, by) in directed:
            if ay <= py < by or by <= py < ay:
                cross_x = ax + (py - ay) * (bx - ax) / (by - ay)
                if cross_x > px:
                    w += 1 if by > ay else -1
        return w

    faces = []
    for f in cdt_faces:
        cx = sum(cdt_verts[i].x for i in f) / len(f)
        cy = sum(cdt_verts[i].y for i in f) / len(f)
        if winding(cx, cy) != 0:
            faces.append(f)
    mesh = bpy.data.meshes.new("Napis")
    mesh.from_pydata([(v.x, v.y, 0.0) for v in cdt_verts], [], faces)
    return mesh


def build_mug_text(mats, design):
    """Napis „Amore Mio” na ściance kubka, zwrócony w stronę -Y (ku aparatowi
    w ujęciu 1). Szerokość napisu jest dopasowana do projektu, a wierzchołki
    leżą na powierzchni kubka r(z)."""
    d = MUG_DESIGNS[design]
    font = bpy.data.fonts.load(os.path.join(FONT_DIR, d["font"]))
    curve = bpy.data.curves.new("Napis", "FONT")
    curve.body = MUG_TEXT.replace(" ", "\n") if d["lines"] == 2 else MUG_TEXT
    curve.font = font
    curve.size = 1.0
    curve.space_word = d.get("word_space", 1.0)
    curve.align_x = "CENTER"
    curve.align_y = "CENTER"
    curve.resolution_u = 20
    curve.fill_mode = "NONE"   # same kontury; wypełnienie liczymy niżej
    tmp = link(bpy.data.objects.new("Napis_tmp", curve))
    depsgraph = bpy.context.evaluated_depsgraph_get()
    outline = bpy.data.meshes.new_from_object(tmp.evaluated_get(depsgraph))
    bpy.data.objects.remove(tmp)

    mesh = fill_glyph_outlines(outline)
    bpy.data.meshes.remove(outline)

    bm = bmesh.new()
    bm.from_mesh(mesh)
    xs = [v.co.x for v in bm.verts]
    ys = [v.co.y for v in bm.verts]
    k = d["text_width"] / (max(xs) - min(xs))
    cx, cy = (max(xs) + min(xs)) / 2, (max(ys) + min(ys)) / 2
    for v in bm.verts:
        v.co = Vector(((v.co.x - cx) * k, (v.co.y - cy) * k, 0.0))
    for _ in range(10):
        long_edges = [e for e in bm.edges if e.calc_length() > 0.0012]
        if not long_edges:
            break
        bmesh.ops.subdivide_edges(bm, edges=long_edges, cuts=1, use_grid_fill=True)
        bmesh.ops.triangulate(bm, faces=[f for f in bm.faces if len(f.verts) > 3])
    r = d["radius"]
    r_mid = r(d["text_z"])
    for v in bm.verts:
        z = d["text_z"] + v.co.y
        rad = r(z) + 0.00025
        theta = v.co.x / r_mid
        v.co = Vector((rad * math.sin(theta), -rad * math.cos(theta), z))
    bm.to_mesh(mesh)
    bm.free()
    obj = link(bpy.data.objects.new("Napis", mesh))
    obj.location = MUG_BASE
    obj.data.materials.append(mats["print"])
    return obj


def build_floor_lamp(mats):
    x, y = LAMP_XY
    cylinder("Lampa_podstawa", 0.14, 0.022, (x, y, 0.011), mats["lamp_metal"])
    pole_h = 1.32
    cylinder("Lampa_slup", 0.011, pole_h, (x, y, pole_h / 2), mats["lamp_metal"], vertices=32)
    mesh = bpy.data.meshes.new("Lampa_abazur")
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=False, segments=96, radius1=0.20, radius2=0.14, depth=0.28)
    bm.to_mesh(mesh)
    bm.free()
    shade = link(bpy.data.objects.new("Lampa_abazur", mesh))
    shade.location = (x, y, pole_h + 0.10)
    shade.data.materials.append(mats["lamp_shade"])
    shade.modifiers.new("Grubosc", "SOLIDIFY").thickness = 0.003
    shade.data.shade_smooth()


def build_painting(mats):
    p = PAINTING
    box("Rama", (p["w"] + 0.05, 0.025, p["h"] + 0.05), (p["x"], WALL_Y - 0.0125, p["z"]),
        mats["frame"], bevel=0.003)
    box("Obraz", (p["w"], 0.004, p["h"]), (p["x"], WALL_Y - 0.027, p["z"]), mats["painting"])


def build_book(mats):
    x, y, rot = -0.30, -0.08, math.radians(14)
    box("Ksiazka_okladka", (0.155, 0.225, 0.028), (x, y, TABLE_TOP_Z + 0.014),
        mats["book_cover"], rotation_z=rot, bevel=0.0015)
    box("Ksiazka_kartki", (0.150, 0.216, 0.024), (x + 0.004, y, TABLE_TOP_Z + 0.014),
        mats["book_pages"], rotation_z=rot)


def build_remote(mats):
    x, y, rot = REMOTE[0], REMOTE[1], math.radians(REMOTE[2])
    remote = box("Pilot", (0.046, 0.175, 0.020), (x, y, TABLE_TOP_Z + 0.010),
                 mats["remote"], rotation_z=rot, bevel=0.008)
    for i in range(4):
        for j in range(3):
            local = Vector((-0.012 + j * 0.012, 0.045 - i * 0.018, 0.0105))
            local.rotate(remote.rotation_euler)
            cylinder(f"Pilot_przycisk_{i}_{j}", 0.0042, 0.003,
                     remote.location + local, mats["remote_buttons"], vertices=24)


def build_window_light():
    """Miękkie światło dzienne z lewej strony, jak z okna; słabe rozproszone
    światło otoczenia, żeby kierunek światła i cienie były wyraźne."""
    light = bpy.data.lights.new("Okno", "AREA")
    light.shape = "RECTANGLE"
    light.size = 0.9
    light.size_y = 1.2
    light.energy = 160.0
    light.color = (1.0, 0.98, 0.95)
    obj = link(bpy.data.objects.new("Okno", light))
    obj.location = (-1.25, -0.55, 1.30)
    direction = Vector((0.0, 0.0, TABLE_TOP_Z + 0.05)) - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()

    world = bpy.data.worlds.new("Swiat")
    world.use_nodes = True
    bg = world.node_tree.nodes["Background"]
    bg.inputs["Color"].default_value = (0.80, 0.86, 0.95, 1.0)
    bg.inputs["Strength"].default_value = 0.05
    bpy.context.scene.world = world


def camera_location(position, side_step):
    horizontal = math.sqrt(CAMERA_DISTANCE ** 2 - (TABLE_TOP_Z + EYE_HEIGHT - AIM_POINT.z) ** 2)
    x = 0.0 if position == 1 else side_step
    return Vector((AIM_POINT.x + x, AIM_POINT.y - horizontal, TABLE_TOP_Z + EYE_HEIGHT))


def set_mug_xy(x, y):
    """Przestawia kubek (wariant sceny, np. V04B: kubek przy przednim brzegu stołu)."""
    global MUG_BASE, AIM_POINT
    MUG_BASE = Vector((x, y, TABLE_TOP_Z))
    AIM_POINT = Vector((x, y, TABLE_TOP_Z + 0.055))


def make_camera(location, aim, pitch_deg=None, res=(RES_X, RES_Y), yaw_deg=None):
    """Aparat w punkcie location. Kierunek: na punkt aim albo podany wprost
    (yaw_deg, pitch_deg). Kadr pionowy (wyższy niż szerszy) to obrócony aparat:
    36 mm matrycy przypada wtedy na dłuższy, pionowy bok."""
    cam_data = bpy.data.cameras.new("Aparat")
    cam_data.lens = FOCAL_LENGTH_MM
    cam_data.sensor_fit = "HORIZONTAL" if res[0] >= res[1] else "AUTO"
    cam_data.sensor_width = SENSOR_WIDTH_MM
    cam_data.sensor_height = SENSOR_HEIGHT_MM
    cam_data.clip_start = 0.02
    cam_data.dof.use_dof = True
    cam_data.dof.aperture_fstop = F_STOP
    cam_data.dof.aperture_blades = 7
    cam = link(bpy.data.objects.new("Aparat", cam_data))
    cam.location = location
    d = aim - location
    yaw = math.radians(yaw_deg) if yaw_deg is not None else math.atan2(-d.x, d.y)
    pitch = math.radians(pitch_deg) if pitch_deg is not None else math.atan2(d.z, d.xy.length)
    cam.rotation_euler = Euler((math.radians(90) + pitch, 0.0, yaw))
    cam_data.dof.focus_distance = d.length - 0.04   # przednia ścianka kubka
    scene = bpy.context.scene
    scene.camera = cam
    scene.render.resolution_x, scene.render.resolution_y = res
    return cam


def configure_render(out_path, scale, samples, exposure):
    scene = bpy.context.scene
    scene.render.engine = "CYCLES"
    scene.cycles.device = "CPU"
    scene.cycles.samples = samples
    scene.cycles.use_denoising = True
    scene.cycles.denoiser = "OPENIMAGEDENOISE"
    scene.cycles.max_bounces = 8
    scene.render.resolution_percentage = scale
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_depth = "8"
    scene.render.filepath = out_path
    # Standard: kolory na obrazie odpowiadają wartościom sRGB bez dodatkowej krzywej,
    # co pozwala sprawdzić odcień palety bezpośrednio na renderze.
    scene.view_settings.view_transform = "Standard"
    scene.view_settings.look = "None"
    scene.view_settings.exposure = exposure


# ---------------------------------------------------------------------------
# Pomiar i kalibracja koloru na gotowym obrazie
# ---------------------------------------------------------------------------

def measure_colors(path, design):
    """Odczytuje z obrazu: szkliwo (mediana łaty pod napisem, od strony aparatu)
    i napis (mediana rdzenia liter w obrysie napisu). Zwraca kolory liniowe."""
    scene = bpy.context.scene
    cam = scene.camera
    img = bpy.data.images.load(path, check_existing=False)
    w, h = img.size
    px = np.array(img.pixels[:], dtype=np.float32).reshape(h, w, 4)[:, :, :3]
    bpy.data.images.remove(img)
    lin = np.where(px <= 0.04045, px / 12.92, ((px + 0.055) / 1.055) ** 2.4)

    def to_px(p):
        c = world_to_camera_view(scene, cam, p)
        return int(c.x * w), int(c.y * h)

    d = MUG_DESIGNS[design]
    view = (cam.location - MUG_BASE)
    theta = math.atan2(view.x, -view.y) - math.radians(25)
    z = 0.030 if not d["foot"] else d["foot"] + 0.024
    rad = d["radius"](z)
    gx, gy = to_px(MUG_BASE + Vector((rad * math.sin(theta), -rad * math.cos(theta), z)))
    half = max(2, w // 120)
    glaze = np.median(lin[gy - half:gy + half + 1, gx - half:gx + half + 1].reshape(-1, 3), axis=0)

    # maska liter: rzut trójkątów napisu na obraz, potem odjęcie 1 px brzegu,
    # żeby w pomiarze nie było pikseli zmieszanych ze szkliwem
    text = bpy.data.objects["Napis"]
    proj = []
    for v in text.data.vertices:
        c = world_to_camera_view(scene, cam, text.matrix_world @ v.co)
        proj.append((c.x * w, c.y * h))
    proj = np.array(proj)
    mask = np.zeros((h, w), dtype=bool)
    for poly in text.data.polygons:
        tri = proj[list(poly.vertices)]
        x0, y0 = np.floor(tri.min(axis=0)).astype(int)
        x1, y1 = np.ceil(tri.max(axis=0)).astype(int)
        gx_, gy_ = np.meshgrid(np.arange(x0, x1 + 1) + 0.5, np.arange(y0, y1 + 1) + 0.5)
        (ax, ay), (bx, by), (cx, cy) = tri[:3]
        d1 = (gx_ - bx) * (ay - by) - (ax - bx) * (gy_ - by)
        d2 = (gx_ - cx) * (by - cy) - (bx - cx) * (gy_ - cy)
        d3 = (gx_ - ax) * (cy - ay) - (cx - ax) * (gy_ - ay)
        inside = ~(((d1 < 0) | (d2 < 0) | (d3 < 0)) & ((d1 > 0) | (d2 > 0) | (d3 > 0)))
        mask[y0:y1 + 1, x0:x1 + 1] |= inside
    core = mask.copy()
    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        core &= np.roll(mask, (dy, dx), axis=(0, 1))
    text_col = np.median(lin[core], axis=0)
    return tuple(float(c) for c in glaze), tuple(float(c) for c in text_col)


def apply_calibration(cal):
    scene = bpy.context.scene
    scene.view_settings.exposure = cal["exposure"]
    for key, name in (("glaze", "Szkliwo"), ("text", "Nadruk")):
        bsdf = bpy.data.materials[name].node_tree.nodes["Principled BSDF"]
        bsdf.inputs["Base Color"].default_value = (*cal[key], 1.0)
    inner = bpy.data.materials["Szkliwo_wnetrze"].node_tree.nodes["Principled BSDF"]
    inner.inputs["Base Color"].default_value = (*cal["inner"], 1.0)


def calibrate(design, out_path, iterations=3):
    """Dobiera ekspozycję całego obrazu oraz kolor bazowy szkliwa i nadruku tak,
    żeby na gotowym renderze szkliwo i napis miały odcienie z palety.
    Model: kolor na obrazie (liniowo) = kolor bazowy × oświetlenie w danym miejscu."""
    d = MUG_DESIGNS[design]
    t_glaze = np.array(hex_to_linear(PALETTE[d["glaze"]]))
    t_text = np.array(hex_to_linear(PALETTE[d["text"]]))
    t_inner = np.array(hex_to_linear(PALETTE[d["inner"]]))
    cal = {"exposure": 0.0, "glaze": list(t_glaze), "text": list(t_text), "inner": list(t_inner)}
    i = attempts = 0
    while i < iterations:
        attempts += 1
        if attempts > iterations + 6:
            raise RuntimeError("Kalibracja koloru nie zbiega się (przepalone szkliwo).")
        apply_calibration(cal)
        bpy.ops.render.render(write_still=True)
        o_glaze, o_text = (np.array(c) for c in measure_colors(out_path, design))
        print(f"KALIBRACJA {i}: szkliwo {linear_to_hex(o_glaze)} (cel {PALETTE[d['glaze']]}), "
              f"napis {linear_to_hex(o_text)} (cel {PALETTE[d['text']]}), ekspozycja {cal['exposure']:.3f}")
        if o_glaze.max() >= 0.985:
            # przepalony kanał nie mówi, ile światła pada; najpierw zmniejsz ekspozycję
            cal["exposure"] -= 0.5
            continue
        i += 1
        light = o_glaze / np.array(cal["glaze"])
        light_text = o_text / np.array(cal["text"])
        a_glaze = t_glaze / light
        boost = max(1.0, a_glaze.max() / 0.92)
        cal["exposure"] += math.log2(boost)
        cal["glaze"] = list(np.clip(a_glaze / boost, 0.0, 1.0))
        cal["text"] = list(np.clip(t_text / (light_text * boost), 0.0, 1.0))
        cal["inner"] = list(np.clip(t_inner / (light * boost), 0.0, 1.0))
    apply_calibration(cal)
    return {k: (float(v) if k == "exposure" else [float(c) for c in v]) for k, v in cal.items()}


# ---------------------------------------------------------------------------
# Raport geometrii: odstęp słupa lampy od kubka w obrazie
# ---------------------------------------------------------------------------

def geometry_report(design):
    scene = bpy.context.scene
    d = MUG_DESIGNS[design]
    top_z = MUG_BASE.z + d["height"]
    mug_r = max(d["radius"](i / 1000) for i in range(int(d["height"] * 1000) + 1))
    pole_axis = Vector((LAMP_XY[0], LAMP_XY[1], top_z))

    def right_of(target, cam_loc):
        v = target - cam_loc
        v.z = 0.0
        return Vector((v.y, -v.x, 0.0)).normalized()   # kierunek „w prawo” w obrazie

    for step_cm in range(0, 31):
        s = step_cm / 100
        cam = make_camera(camera_location(2 if s else 1, s), AIM_POINT, CAMERA_PITCH_DEG)
        bpy.context.view_layer.update()
        edge_z = Vector((0.0, 0.0, d["height"] * 0.8))
        mug_c = world_to_camera_view(scene, cam, MUG_BASE + edge_z).x * RES_X
        mug_right = world_to_camera_view(
            scene, cam, MUG_BASE + edge_z + right_of(MUG_BASE, cam.location) * mug_r).x * RES_X
        pole_left = world_to_camera_view(
            scene, cam, pole_axis - right_of(pole_axis, cam.location) * 0.011).x * RES_X
        mug_w = 2 * (mug_right - mug_c)
        gap = pole_left - mug_right
        print(f"GEOMETRIA przesuniecie {step_cm:2d} cm: odstep slup-kubek {gap:7.1f} px "
              f"({gap / mug_w:5.2f} szerokosci kubka; kubek {mug_w:.0f} px)")
        bpy.data.objects.remove(cam)


# ---------------------------------------------------------------------------
# Pozostałe ujęcia L1-03 z tej samej sceny (V01, V02, V03, V04B)
# Wszystkie: ten sam kubek, światło, kalibracja koloru i ustawienia aparatu co V04A v3.
# V01-przed = V04A pozycja 1, V03-poziomo = V04A pozycja 2 (kopie plików, bez renderu).
# ---------------------------------------------------------------------------

V04A_HORIZONTAL = math.sqrt(CAMERA_DISTANCE ** 2 - (EYE_HEIGHT - 0.055) ** 2)  # 0,656 m
V04B_MUG_Y = TABLE_Y[0] + 0.05 + 0.047   # kubek ok. 5 cm od przedniej krawędzi stołu
V04B_HORIZONTAL = 0.70

SHOTS = {
    # V01-po: ta sama odległość w poziomie co „przed”, aparat 56 cm nad blatem, celuje w kubek;
    # najmniejsza wysokość, przy której nad kubkiem widać już tylko blat (zapas >= 1/10 wys. kubka)
    "v01-po": {"camera": (0.0, -V04A_HORIZONTAL, TABLE_TOP_Z + 0.56)},
    # V02: stały kierunek aparatu (skręt 11,6° w prawo, 10,3° w dół); A: książka ucięta przy lewej
    # krawędzi, pilot wchodzi przy prawej; B: aparat 12 cm do przodu i 3 cm w prawo, brzegi czyste
    "v02-a": {"camera": (-0.05, -1.35, TABLE_TOP_Z + EYE_HEIGHT), "yaw": -11.6, "pitch": -10.3},
    "v02-b": {"camera": (-0.02, -1.23, TABLE_TOP_Z + EYE_HEIGHT), "yaw": -11.6, "pitch": -10.3},
    # V03-pionowo: położenie i kierunek aparatu jak V04A pozycja 2, kadr obrócony do pionu
    "v03-pionowo": {"camera": (SIDE_STEP, -V04A_HORIZONTAL, TABLE_TOP_Z + EYE_HEIGHT),
                    "pitch": CAMERA_PITCH_DEG, "res": (RES_Y, RES_X)},
    # V04B: kubek przy przednim brzegu stołu; aparat 0,70 m w poziomie od kubka, zawsze celuje w kubek
    "v04b-1": {"mug": (0.0, V04B_MUG_Y), "camera": (0.0, V04B_MUG_Y - V04B_HORIZONTAL, TABLE_TOP_Z + 0.055)},
    "v04b-2": {"mug": (0.0, V04B_MUG_Y), "camera": (0.0, V04B_MUG_Y - V04B_HORIZONTAL, TABLE_TOP_Z + 0.30)},
    "v04b-3": {"mug": (0.0, V04B_MUG_Y), "camera": (0.0, V04B_MUG_Y - V04B_HORIZONTAL, TABLE_TOP_Z - 0.03)},
}


def build_scene(design):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    mats = build_materials(design)
    build_room(mats)
    build_table(mats)
    build_mug(mats, design)
    build_mug_text(mats, design)
    build_floor_lamp(mats)
    build_painting(mats)
    build_book(mats)
    build_remote(mats)
    build_window_light()


def main():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    parser = argparse.ArgumentParser()
    parser.add_argument("--view", choices=("shot", "closeup"), default="shot")
    parser.add_argument("--design", type=int, choices=(1, 2, 3), default=1)
    parser.add_argument("--position", type=int, choices=(1, 2), default=1)
    parser.add_argument("--side-step", type=float, default=SIDE_STEP)
    parser.add_argument("--out")
    parser.add_argument("--scale", type=int, default=100)
    parser.add_argument("--samples", type=int, default=256)
    parser.add_argument("--calibrate", help="zapisz kalibrację koloru do pliku JSON")
    parser.add_argument("--use-calibration", help="użyj kalibracji z pliku JSON")
    parser.add_argument("--geometry-report", action="store_true")
    parser.add_argument("--shot", choices=sorted(SHOTS), help="pozostałe ujęcia L1-03 (V01, V02, V03, V04B)")
    args = parser.parse_args(argv)

    shot = SHOTS.get(args.shot)
    if shot and "mug" in shot:
        set_mug_xy(*shot["mug"])
    build_scene(args.design)
    if args.geometry_report:
        geometry_report(args.design)
        return

    if shot:
        make_camera(Vector(shot["camera"]), AIM_POINT, pitch_deg=shot.get("pitch"),
                    res=shot.get("res", (RES_X, RES_Y)), yaw_deg=shot.get("yaw"))
    elif args.view == "closeup":
        location = MUG_BASE + Vector((0.0, -0.40, 0.11))
        make_camera(location, AIM_POINT, res=CLOSEUP_RES)
    else:
        make_camera(camera_location(args.position, args.side_step), AIM_POINT, CAMERA_PITCH_DEG)
    configure_render(os.path.abspath(args.out), args.scale, args.samples, 0.0)

    if args.use_calibration:
        with open(args.use_calibration) as f:
            apply_calibration(json.load(f))
    if args.calibrate:
        cal = calibrate(args.design, os.path.abspath(args.out))
        os.makedirs(os.path.dirname(os.path.abspath(args.calibrate)), exist_ok=True)
        with open(args.calibrate, "w") as f:
            json.dump(cal, f, indent=2)

    bpy.ops.render.render(write_still=True)
    glaze, text = measure_colors(os.path.abspath(args.out), args.design)
    d = MUG_DESIGNS[args.design]
    print(f"POMIAR: szkliwo {linear_to_hex(glaze)} (cel {PALETTE[d['glaze']]}), "
          f"napis {linear_to_hex(text)} (cel {PALETTE[d['text']]})")


if __name__ == "__main__":
    main()
