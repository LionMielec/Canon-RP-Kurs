#!/usr/bin/env python3
"""Canon RP kurs — L1-06-V02: schemat z góry, okno, przedmiot i trzy miejsca Ani.

Jeden schemat w trzech plikach; w każdym podświetlone jest inne miejsce Ani,
pozostałe dwa są przygaszone. Kolory i krój jak schemat L1-03-V05 część B
(paleta aplikacji). Nazwy miejsc według docs/24_SLOWNIK_NAZW.md.

Przykład:
  python3 production/l1-06/v02/build_v02_schemat.py
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))

# Paleta jak L1-03-V05 część B
BG = "#f8f3fc"
PANEL = "#fffdfd"
LINE = "#e6dcec"
LIGHT = "#ece2f7"
VIOLET = "#70429b"
VIOLET_DARK = "#51316f"
TEXT = "#382343"
OBJECT = "#a33284"
MUTED_FILL = "#ddd0ea"
MUTED_DARK = "#c4b3d6"
MUTED_TEXT = "#a898b8"

WIDTH, HEIGHT = 800, 640
OBJ = (400, 330)

# (numer, nazwa, środek miejsca Ani, kierunek patrzenia w stopniach: 0 = w dół rysunku,
#  położenie podpisu, wyrównanie podpisu)
PLACES = [
    (1, "światło z przodu", (400, 180), 0, (452, 191), "start"),
    (2, "światło z boku", (150, 330), -90, (160, 412), "middle"),
    (3, "światło od tyłu", (400, 510), 180, (452, 521), "start"),
]


def place(number, name, center, facing, label, anchor, active):
    x, y = center
    fill, dark = (VIOLET, VIOLET_DARK) if active else (MUTED_FILL, MUTED_DARK)
    num_col = "#ffffff" if active else MUTED_TEXT
    txt_col = TEXT if active else MUTED_TEXT
    out = []
    # aparat przed Anią, skierowany na przedmiot (rysowany dla kierunku „w dół”, potem obrót)
    out.append(f'<g transform="translate({x} {y}) rotate({facing})">'
               f'<rect x="-22" y="26" width="44" height="18" rx="4" fill="{dark}"/>'
               f'<rect x="-10" y="42" width="20" height="14" rx="3" fill="{dark}"/></g>')
    out.append(f'<circle cx="{x}" cy="{y}" r="32" fill="{fill}"/>')
    out.append(f'<text x="{x}" y="{y + 12}" text-anchor="middle" font-size="34" font-weight="700" '
               f'fill="{num_col}">{number}</text>')
    weight = 700 if active else 600
    out.append(f'<text x="{label[0]}" y="{label[1]}" text-anchor="{anchor}" font-size="30" '
               f'font-weight="{weight}" fill="{txt_col}">{name}</text>')
    return "\n  ".join(out)


def svg(active_number):
    active_name = next(n for k, n, *_ in PLACES if k == active_number)
    desc = ("Widok z góry. Na górze ściana z oknem, blisko okna przedmiot. Trzy miejsca Ani "
            "z aparatem skierowanym na przedmiot: 1 między oknem a przedmiotem, plecami do okna; "
            "2 z boku, okno z jej boku; 3 za przedmiotem, twarzą do okna. "
            f"Podświetlone miejsce {active_number}: {active_name}.")
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" '
        f'aria-labelledby="t d" font-family="-apple-system, BlinkMacSystemFont, \'Segoe UI\', sans-serif">',
        f'  <title id="t">Miejsce {active_number}: {active_name}</title>',
        f'  <desc id="d">{desc}</desc>',
        f'  <rect width="{WIDTH}" height="{HEIGHT}" fill="{BG}"/>',
        # pokój i ściana z oknem
        f'  <rect x="30" y="74" width="740" height="536" rx="16" fill="{PANEL}" stroke="{LINE}" stroke-width="2"/>',
        f'  <path d="M300 96 L500 96 L610 600 L190 600 Z" fill="{LIGHT}" opacity="0.6"/>',
        f'  <rect x="30" y="74" width="740" height="22" rx="4" fill="{LINE}"/>',
        f'  <rect x="300" y="68" width="200" height="34" rx="4" fill="{PANEL}" stroke="{VIOLET}" stroke-width="4"/>',
        f'  <text x="400" y="52" text-anchor="middle" font-size="30" font-weight="700" fill="{TEXT}">okno</text>',
    ]
    # najpierw miejsca przygaszone, na końcu podświetlone (na wierzchu)
    for active in (False, True):
        for number, name, center, facing, label, anchor in PLACES:
            if (number == active_number) == active:
                parts.append("  " + place(number, name, center, facing, label, anchor, active))
        if not active:
            # linia od podświetlonego miejsca do przedmiotu, pod przedmiotem
            x, y = next(c for k, _, c, *_ in PLACES if k == active_number)
            parts.append(f'  <line x1="{x}" y1="{y}" x2="{OBJ[0]}" y2="{OBJ[1]}" stroke="{VIOLET}" '
                         f'stroke-width="4" stroke-dasharray="10 8" stroke-linecap="round"/>')
            parts.append(f'  <circle cx="{OBJ[0]}" cy="{OBJ[1]}" r="34" fill="{OBJECT}"/>')
    parts.append("</svg>\n")
    return "\n".join(parts)


def main():
    for number in (1, 2, 3):
        path = os.path.join(HERE, f"l1-06-v02-schemat-{number}.svg")
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg(number))
        print(path)


if __name__ == "__main__":
    main()
