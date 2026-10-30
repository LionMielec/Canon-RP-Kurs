# L1-08 — karta wizualno-produkcyjna

Aktualne statusy materiałów: docs/16_ASSET_MANIFEST.md (D-074). Statusy poniżej są historyczne.

Stan: 30.10.2026. Dokument produkcyjny; zgodnie z D-048 jego treść nie jest widoczna w kursie.

Treść lekcji: `docs/L1-08_CHCE_MIEC_WIECEJ_RZECZY_OSTRYCH.md` (brama 2, D-090). Zakres: D-089.

## Kroki lekcji

| ID | Krok | Materiał |
|---|---|---|
| L1-08-S01 | Najpierw zobacz, o co chodzi | L1-08-V01 |
| L1-08-S02 | Sprawdź, czy aparat jest gotowy | — |
| L1-08-S03 | Ustaw punkt ostrości na środkowym przedmiocie | — |
| L1-08-S04 | Ustaw większą liczbę przy F | L1-07-V03 (podpunkt 1); L1-02-V04 (podpunkt 2) |
| L1-08-S05 | Większa liczba, więcej rzeczy ostrych | L1-08-V02 |
| Ćwiczenie | Trzy zdjęcia, jeden kadr | L1-08-V03 (przed ćwiczeniem); L1-02-V03 („Porównaj”) |
| Pomoc | Jeśli coś nie działa | L1-05-V02 („Obracam pokrętło…”) |

## Zasady dla materiałów L1-08
- Pochodzenie każdego materiału według D-057: WŁASNE, RENDER, WOLNA LICENCJA albo CANON — DO PODMIANY.
- Rendery powstają w scenie Blender z L1-03 i L1-07 (D-051): ten sam regał w tle, ten sam wirtualny aparat; między klatkami jednego materiału zmienia się dokładnie jedna rzecz — przysłona. Dodatkowe elementy sceny tylko własne, proste, bez gotowych modeli. Skrypty w repozytorium, pełne rendery lokalnie (D-078), do `review/` tylko lekkie kopie (D-053).
- Najpierw podgląd w rozdzielczości podglądu do oceny Claude w czacie i właściciela.
- Higgsfield w tej lekcji nie jest używany (D-090).
- Rysunki z instrukcji Canon (D-056): plik kończy się na `-canon`, przechowywany lokalnie, nigdy w publicznym repozytorium ani w `review/`.
- Materiał bez źródła nie ma zamiennika; w aplikacji stoi jawne miejsce na brakujący materiał.

## Materiały

| ID | Krok | Co dokładnie pokazuje | Źródło | Pochodzenie | Plik docelowy | Status |
|---|---|---|---|---|---|---|
| L1-08-V01 | S01 | Trzy klatki tej samej sceny z L1-07 (regał w tle, aparat 50 mm, matryca jak w scenie): przedni kubek (wzór 2) ok. 0,8 m od aparatu, środkowy kubek (wzór 1, napis „Amore Mio”, w miejscu kubka z L1-07, ok. 1 m) — ostrość na jego napisie, stojąca książka z napisem „Notatki” ok. 1,2 m; przedmioty przesunięte w bok, wszystkie widoczne, napisy się nie zasłaniają; f/1.8, f/4.0, f/8; zmienia się tylko przysłona, jasność wszystkich taka sama | render | RENDER | `assets/lessons/l1-08/l1-08-v01-f18.jpg`, `-f40.jpg`, `-f80.jpg` | `TO_DESIGN` |
| L1-08-V02 | S05 | Schemat z góry: prosty prostokąt „aparat”, trzy przedmioty w szeregu (0,8 / 1,0 / 1,2 m), dwa panele „F1.8” i „F8”; jasny zasięg ostrości wokół środkowego przedmiotu — przy F1.8 wąski (tylko środkowy), przy F8 szeroki (wszystkie trzy), za punktem ostrości nieco dłuższy niż przed nim; bez szczegółów wyglądu aparatu; kolory ze stylu aplikacji | schemat SVG | WŁASNE | `assets/lessons/l1-08/l1-08-v02-pas-ostrosci.svg` | `TO_DESIGN` |
| L1-08-V03 | przed ćwiczeniem | Karta „F1.8 → F4.0 → F8 → porównaj przód i tył” | komponent aplikacji, jak L1-07-V04 | — | — | `TO_DESIGN` |

Materiały z wcześniejszych lekcji użyte w L1-08 (bez nowych plików):
- S04, podpunkt 1: dolny pasek ekranu z liczbą przy F — `assets/lessons/l1-07/l1-07-v03-liczba-f-canon.png` (L1-07-V03; tylko lokalnie, D-056).
- S04, podpunkt 2: główne pokrętło — `assets/lessons/l1-02/l1-02-main-dial.jpg` (L1-02-V04).
- Ćwiczenie, „Porównaj”: przycisk odtwarzania — `assets/lessons/l1-02/l1-02-v03-playback-button.jpg` (L1-02-V03).
- Pomoc „Obracam pokrętło, a zmienia się jasność…”: pokrętło przy LOCK — `assets/lessons/l1-05/l1-05-v02-pokretlo-przy-lock.jpg` (L1-05-V02).

## Tabela źródeł (D-048)

| Twierdzenie w lekcji | Źródło |
|---|---|
| W Av Ania wybiera liczbę przy F, aparat dobiera czas; jasność standardowa | instrukcja PL/EN, s. 100 |
| Większa liczba F — szerszy obszar ostrości od pierwszego planu do tła | instrukcja PL/EN, s. 100, 101; Canon UK, „Depth of field”, https://www.canon.co.uk/pro/infobank/depth-of-field/ |
| Zapis „F4.0” na ekranie | instrukcja PL/EN, s. 101 (rysunek) |
| Większa liczba F = dłuższy czas | instrukcja PL/EN, s. 101 (wniosek ze wskazówek do migającego czasu); Canon UK, „Depth of field” (jw.) |
| Ostrość sięga tylko pewien kawałek przed i za punktem ostrości; przedmiot dalej wypada poza zasięg | Canon UK, „Depth of field” (jw.); Canon U.S.A., RF Lens World, „Depth of Field”, https://www.usa.canon.com/pro/rf-lens-world/features/depth-of-field |
| Oprzeć łokcie o stół, spust spokojnie | Canon Europe, „Sharper photos”, https://canon-europe.com/canon-club/sharper-photos; instrukcja PL/EN, s. 54 |
| Miga 30" — za ciemno; miga 1/4000 — za jasno | instrukcja PL/EN, s. 101 |
| Pokrętło przy LOCK zmienia jasność | instrukcja PL/EN, s. 57, 128 |

Szczegóły: `docs/L1-08_ZRODLA_INSTRUKCJA.md`.

## Kontekst dla nauczyciela AI
Cel ćwiczenia: świadomy wybór większej liczby przy F, gdy ostrych ma być kilka przedmiotów, przy stałym kadrze i punkcie ostrości na środkowym przedmiocie. AI w pierwszej kolejności sprawdza: (1) czy przy F8 przedni i tylny przedmiot są czytelniejsze niż przy F1.8, a środkowy ostry na wszystkich zdjęciach, (2) czy Ania zauważa kompromis: przy F8 tło jest mniej rozmyte. AI nie proponuje jeszcze: zmiany czasu, ISO, innych trybów, statywu, ogniskowej ani oceny kompozycji.

## Do sprawdzenia na aparacie Ani
Lista w `docs/L1-08_ZRODLA_INSTRUKCJA.md`.
