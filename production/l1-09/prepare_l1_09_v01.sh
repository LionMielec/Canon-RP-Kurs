#!/bin/bash
# Canon RP kurs — L1-09-V01: portret przy oknie i wycinek bliższego oka (D-094, D-095).
#
# Wejście: oryginał z Higgsfield (Nano Banana Pro, generacja
# a62de71e-2c9e-4ece-b480-e0f8ac68cc67, 2400 × 1792), zapisany jako
#   production/l1-09/renders/l1-09-v01-oryginal.png
# Folder renders jest poza Git (D-078); oryginał pobiera się ręcznie.
#
# Wyjście (w tym samym folderze renders):
#   l1-09-v01-portret.jpg — cały kadr, 1200 × 896,
#   l1-09-v01-oko.jpg     — wycinek 3:2 z bliższym okiem, 1200 × 800.
#
# Jakość JPEG 85 w sips: te same tablice kompresji co pliki L1-08-V01
# (app/dist/assets/lessons/l1-08/l1-08-v01-*.jpg), sprawdzone 01.11.2026.
# Oryginał nie ma profilu kolorów; osadzamy sRGB jak w plikach L1-08-V01.
#
# Uruchomienie z katalogu repozytorium:
#   bash production/l1-09/prepare_l1_09_v01.sh

set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
RENDERS="$HERE/renders"
SRC="$RENDERS/l1-09-v01-oryginal.png"
PROFILE="/System/Library/ColorSync/Profiles/sRGB Profile.icc"
QUALITY=85

SRC_W=2400
SRC_H=1792
PORTRAIT_W=1200
PORTRAIT_H=896

# Wycinek oka — współrzędne w pikselach oryginału 2400 × 1792, od lewego
# górnego rogu. Bliższe oko: to po lewej stronie zdjęcia (prawe oko osoby,
# od strony okna). Głowa jest lekko obrócona w prawo: czubek nosa leży
# na prawo od środka między oczami, oko po lewej jest szersze i widać
# po jego stronie więcej policzka. Prostokąt obejmuje całe oko z brwią
# i marginesem; brew jest w środku szerokości, oko po prawej go nie
# obejmuje. Proporcja 3:2.
EYE_X=860       # lewy brzeg wycinka
EYE_Y=400       # górny brzeg wycinka
EYE_W=360       # szerokość
EYE_H=240       # wysokość
EYE_OUT_W=1200
EYE_OUT_H=800

[ -f "$SRC" ] || { echo "BRAK oryginału: $SRC" >&2; exit 1; }
[ -f "$PROFILE" ] || { echo "BRAK profilu sRGB: $PROFILE" >&2; exit 1; }

dim() { sips -g "$1" "$2" | awk -v k="$1:" '$1 == k { print $2 }'; }

if [ "$(dim pixelWidth "$SRC")" != "$SRC_W" ] || [ "$(dim pixelHeight "$SRC")" != "$SRC_H" ]; then
  echo "Oryginał nie ma ${SRC_W} × ${SRC_H}" >&2
  exit 1
fi
if [ $((EYE_W * 2)) -ne $((EYE_H * 3)) ]; then
  echo "Wycinek oka nie ma proporcji 3:2" >&2
  exit 1
fi

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# Portret: cały kadr, pomniejszony o połowę.
sips -s format jpeg -s formatOptions "$QUALITY" --embedProfile "$PROFILE" \
  -z "$PORTRAIT_H" "$PORTRAIT_W" "$SRC" --out "$RENDERS/l1-09-v01-portret.jpg" >/dev/null

# Oko: najpierw przycięcie, potem powiększenie — w dwóch wywołaniach, bo sips
# w jednym wywołaniu skaluje przed przycięciem.
sips -c "$EYE_H" "$EYE_W" --cropOffset "$EYE_Y" "$EYE_X" "$SRC" --out "$TMP/oko.png" >/dev/null
sips -s format jpeg -s formatOptions "$QUALITY" --embedProfile "$PROFILE" \
  -z "$EYE_OUT_H" "$EYE_OUT_W" "$TMP/oko.png" --out "$RENDERS/l1-09-v01-oko.jpg" >/dev/null

for f in l1-09-v01-portret.jpg l1-09-v01-oko.jpg; do
  echo "$f: $(dim pixelWidth "$RENDERS/$f") × $(dim pixelHeight "$RENDERS/$f")"
done
