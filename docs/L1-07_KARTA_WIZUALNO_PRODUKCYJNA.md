# L1-07 — karta wizualno-produkcyjna

Aktualne statusy materiałów: docs/16_ASSET_MANIFEST.md (D-074). Statusy poniżej są historyczne.

Stan: 22.10.2026. Dokument produkcyjny; zgodnie z D-048 jego treść nie jest widoczna w kursie.

Treść lekcji: `docs/L1-07_ROZMYWAM_TLO.md` (brama 2, D-084). Zakres: D-083.

## Kroki lekcji

| ID | Krok | Materiał |
|---|---|---|
| L1-07-S01 | Najpierw zobacz, o co chodzi | L1-07-V01 |
| L1-07-S02 | Przestaw pokrętło na Av | L1-07-V02 |
| L1-07-S03 | Sprawdź punkt ostrości | — |
| L1-07-S04 | Znajdź liczbę przy F | L1-07-V03 |
| L1-07-S05 | Zmień liczbę głównym pokrętłem | L1-02-V04 (główne pokrętło) |
| L1-07-S06 | Mała liczba, rozmyte tło | — |
| Ćwiczenie | To samo zdjęcie, dwa razy | L1-07-V04 (przed ćwiczeniem); L1-02-V03 („Porównaj”) |
| Pomoc | Jeśli coś nie działa | L1-05-V02 („Obracam pokrętło…”); L1-07-V02 („Liczba przy F nie chce się zmienić”) |

## Zasady dla materiałów L1-07
- Pochodzenie każdego materiału według D-057: WŁASNE, RENDER, WOLNA LICENCJA albo CANON — DO PODMIANY.
- Rendery powstają w scenie Blender z L1-03 (D-051): ten sam kubek, ten sam wirtualny aparat; między wersjami jednego materiału zmienia się dokładnie jedna rzecz. Dodatkowe elementy sceny tylko własne, proste, bez gotowych modeli. Skrypty w repozytorium, pełne rendery lokalnie (D-078), do `review/` tylko lekkie kopie (D-053).
- Najpierw jedna para w rozdzielczości podglądu do oceny właściciela.
- Rysunki z instrukcji Canon (D-056): plik kończy się na `-canon`, przechowywany lokalnie, nigdy w publicznym repozytorium ani w `review/`. W wersji bez pliku aplikacja pokazuje w tym miejscu jawne miejsce na brakujący materiał.
- Oznaczenia elementów statyczne i wyraźne, w stylu zatwierdzonym w L1-01 i L1-02 (D-038). Bez animacji.
- Materiał bez źródła nie ma zamiennika; w aplikacji stoi jawne miejsce na brakujący materiał.

## Materiały

| ID | Krok | Co dokładnie pokazuje | Źródło | Pochodzenie | Plik docelowy | Status |
|---|---|---|---|---|---|---|
| L1-07-V01 | S01 | Para tej samej sceny: kubek z napisem, wyraźne tło 2–3 m za kubkiem, aparat ok. 1 m od kubka, ostrość na napisie, ogniskowa 50 mm i matryca jak w istniejącej scenie; przysłona f/1.8 (tło rozmyte) i f/5.6 (tło wyraźniejsze). Zmienia się tylko przysłona; jasność obu zdjęć taka sama | render, scena Blender z `production/l1-03/scene/` | RENDER | `assets/lessons/l1-07/l1-07-v01-f18.jpg`, `l1-07-v01-f56.jpg` | `TO_DESIGN` |
| L1-07-V02 | S02, Pomoc | Pokrętło trybów ze statycznym oznaczeniem napisu Av | wycinek z `fbe2fd62-e8ab-465b-b340-b6d0b4458622.jpg`, tak jak L1-04-V02 | WŁASNE | `assets/lessons/l1-07/l1-07-v02-pokretlo-av.jpg` | `TO_PREPARE` |
| L1-07-V03 | S04 | Dolny pasek ekranu: „F5.6” i skala jasności | instrukcja PL, s. 100 (krok 2) | CANON — DO PODMIANY | `assets/lessons/l1-07/l1-07-v03-liczba-f-canon.png` (tylko lokalnie) | `TO_PREPARE` |
| L1-07-V04 | przed ćwiczeniem | Karta: „F1.8 → F5.6 → porównaj tło” | bez pliku, jak L1-05-V05 | — | komponent aplikacji | `TO_DESIGN` |

