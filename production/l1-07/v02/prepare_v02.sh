#!/bin/sh
# Canon RP kurs — L1-07-V02: pokrętło trybów, oznaczenie napisu Av (D-084).
# Ten sam wycinek co L1-04-V02 (620 × 620 px, lewy górny róg x 900, y 700
# w zdjęciu fbe2fd62…, 2048 × 1592 px); oznaczenie napisu Av rysuje aplikacja
# jako znacznik „halo”: środek x 57 %, y 34 %, szerokość i wysokość 13 %
# (w L1-04-V02 dla P: x 38 %, y 35 %, 13 %). Sprawdzone na próbnym pierścieniu
# 22.10.2026; podgląd review/l1-07/l1-07-v02-pokretlo-av-znacznik-probny.jpg.
# Uruchamiać z katalogu głównego repozytorium.
set -eu
SRC=materials/camera-source-pack-2026-09-24/raw/fbe2fd62-e8ab-465b-b340-b6d0b4458622.jpg
OUT=production/assets/l1-07/l1-07-v02-pokretlo-av.jpg
mkdir -p "$(dirname "$OUT")"
sips -s format jpeg -s formatOptions 92 -c 620 620 --cropOffset 700 900 "$SRC" --out "$OUT" >/dev/null
sips -g pixelWidth -g pixelHeight "$OUT"
