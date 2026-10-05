# L1-06 — karta wizualno-produkcyjna

Aktualne statusy materiałów: docs/16_ASSET_MANIFEST.md (D-074). Statusy poniżej są historyczne.

Stan: 05.10.2026. Dokument produkcyjny; zgodnie z D-048 jego treść nie jest widoczna w kursie.

## Zasady dla materiałów L1-06
- Pochodzenie każdego materiału według D-057: WŁASNE, RENDER, WOLNA LICENCJA albo CANON — DO PODMIANY.
- Rendery powstają w scenie Blender z L1-03/L1-04 (D-051): ten sam kubek, ten sam wirtualny aparat; między wersjami jednego materiału zmienia się dokładnie jedna rzecz. Skrypty w repozytorium, pełne rendery lokalnie, do `review/` tylko lekkie kopie (D-053).
- Najpierw jedno ujęcie próbne (V01 „z boku”) do oceny właściciela, potem pozostałe (D-075).
- Rysunki z instrukcji Canon (D-056): plik kończy się na `-canon`, przechowywany lokalnie, nigdy w publicznym repozytorium ani w publicznej wersji aplikacji. W wersji bez pliku aplikacja pokazuje w tym miejscu jawne miejsce na brakujący materiał.
- Oznaczenia elementów statyczne i wyraźne, w stylu zatwierdzonym w L1-01 i L1-02 (D-038). Bez animacji.
- Materiał bez źródła nie ma zamiennika; w aplikacji stoi jawne miejsce na brakujący materiał.

## Materiały

| ID | Krok | Co dokładnie pokazuje | Źródło | Pochodzenie | Plik docelowy | Status |
|---|---|---|---|---|---|---|
| L1-06-V01 | S01–S04 | Ten sam kubek w trzech wersjach: światło z okna z przodu, z boku, od tyłu. Aparat i kubek stałe; zmienia się tylko położenie okna. W wersji „od tyłu” okno jest za kubkiem, w kadrze. | render, scena Blender z L1-03/L1-04 z dodanym źródłem światła w kształcie okna; najpierw ujęcie próbne „z boku” (D-075) | RENDER | `assets/lessons/l1-06/l1-06-v01-przod.jpg`, `l1-06-v01-bok.jpg`, `l1-06-v01-tyl.jpg` | `TO_ANIMATE` |
| L1-06-V02 | S02–S04 | Schemat z góry: okno, przedmiot, trzy miejsca Ani (1 z przodu, 2 z boku, 3 od tyłu); w każdym kroku podświetlone inne miejsce | grafika SVG jak L1-03-V05 część B | WŁASNE | `assets/lessons/l1-06/l1-06-v02-schemat-1.svg`, `-2.svg`, `-3.svg` | `TO_DESIGN` |
| L1-06-V03 | S04 | Para: światło od tyłu przy 0 i przy plus 1 | render, ta sama scena, opcja przesunięcia ekspozycji | RENDER | `assets/lessons/l1-06/l1-06-v03-tyl-zero.jpg`, `l1-06-v03-tyl-plus1.jpg` | `TO_ANIMATE` |
| L1-06-V04 | przed ćwiczeniem | Karta: „z przodu → z boku → od tyłu → porównaj → znacznik na 0” | bez pliku | — | komponent aplikacji | komponent UI |

**Ujęcie próbne V01 „z boku” (05.10.2026):** skrypt `production/l1-06/build_l1_06_v01.py` (korzysta ze sceny `production/l1-03/scene/build_v04a_scene.py` bez jej zmiany). Kubek 1, kolory z kalibracji `shot-1.json`, aparat jak V04A pozycja 1 (50 mm, f/8). Zamiast światła sceny L1-03 jedno okno — parametry są wyborem produkcyjnym, nie pomiarem: prostokąt 1,0 × 1,2 m, pionowy, parapet 0,85 m nad podłogą, 1,0 m na lewo od kubka, prostopadle do osi aparatu; 160 W, barwa jak okno w scenie L1-03; słabe światło otoczenia bez zmian. Ekspozycja: strona kubka zwrócona do okna ma jasność szkliwa z palety. Podgląd: `review/l1-06/l1-06-v01-bok.jpg`.

Materiały z wcześniejszych lekcji użyte w L1-06 (bez nowych plików):
- S04, podpunkt 3, i pomoc „Przy świetle od tyłu…”: pokrętło przy LOCK — `assets/lessons/l1-05/l1-05-v02-pokretlo-przy-lock.jpg` (L1-05-V02).
- S04, podpunkt 3: skala jasności, znacznik w stronę plusa — `assets/lessons/l1-05/l1-05-v04-skala-jasnosci-canon.png` (L1-05-V04; rysunek Canon, tylko lokalnie).
- Ćwiczenie, „Porównaj”: przycisk odtwarzania — `assets/lessons/l1-02/l1-02-v03-playback-button.jpg` (L1-02-V03).

## Tabela źródeł (D-048)

| Twierdzenie w lekcji | Źródło |
|---|---|
| Trzy kierunki światła; z przodu: równe oświetlenie, kolory i szczegóły, mało cieni, płasko; z boku: jedna strona jasna, druga w cieniu, widać kształt; od tyłu: przedmiot ciemny, sylwetka; dodatnia korekta pomaga przy zbyt jasnym tle | Canon Singapore SNAPSHOT, „[Lesson 8] How Light Affects Photography”, https://snapshot.asia.canon/en/article/lesson-8-how-light-affects-photography |
| Cień po stronie przeciwnej do światła; od tyłu = światło naprzeciw aparatu; korekta jasności przy świetle od tyłu | Canon Singapore SNAPSHOT, „[Lesson 14] Knowing Your Light Rays”, https://snapshot.asia.canon/en/article/lesson-14-knowing-your-light-rays (bez części o portretach) |
| Przy oknie: z przodu = plecami do okna, uwaga na własny cień (przesunąć się w bok lub kucnąć); z boku = równolegle do okna, blisko okna mocny kontrast, dalej równiej; od tyłu = fotografowanie w stronę okna | Nikon School UK, „Shooting with Window Light”, https://nikonschool.co.uk/hints-and-tips/shooting-with-window-light |
| Nie kierować aparatu na słońce: uszkodzenie aparatu i wzroku | instrukcja PL, s. 232, 49 |
| Korekta pokrętłem przy LOCK w P; zostaje po wyłączeniu | instrukcja PL, s. 57, 128 (L1-05) |

## Do sprawdzenia na aparacie Ani (po powrocie właściciela, D-056)
Lista w `docs/L1-06_ZRODLA_INSTRUKCJA.md`, sekcja „Do sprawdzenia na aparacie Ani”; zwłaszcza punkt 8 (ile plusa przy świetle od tyłu — tekst lekcji podaje 1, pomoc 2).