Materiały z wcześniejszych lekcji użyte w L1-07 (bez nowych plików):
- S05, podpunkt 1: główne pokrętło — `assets/lessons/l1-02/l1-02-main-dial.jpg` (L1-02-V04).
- Ćwiczenie, „Porównaj”: przycisk odtwarzania — `assets/lessons/l1-02/l1-02-v03-playback-button.jpg` (L1-02-V03).
- Pomoc „Obracam pokrętło, a zmienia się jasność…”: pokrętło przy LOCK — `assets/lessons/l1-05/l1-05-v02-pokretlo-przy-lock.jpg` (L1-05-V02).

## Tabela źródeł (D-048)

| Twierdzenie w lekcji | Źródło |
|---|---|
| W Av Ania wybiera liczbę przy F, a czas aparat dobiera sam; Av jest na pokrętle trybów | instrukcja PL/EN, s. 100 |
| Av leży dwie pozycje od P, za Tv | instrukcja PL/EN, s. 34; zdjęcie aparatu Ani `fbe2fd62…` |
| Liczbę przy F zmienia główne pokrętło, patrząc na ekran | instrukcja PL/EN, s. 56, 100 (krok 2) |
| Na ekranie „F5.6” na dolnym pasku, obok skala jasności | instrukcja PL/EN, s. 100 (krok 2), s. 592 |
| Mniejsza liczba — tło bardziej rozmyte; większa — więcej ostrego | instrukcja PL/EN, s. 100; Canon Europe, „Top tips for bokeh”, https://www.canon-europe.com/get-inspired/tips-and-techniques/bokeh-photography/ |
| Im dalej tło za przedmiotem, tym mocniej się rozmywa | Canon Europe, „Top tips for bokeh” (jw.); Canon Singapore SNAPSHOT, „Lens Basics #3: Creating Bokeh”, https://snapshot.asia.canon/en/article/lens-basics-3-creating-bokeh |
| Najmniejsza liczba obiektywu Ani to 1.8 | Canon Camera Museum, „RF50mm F1.8 STM”, https://global.canon/en/c-museum/product/rf498.html; napis na obiektywie Ani (`0155ae68…`, `89e221d3…`) |
| Miga 30" — za ciemno; miga 1/4000 — za jasno | instrukcja PL/EN, s. 101 |
| Poruszenie: mocno trzymać aparat, spust spokojnie | instrukcja PL/EN, s. 54 |
| Pokrętło przy LOCK w Av zmienia jasność (korektę) | instrukcja PL/EN, s. 57, 128 |

Szczegóły: `docs/L1-07_ZRODLA_INSTRUKCJA.md`.

## Kontekst dla nauczyciela AI
Cel ćwiczenia: świadome rozmycie tła liczbą przy F przy stałym kadrze i stałym punkcie ostrości. AI sprawdza najpierw, czy na zdjęciu z F1.8 tło jest bardziej rozmyte niż z F5.6, a przedmiot ostry na obu; potem, czy Ania wskazuje różnicę w tle i wie, którą liczbę ustawiła. AI nie proponuje jeszcze zmiany czasu, ISO, innych trybów, ogniskowej ani oceny kompozycji.

## Pomoc warunkowa
- Wpis o pierścieniu na obiektywie (zmiana liczby przy F pierścieniem przy spuście do połowy) — dopiero po sprawdzeniu na aparacie Ani (EN 58; `docs/L1-07_ZRODLA_INSTRUKCJA.md`, punkt g). Materiał: wycinek ze zdjęcia `24edb1ad…` lub `7d5062d5…` (przełącznik CONTROL/FOCUS). Do tego czasu bez wpisu i bez materiału.

## Do sprawdzenia na aparacie Ani
Lista w `docs/L1-07_ZRODLA_INSTRUKCJA.md`, sekcja „Do sprawdzenia na aparacie Ani”; zwłaszcza napis „F1.8” na ekranie i ustawienia ostrości po przejściu P → Av.
