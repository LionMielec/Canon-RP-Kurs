# L1-04 — karta wizualno-produkcyjna

Aktualne statusy materiałów: docs/16_ASSET_MANIFEST.md (D-074). Statusy poniżej są historyczne.

Stan: 02.10.2026. Dokument produkcyjny; zgodnie z D-048 jego treść nie jest widoczna w kursie.

## Zasady dla materiałów L1-04
- Pochodzenie każdego materiału według D-057: WŁASNE, RENDER, WOLNA LICENCJA albo CANON — DO PODMIANY.
- Rysunki z instrukcji Canon (D-056): plik kończy się na `-canon`, przechowywany lokalnie, nigdy w publicznym repozytorium ani w publicznej wersji aplikacji.
- Wycinek z rysunku Canon obejmuje tylko wskazany rysunek, bez numerów stron, podpisów i tekstu instrukcji.
- Oznaczenia elementów statyczne i wyraźne, w stylu zatwierdzonym w L1-01 i L1-02 (D-038). Bez animacji.

## Materiały

| ID | Krok | Co dokładnie pokazuje | Źródło | Pochodzenie | Plik docelowy | Status |
|---|---|---|---|---|---|---|
| L1-04-V01 | S01 | Para z tej samej sceny 3D: kubek ok. 0,5 m i książka z napisem „Notatki” ok. 1,0 m; A — ostry kubek, B — ostra książka; f/2.8, aparat nieruchomy, zmienia się tylko odległość ostrości | render: ujęcia `l1-04-blizej`, `l1-04-dalej` | RENDER | `assets/lessons/l1-04/l1-04-v01-blizej.jpg`, `l1-04-v01-dalej.jpg` | podgląd w produkcji |
| L1-04-V02 | S03 | Wycinek góry aparatu Ani: pokrętło trybów, statyczne oznaczenie litery P | `fbe2fd62-e8ab-465b-b340-b6d0b4458622.jpg` | WŁASNE | `assets/lessons/l1-04/l1-04-v02-pokretlo-p.jpg` | do przygotowania |
| L1-04-V03 | S04 | Wycinek tyłu aparatu Ani: tylny wybierak, statyczne oznaczenie przycisku Q/SET | `57652b89-ae48-4cd1-b998-e883aee8aa1f.jpg` | WŁASNE | `assets/lessons/l1-04/l1-04-v03-przycisk-q.jpg` | do przygotowania |
| L1-04-V04 | S04 | Ekran szybkich ustawień z zaznaczonym napisem Metoda AF i rzędem ikon u dołu (środkowy rysunek strony) | instrukcja PL, s. 65 | CANON — DO PODMIANY | `assets/lessons/l1-04/l1-04-v04-ekran-q-canon.png` | do wycięcia |
| L1-04-V05 | S04 | Ekran z podpisem „1-punktowy AF”, punktem ostrości na środku i zaznaczoną ikoną z jednym małym kwadratem | instrukcja PL, s. 188 | CANON — DO PODMIANY | `assets/lessons/l1-04/l1-04-v05-1-punktowy-af-canon.png` | do wycięcia |
| L1-04-V06 | S05 | Tył aparatu Ani: trzy statyczne oznaczenia — przycisk lupy (prawy górny róg), Q/SET i przycisk kosza; wszystkie trzy są w kadrze zdjęcia `57652b89…` | `57652b89-ae48-4cd1-b998-e883aee8aa1f.jpg` | WŁASNE | `assets/lessons/l1-04/l1-04-v06-przycisk-punktu-af.jpg` | do przygotowania |
| L1-04-V07 | S05 | Ekran po naciśnięciu przycisku lupy: punkt ostrości na środku ekranu, u dołu ikony kosza i SET (krok 2). Na s. 192–195 nie ma rysunku z białym punktem ostrości przesuniętym w bok | instrukcja PL, s. 193 | CANON — DO PODMIANY | `assets/lessons/l1-04/l1-04-v07-przesuwanie-punktu-canon.png` | do wycięcia |
| L1-04-V08 | S06 | Ekran w trybie P z zielonym punktem ostrości na przedmiocie po ustawieniu ostrości (krok 3, sam ekran, bez rysunku spustu) | instrukcja PL, s. 194 | CANON — DO PODMIANY | `assets/lessons/l1-04/l1-04-v08-zielony-punkt-canon.png` | do wycięcia |
| L1-04-V09 | Pomoc | Ekran z palcem na ikonie migawki dotykowej w lewym dolnym rogu (lewy rysunek) | instrukcja PL, s. 163 | CANON — DO PODMIANY | `assets/lessons/l1-04/l1-04-v09-migawka-dotykowa-canon.png` | do wycięcia |
| L1-04-V10 | ćwiczenie | Karta przed ćwiczeniem: „P → jeden punkt ostrości → punkt ostrości na przedmiot → spust do połowy → zielony punkt ostrości → zdjęcie → powiększ” | bez osobnego pliku | — | komponent aplikacji | komponent UI |
| L1-04-V11 | S04, podpunkt 4 | Napis ONE SHOT na ekranie szybkich ustawień, ze statycznym oznaczeniem (lewa kolumna, druga ikona od góry) | instrukcja PL, s. 65 — ten sam rysunek co V04 | CANON — DO PODMIANY | `assets/lessons/l1-04/l1-04-v04-ekran-q-canon.png` (plik wspólny z V04) | `APPROVAL_PENDING` |
| L1-04-V12 | Pomoc, menu 1 i 6 | Wycinek tyłu aparatu Ani: przycisk MENU po lewej stronie wizjera, statyczne oznaczenie | `57652b89-ae48-4cd1-b998-e883aee8aa1f.jpg` | WŁASNE | `assets/lessons/l1-04/l1-04-v12-przycisk-menu.jpg` | `APPROVAL_PENDING` |
| L1-04-V13 | Pomoc, menu 2 | Ekran menu aparatu Ani: czerwona część z ikoną aparatu, strony 1–5, statyczne oznaczenie czerwonej karty | `10a55454-d36b-4e92-9568-1b4dd40ffa5e.jpg` | WŁASNE | `assets/lessons/l1-04/l1-04-v13-menu-czerwona-czesc.jpg` | `APPROVAL_PENDING` + `TO_VERIFY` (układ stron w trybie P) |
| L1-04-V14 | Pomoc, menu 3 | Ekran menu aparatu Ani: strona 3 z zaznaczonym napisem Metoda AF, statyczne oznaczenie napisu | `336149b5-debf-4a74-b168-12d210f1b591.jpg` | WŁASNE | `assets/lessons/l1-04/l1-04-v14-menu-metoda-af.jpg` | `APPROVAL_PENDING` + `TO_VERIFY` (układ stron w trybie P) |
| L1-04-V15 | Pomoc, menu 4 | Ekran wyboru metody: podpis „1-punktowy AF”, rząd ikon u dołu, statyczne oznaczenie ikony z jednym małym kwadratem. Na s. 189–190 nie ma osobnego rysunku wyboru metody w menu | instrukcja PL, s. 188 — ten sam rysunek co V05 | CANON — DO PODMIANY | `assets/lessons/l1-04/l1-04-v05-1-punktowy-af-canon.png` (plik wspólny z V05) | `APPROVAL_PENDING` + `TO_VERIFY` (czy menu otwiera ten ekran) |
| L1-04-V16 | Pomoc, menu 5 | Dwa ekrany menu: strona z zaznaczonym napisem Działanie AF (oznaczenie napisu) oraz ekran wyboru z zaznaczonym ONE SHOT i podpisem One-Shot AF (oznaczenie) | instrukcja PL, s. 185 (krok 1 i krok 2) | CANON — DO PODMIANY | `assets/lessons/l1-04/l1-04-v16-dzialanie-af-menu-canon.png`, `l1-04-v16-one-shot-af-canon.png` | `APPROVAL_PENDING` |
| L1-04-V17 | Pomoc, „Widzę dużą ramkę ostrości…” | Ekran fotografowania w trybie P z ramką ostrości na twarzy, statyczne oznaczenie ramki ostrości | instrukcja PL, s. 191 (krok 1) | CANON — DO PODMIANY | `assets/lessons/l1-04/l1-04-v17-ramka-na-twarzy-canon.png` | `APPROVAL_PENDING` |
| L1-04-V18 | Pomoc, „Punkt ostrości robi się pomarańczowy” | Ekran z pomarańczowym punktem ostrości | BRAK — w instrukcji PL nie ma rysunku z pomarańczowym punktem ostrości (sprawdzone s. 70, 163, 185, 191–197, 565: tylko tekst); w pakiecie zdjęć Ani też go nie ma | — | — | brak źródła — do decyzji właściciela; w aplikacji nie wstawiono zamiennika |

