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

**Ujęcie próbne V01 „z boku” (05.10.2026):** skrypt `production/l1-06/build_l1_06_v01.py` (korzysta ze sceny `production/l1-03/scene/build_v04a_scene.py` bez jej zmiany). Kubek 1, kolory z kalibracji `shot-1.json`, aparat jak V04A pozycja 1 (50 mm, f/8). Zamiast światła sceny L1-03 jedno okno — parametry są wyborem produkcyjnym, nie pomiarem: prostokąt 1,0 × 1,2 m, pionowy, parapet 0,85 m nad podłogą, 1,0 m na lewo od kubka, prostopadle do osi aparatu; 160 W, barwa jak okno w scenie L1-03. Ekspozycja: strona kubka zwrócona do okna ma jasność szkliwa z palety. Pierwszy podgląd (ze słabym światłem otoczenia i lampą stojącą w kadrze): `review/l1-06/l1-06-v01-bok.jpg`.

**Poprawka ujęcia próbnego (05.10.2026)** po ocenie właściciela (efekt za słaby, słup lampy sugerował inne źródło światła). Lampa stojąca usunięta ze sceny L1-06; okno jest jedynym źródłem światła (światło otoczenia sceny wyłączone, ściany odbijają tylko światło okna). Próba 1 — tylko te zmiany: `review/l1-06/l1-06-v01-bok-proba1.jpg`. Próba 2 — dodatkowo ściana naprzeciw okna (prawa, poza kadrem) matowa, ciepła szarobeżowa `#8c8378` (wybór produkcyjny, nie pomiar; opcja skryptu `--dark-wall`): `review/l1-06/l1-06-v01-bok-proba2.jpg`. Różnica jasności stron kubka (łaty 60° w lewo i w prawo od osi aparatu, 3 cm nad dnem): pierwszy podgląd 2,91 EV, próba 1 2,90 EV, próba 2 3,32 EV. Kolory kubka i stołu, obróbka obrazu, okno, aparat i kubek bez zmian.

**Komplet ujęć V01 i para V03 (05.10.2026)** na ustawieniach próby 2, do oceny właściciela. Skrypt `production/l1-06/build_l1_06_v01.py` (opcje `--window przod|bok|tyl --dark-wall`, dla V03 `--plus1-out`). We wszystkich wersjach: kubek, aparat, stół, pokój bez lampy stojącej, bez światła otoczenia, ściana prawa matowa `#8c8378` (jak w próbie 2) i to samo okno — prostokąt świecący 1,0 × 1,2 m, 160 W, dolna krawędź szyby 0,85 m nad podłogą. Zmienia się tylko położenie okna:
- „z przodu” — okno za aparatem, w osi aparat–kubek, 1,0 m od osi kubka, poza kadrem;
- „z boku” — dokładnie próba 2: okno 1,0 m na lewo od kubka;
- „od tyłu” — okno w ścianie za kubkiem, w osi aparat–kubek, w kadrze; szyba 1,53 m od osi kubka (tam stoi ściana sceny).

Dobór jasności (wybór produkcyjny): „z przodu” i „z boku” — strona kubka zwrócona do okna ma jasność koloru szkliwa z palety (łata pomiaru „z przodu”: środek przodu kubka, „z boku”: 60° w lewo; obie 3 cm nad dnem). „Od tyłu” — średnia jasność całego kadru jak średnia szarość (średnia jasność liniowa 0,18). To przybliżenie pomiaru wielosegmentowego w trybie P, a nie odwzorowanie algorytmu Canon. V03 „przy 0” to ta sama klatka co V01 „od tyłu”; „przy plus 1” to ta sama scena wyrenderowana z ekspozycją o 1 EV wyższą. Krzywa obrazu, kontrast, zarządzanie kolorem i kolory materiałów bez zmian; bez obróbki po renderze.

Okno w ścianie za kubkiem (tylko „od tyłu”; wybór produkcyjny, nie pomiar): otwór w ścianie 1,16 × 1,36 m, dół otworu 0,77 m nad podłogą; mur 30 cm (ościeża dobudowane za 5-centymetrową ścianą sceny); biała rama `#eeece8` szerokości 8 cm i głębokości 7 cm, w połowie grubości muru; parapet wewnętrzny `#ece9e3` 1,26 × 0,165 × 0,025 m, wystaje 5 cm przed ścianę. Szyba to sam prostokąt świecący — jednolite, jasne światło dnia, bez krajobrazu, budynków, firanek i zasłon. Obraz wiszący na tej ścianie jest w tej wersji zdjęty, bo wypadałby w miejscu okna.

Pomiary (jasność liniowa, łaty 3 cm nad dnem kubka): „z przodu” — przód kubka 0,789, strony 60° w lewo i w prawo 0,373 i 0,369 (przód jaśniejszy od boków o 1,1 EV, lewa i prawa strona równe, 0,02 EV); „z boku” — strona od okna 0,790, strona w cieniu 0,079, różnica 3,32 EV (jak próba 2); „od tyłu przy 0” — przód kubka 0,030 (strony 0,044 i 0,045), szyba 1,000 (przepalona), średnia kadru 0,182; „od tyłu przy plus 1” — przód kubka 0,059 (strony 0,089 i 0,090), szyba 1,000, średnia kadru 0,282.

Pełne rendery lokalnie w `production/l1-06/renders/` (poza Git). Podglądy (dłuższy bok 2000 px): `review/l1-06/l1-06-v01-przod.jpg`, `l1-06-v01-bok.jpg`, `l1-06-v01-tyl.jpg`, `l1-06-v03-tyl-zero.jpg`, `l1-06-v03-tyl-plus1.jpg`; arkusz porównawczy `review/l1-06/porownanie-v01.jpg`.

**Schemat V02 (05.10.2026)**, do oceny właściciela: generator `production/l1-06/v02/build_v02_schemat.py`, pliki `production/l1-06/v02/l1-06-v02-schemat-1.svg`, `-2.svg`, `-3.svg` (kopia do `assets/lessons/l1-06/` w aplikacji przy wstawianiu lekcji). Widok z góry: ściana z oknem na górze, przedmiot (koło) blisko okna, trzy miejsca Ani (koło z numerem i znak aparatu skierowany na przedmiot): 1 „światło z przodu” między oknem a przedmiotem, 2 „światło z boku” na linii równoległej do ściany z oknem, 3 „światło od tyłu” za przedmiotem. W każdym pliku podświetlone jedno miejsce (fiolet i przerywana linia do przedmiotu), dwa pozostałe przygaszone. Paleta i krój jak L1-03-V05 część B. Arkusz w szerokości 430 px: `review/l1-06/v02-schemat-arkusz.png`.

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
