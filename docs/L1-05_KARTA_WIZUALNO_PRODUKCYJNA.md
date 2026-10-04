# L1-05 — karta wizualno-produkcyjna

Aktualne statusy materiałów: docs/16_ASSET_MANIFEST.md (D-074). Statusy poniżej są historyczne.

Stan: 03.10.2026. Dokument produkcyjny; zgodnie z D-048 jego treść nie jest widoczna w kursie.

## Zasady dla materiałów L1-05
- Pochodzenie każdego materiału według D-057: WŁASNE, RENDER, WOLNA LICENCJA albo CANON — DO PODMIANY.
- Rysunki z instrukcji Canon (D-056): plik kończy się na `-canon`, przechowywany lokalnie, nigdy w publicznym repozytorium ani w publicznej wersji aplikacji. W wersji bez pliku aplikacja pokazuje w tym miejscu jawne miejsce na brakujący materiał.
- Wycinek z rysunku Canon obejmuje tylko wskazany rysunek, bez numerów stron, podpisów i tekstu instrukcji.
- Oznaczenia elementów statyczne i wyraźne, w stylu zatwierdzonym w L1-01 i L1-02 (D-038). Bez animacji.
- Materiał bez źródła nie ma zamiennika; w aplikacji stoi jawne miejsce na brakujący materiał.

## Materiały

| ID | Krok | Co dokładnie pokazuje | Źródło | Pochodzenie | Plik docelowy | Status |
|---|---|---|---|---|---|---|
| L1-05-V01 | S01 | Trzy rendery jednej sceny: −1, 0, +1 stopnia; aparat, przedmioty i światło stałe | scena Blender z L1-04: ujęcie `l1-04-blizej`, kubek 1, kalibracja `shot-1.json`; różni się tylko ekspozycja w zarządzaniu kolorem (`--exposure-offset` −1, 0, +1) | RENDER | `assets/lessons/l1-05/l1-05-v01-minus1.jpg`, `l1-05-v01-zero.jpg`, `l1-05-v01-plus1.jpg` | `APPROVAL_PENDING` |
| L1-05-V02 | S02, pomoc | Góra aparatu Ani: pokrętło trybów, oznaczone pokrętło przy LOCK i napis LOCK | `fbe2fd62-e8ab-465b-b340-b6d0b4458622.jpg` | WŁASNE | `assets/lessons/l1-05/l1-05-v02-pokretlo-przy-lock.jpg` | `APPROVAL_PENDING` |
| L1-05-V03 | S03, pomoc | Ekran aparatu Ani w trybie P, skala jasności, znacznik przy 0 | BRAK — zdjęcie po powrocie właściciela, razem z L1-04 V07 i V18 | — | — | brak źródła; w aplikacji jawne miejsce na brakujący materiał, bez zamiennika |
| L1-05-V04 | S04 | Dwa paski skali, znacznik w stronę plusa i minusa | instrukcja PL, s. 128 | CANON — DO PODMIANY | `assets/lessons/l1-05/l1-05-v04-skala-jasnosci-canon.png` (tylko lokalnie) | `APPROVAL_PENDING` |
| L1-05-V05 | ćwiczenie | Karta: „0 → minus 1 → plus 1 → porównaj → wróć do 0” | bez pliku | — | komponent aplikacji | komponent UI |

Materiały z wcześniejszych lekcji użyte w L1-05 (bez nowych plików):
- S05, podpunkt 2: przycisk odtwarzania — `assets/lessons/l1-02/l1-02-v03-playback-button.jpg` (L1-02-V03).
- Pomoc, „Obracam pokrętło…”: pokrętło trybów z literą P — `assets/lessons/l1-04/l1-04-v02-pokretlo-p.jpg` (L1-04-V02).

## Tabela źródeł (D-048)

| Twierdzenie w lekcji | Źródło |
|---|---|
| Korekta w P: pokrętło szybkiej kontroli, spust do połowy, skala −3…+3 co 1/3, powrót na środek skali | instrukcja PL, s. 57, 128 |
| Korekta zostaje po wyłączeniu aparatu | instrukcja PL, s. 128; Canon Europe — Exposure Compensation |
| W A+ korekta nie działa | instrukcja PL, s. 110, 114–115, 128 |
| Pomocnik rozjaśniający (Autom. optymalizator jasności) może osłabić ciemniejsze zdjęcie | instrukcja PL, s. 128, 136 |
| Ekran pokazuje jasność zdjęcia przy włączonej symulacji; zdjęcie i tak zgodne z ustawieniem | instrukcja PL, s. 139, 231 |
| Jasność ekranu nie zmienia zdjęcia | instrukcja PL, s. 373 |
| Liczby przy skali się zmieniają (rysunki: inna przysłona) | instrukcja PL, s. 128 |
| Aparat zakłada średnią scenę: jasny przedmiot wychodzi ciemniej, ciemny jaśniej; nie ma jednej poprawnej jasności | Canon Europe — Exposure Compensation; Canon Asia SNAPSHOT — Camera Basics #4 |
| Plus jaśniej, minus ciemniej; 1 stopień = dwa razy więcej/mniej światła | Canon Europe; Canon Asia SNAPSHOT — Camera Basics #4 |

## Do sprawdzenia na aparacie Ani (po powrocie właściciela, D-056)
Lista w `docs/L1-05_ZRODLA_INSTRUKCJA.md`, sekcja „Do sprawdzenia na aparacie Ani”, oraz porównanie rysunku V04 z ekranem aparatu.