## Tabela źródeł (D-048)

| Twierdzenie w lekcji | Źródło |
|---|---|
| W A+ aparat sam wybiera miejsce ostrości (twarz albo cały obszar AF); metody AF nie da się zmienić | instrukcja PL, s. 97, 188, 190 |
| Pokrętło na P; w P aparat sam ustawia czas i przysłonę, metodę AF można zmienić | instrukcja PL, s. 96–97 |
| Q/SET otwiera szybkie ustawienia; wybór w górę/w dół, zmiana w lewo/w prawo, zatwierdzenie Q/SET; nie działa w A+ | instrukcja PL, s. 65 |
| Metoda AF i ONE SHOT widoczne na ekranie szybkich ustawień | rysunek, instrukcja PL, s. 65 — do sprawdzenia na aparacie |
| [Działanie AF] → [One-Shot AF]; [Metoda AF] → [1-punktowy AF] przez menu | instrukcja PL, s. 185–186, 188, 190 |
| Przycisk lupy w prawym górnym rogu; przesuwanie dotykiem, pokrętłami lub przyciskami; przycisk kosza wraca na środek; punkt ostrości może nie dojść do brzegu ekranu | instrukcja PL, s. 33, 193 |
| Zielony punkt ostrości i sygnał = ostrość; pomarańczowy = brak ostrości | instrukcja PL, s. 194 |
| Migawka dotykowa: ikona w lewym dolnym rogu; wyłączona — dotyk tylko ustawia ostrość | instrukcja PL, s. 163 |
| U Ani migawka dotykowa jest wyłączona | zdjęcie aparatu Ani `f1097406…` |
| Czerwona ramka ostrości przy oglądaniu zdjęcia; u Ani [Wyśw. punktu AF] = [Włącz] | instrukcja PL, s. 352; zdjęcie aparatu Ani `e81a5d55…` |
| Ostrość na jedną odległość; ostre to, co w pewnym zakresie przed i za miejscem ostrości | Canon Australia — What is Depth of Field? |
| Jeden punkt ostrości pozwala wskazać miejsce ostrości; przy wyborze automatycznym wybiera aparat | Canon Europe — All about Autofocus |

## Do sprawdzenia na aparacie Ani (po powrocie właściciela, D-056)
Lista w `docs/L1-04_ZRODLA_INSTRUKCJA.md`, sekcja „Do sprawdzenia na aparacie Ani”, oraz porównanie rysunków V04, V05, V07–V09, V11, V15–V17 z ekranami aparatu. Zdjęcia V13 i V14 pokazują menu z pięcioma stronami (najpewniej tryb A+); układ stron w trybie P do sprawdzenia.
