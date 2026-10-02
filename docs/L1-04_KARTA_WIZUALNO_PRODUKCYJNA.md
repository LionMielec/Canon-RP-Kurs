# L1-04 — karta wizualno-produkcyjna

Stan: 01.10.2026. Dokument produkcyjny; zgodnie z D-048 jego treść nie jest widoczna w kursie.

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
| L1-04-V04 | S04 | Ekran szybkich nastaw z zaznaczoną pozycją [Metoda AF] i rzędem ikon metod u dołu (środkowy rysunek strony) | instrukcja PL, s. 65 | CANON — DO PODMIANY | `assets/lessons/l1-04/l1-04-v04-ekran-q-canon.png` | do wycięcia |
| L1-04-V05 | S04 | Ekran z podpisem „1-punktowy AF”, punktem na środku i zaznaczoną ikoną jednego punktu | instrukcja PL, s. 188 | CANON — DO PODMIANY | `assets/lessons/l1-04/l1-04-v05-1-punktowy-af-canon.png` | do wycięcia |
| L1-04-V06 | S05 | Tył aparatu: statyczne oznaczenie przycisku punktu AF (prawy górny róg) i przycisku kosza. Najpierw sprawdzić, czy oba przyciski są w kadrze zdjęcia `57652b89`; jeśli tak — WŁASNE; jeśli nie — rysunek z instrukcji PL, s. 33 | `57652b89…` albo instrukcja PL, s. 33 | WŁASNE albo CANON — DO PODMIANY | `assets/lessons/l1-04/l1-04-v06-przycisk-punktu-af.jpg` (albo `…-canon.png`) | do przygotowania |
| L1-04-V07 | S05 | Ekran po naciśnięciu przycisku punktu AF: punkt przesunięty w bok, u dołu ikony kosza i SET (krok 2) | instrukcja PL, s. 193 | CANON — DO PODMIANY | `assets/lessons/l1-04/l1-04-v07-przesuwanie-punktu-canon.png` | do wycięcia |
| L1-04-V08 | S06 | Ekran w trybie P z zielonym punktem AF na obiekcie po ustawieniu ostrości (krok 3, sam ekran, bez rysunku spustu) | instrukcja PL, s. 194 | CANON — DO PODMIANY | `assets/lessons/l1-04/l1-04-v08-zielony-punkt-canon.png` | do wycięcia |
| L1-04-V09 | Pomoc | Ekran z palcem na ikonie migawki dotykowej w lewym dolnym rogu (lewy rysunek) | instrukcja PL, s. 163 | CANON — DO PODMIANY | `assets/lessons/l1-04/l1-04-v09-migawka-dotykowa-canon.png` | do wycięcia |
| L1-04-V10 | ćwiczenie | Karta przed ćwiczeniem: „P → jeden punkt → punkt na przedmiot → spust do połowy → zielony punkt → zdjęcie → powiększ” | bez osobnego pliku | — | komponent aplikacji | komponent UI |

## Tabela źródeł (D-048)

| Twierdzenie w lekcji | Źródło |
|---|---|
| W A+ aparat sam wybiera miejsce ostrości (twarz albo cały obszar AF); metody AF nie da się zmienić | instrukcja PL, s. 97, 188, 190 |
| Pokrętło na P; w P aparat sam ustawia czas i przysłonę, metodę AF można zmienić | instrukcja PL, s. 96–97 |
| Q/SET otwiera szybkie ustawienia; wybór w górę/w dół, zmiana w lewo/w prawo, zatwierdzenie Q/SET; nie działa w A+ | instrukcja PL, s. 65 |
| [Metoda AF] i ONE SHOT widoczne na ekranie szybkich nastaw | rysunek, instrukcja PL, s. 65 — do sprawdzenia na aparacie |
| [Działanie AF] → [One-Shot AF]; [Metoda AF] → [1-punktowy AF] przez menu | instrukcja PL, s. 185–186, 188, 190 |
| Przycisk punktu AF w prawym górnym rogu; przesuwanie dotykiem, pokrętłami lub przyciskami; kosz wraca na środek; punkt może nie dojść do krawędzi | instrukcja PL, s. 33, 193 |
| Zielony punkt i sygnał = ostrość; pomarańczowy = brak ostrości | instrukcja PL, s. 194 |
| Migawka dotykowa: ikona w lewym dolnym rogu; wyłączona — dotyk tylko ustawia ostrość | instrukcja PL, s. 163 |
| U Ani migawka dotykowa jest wyłączona | zdjęcie aparatu Ani `f1097406…` |
| Czerwona ramka punktu AF przy oglądaniu zdjęcia; u Ani [Wyśw. punktu AF] = [Włącz] | instrukcja PL, s. 352; zdjęcie aparatu Ani `e81a5d55…` |
| Ostrość na jedną odległość; ostre to, co w pewnym zakresie przed i za miejscem ostrości | Canon Australia — What is Depth of Field? |
| Jeden punkt pozwala wskazać miejsce ostrości; przy wyborze automatycznym wybiera aparat | Canon Europe — All about Autofocus |

## Do sprawdzenia na aparacie Ani (po powrocie właściciela, D-056)
Lista w `docs/L1-04_ZRODLA_INSTRUKCJA.md`, sekcja „Do sprawdzenia na aparacie Ani”, oraz porównanie rysunków V04, V05, V07–V09 z ekranami aparatu.
