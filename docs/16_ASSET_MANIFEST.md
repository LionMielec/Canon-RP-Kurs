# Canon RP kurs — ASSET MANIFEST

Stan na: 2026-09-30

Ten plik jest rejestrem materiałów wizualnych przypisanych do konkretnych lekcji. Nie jest magazynem wszystkich zdjęć projektu. Do manifestu trafiają materiały dopiero wtedy, gdy mają określone zastosowanie dydaktyczne.

## Zasady
- Każdy asset ma identyfikator lekcji i materiału, np. `L1-01-V02`.
- Każdy asset jest przypisany do konkretnego kroku lekcji.
- Źródło z Library jest etapem roboczym; przed implementacją finalny plik trafia do repozytorium pod czytelną nazwą.
- Codex używa docelowego pliku zgodnie z przypisaniem; nie wybiera samodzielnie zamienników.
- Statusy: `SOURCE_SELECTED`, `TO_CAPTURE`, `TO_DESIGN`, `TO_ANIMATE`, `TO_PREPARE`, `APPROVAL_PENDING`, `APPROVED`.
- Każdy asset ma pochodzenie: WŁASNE, RENDER, WOLNA LICENCJA albo CANON — DO PODMIANY (D-057). Pliki z instrukcji Canon mają w nazwie końcówkę `-canon`.

## L1-01 — Robię swoje pierwsze zdjęcie

| ID | Zastosowanie | Typ | Źródło / brak | Pochodzenie | Docelowa ścieżka | Status |
|---|---|---|---|---|---|---|
| L1-01-V01 | Włącz aparat | zdjęcie/crop | wyłącznie `fbe2fd62-e8ab-465b-b340-b6d0b4458622.jpg` / `libfile_167abe23e1488191ba89b2d851b2155c` | WŁASNE | `assets/lessons/l1-01/l1-01-v01-power-switch.jpg` | `PREPARED` + `APPROVAL_PENDING` |
| L1-01-V02 | Ustaw A+ | zdjęcie/crop | wyłącznie `fbe2fd62-e8ab-465b-b340-b6d0b4458622.jpg` / `libfile_167abe23e1488191ba89b2d851b2155c` | WŁASNE | `assets/lessons/l1-01/l1-01-v02-mode-a-plus.jpg` | `PREPARED` + `APPROVAL_PENDING` |
| L1-01-V03 | Prawidłowe trzymanie | zdjęcie instruktażowe | brak — nowe ujęcie osoby z aparatem | CANON — DO PODMIANY (instrukcja PL, s. 53: postać trzymająca aparat przed sobą i patrząca na ekran; plik `l1-01-v03-camera-hold-canon.png`) | `assets/lessons/l1-01/l1-01-v03-camera-hold.jpg` | `APPROVAL_PENDING` |
| L1-01-V04 | Pół / pełne naciśnięcie spustu | animacja | brak finalnego źródła ruchu | CANON — DO PODMIANY (instrukcja PL, s. 54: góra aparatu ze strzałką na spust; plik `l1-01-v04-shutter-canon.png`) | `assets/lessons/l1-01/l1-01-v04-shutter-half-full.mp4` | `APPROVAL_PENDING` |
| L1-01-V05 | Potwierdzenie AF | 2 ekrany / sekwencja | brak ekranu fotografowania z AF | CANON — DO PODMIANY (instrukcja PL, s. 191: sam obszar z ramką na twarzy, biała przed i zielona po; pliki `l1-01-v05-af-before-canon.png`, `l1-01-v05-af-confirmed-canon.png`) | `assets/lessons/l1-01/l1-01-v05-af-before.jpg`, `l1-01-v05-af-confirmed.jpg` | `APPROVAL_PENDING` |
| L1-01-V06 | Łatwy/trudny cel AF | plansza | brak scen referencyjnych | RENDER (cztery ujęcia sceny 3D: `l1-01-v06-1-napis`, `-2-gladka-sciana`, `-3-ciemno`, `-4-za-blisko`) | `assets/lessons/l1-01/l1-01-v06-af-easy-hard.jpg` | `APPROVAL_PENDING` |

## L1-02 — Sprawdzam, czy zdjęcie jest ostre

| ID | Zastosowanie | Typ | Źródło / brak | Pochodzenie | Docelowa ścieżka | Status |
|---|---|---|---|---|---|---|
| L1-02-V01 | Wzorzec: ważny element ostry / ostrość przesunięta | zestaw dydaktyczny | render: ujęcia `l1-02-v01-ostrosc-dobra`, `l1-02-v01-ostrosc-przesunieta` (kadr V04A pozycja 1, f/2.8, zmienia się tylko odległość ostrości); zastąpiono rysunki/zdjęcie z Wikimedia po przeglądzie 01.10.2026 | RENDER | `assets/lessons/l1-02/l1-02-v01-focus-reference.*` | `APPROVAL_PENDING` |
| L1-02-V02 | Całe zdjęcie → powiększony detal | para edukacyjna | `l1-02-v02-cale-zdjecie.jpg` (render V04A pozycja 1 v3 zmniejszony do 1200×800) i `l1-02-v02-szczegol.jpg` (wycinek napisu z pełnej rozdzielczości); zastąpiono rysunki/zdjęcie z Wikimedia po przeglądzie 01.10.2026 | RENDER | `assets/lessons/l1-02/l1-02-v02-full-vs-detail.*` | `APPROVAL_PENDING` |
| L1-02-V03 | Przycisk odtwarzania + tylny wybierak | zdjęcie/crop EOS RP Ani z 2 oznaczeniami | `57652b89-ae48-4cd1-b998-e883aee8aa1f.jpg` / `libfile_eb4721328c288191bb5aa19d2aa13f7e` | WŁASNE | `assets/lessons/l1-02/l1-02-v03-playback-selector.jpg` | `SOURCE_SELECTED` + `TO_PREPARE` |
| L1-02-V04 | Lupa + główne pokrętło + tylny wybierak | grafika 3-etapowa | tył: `57652b89-ae48-4cd1-b998-e883aee8aa1f.jpg`; góra: `fbe2fd62-e8ab-465b-b340-b6d0b4458622.jpg` | WŁASNE | `assets/lessons/l1-02/l1-02-v04-magnify-controls.jpg` | `SOURCE_SELECTED` + `TO_DESIGN` |
| L1-02-V05 | Karta przypominająca wzorzec przy ćwiczeniu | karta UI | wycinki z V01/V02 | do ustalenia | `assets/lessons/l1-02/l1-02-v05-sharpness-reference-card.*` | zależny od V01/V02 |

## L1-03 — Układam zdjęcie bez zmiany ustawień

| ID | Zastosowanie | Typ | Źródło / brak | Pochodzenie | Docelowa ścieżka | Status |
|---|---|---|---|---|---|---|
| L1-03-V01 | Ten sam przedmiot: rozpraszające vs prostsze tło po zmianie pozycji | para zdjęć | render 3D sceny w Blenderze 4.5 LTS (D-051) | RENDER | `assets/lessons/l1-03/l1-03-v01-background-position.*` | `APPROVAL_PENDING` |
| L1-03-V02 | Kontrola czterech brzegów kadru | para edukacyjna + statyczne markery | render 3D sceny w Blenderze 4.5 LTS (D-051) | RENDER | `assets/lessons/l1-03/l1-03-v02-frame-edges.*` | `APPROVAL_PENDING` |
| L1-03-V03 | Poziomo / pionowo z tego samego miejsca | para zdjęć | render 3D sceny w Blenderze 4.5 LTS (D-051) | RENDER | `assets/lessons/l1-03/l1-03-v03-horizontal-vertical.*` | `TO_DESIGN` |
| L1-03-V04A | Jeden krok w bok zmienia tło | para zdjęć | render 3D sceny w Blenderze 4.5 LTS (D-051) | RENDER | `assets/lessons/l1-03/l1-03-v04a-step-sideways.*` | `TO_DESIGN` |
| L1-03-V04B | Zmiana wysokości aparatu | 3 zdjęcia | render 3D sceny w Blenderze 4.5 LTS (D-051) | RENDER | `assets/lessons/l1-03/l1-03-v04b-camera-height.*` | `TO_DESIGN` |
| L1-03-V05 | RF 50 mm — stała ogniskowa, brak zoomu | zdjęcie obiektywu Ani + diagram | rzeczywiste zdjęcie RF 50 mm Ani + oficjalne dane Canon | WŁASNE (część A: wycinek zdjęcia `40b8cbb9…`; część B: własny schemat SVG) | `assets/lessons/l1-03/l1-03-v05-fixed-50mm.*` | `APPROVAL_PENDING` |
| L1-03-V06 | Karta „poziomo/pionowo → brzegi/tło → miejsce → zdjęcie” | komponent UI | bez osobnego assetu | do ustalenia | komponent aplikacji | `UI_COMPONENT` |

## L1-04 — Wybieram, co ma być ostre

| ID | Zastosowanie | Typ | Źródło / brak | Pochodzenie | Docelowa ścieżka | Status |
|---|---|---|---|---|---|---|
| L1-04-V01 | Para „ostry bliższy / ostry dalszy”: kubek ok. 0,5 m i książka z napisem „Notatki” ok. 1,0 m; zmienia się tylko odległość ostrości (S01) | para renderów | render: ujęcia `l1-04-blizej`, `l1-04-dalej` | RENDER | `assets/lessons/l1-04/l1-04-v01-blizej.jpg`, `l1-04-v01-dalej.jpg` | `APPROVAL_PENDING` |
| L1-04-V02 | Pokrętło trybów ze statycznym oznaczeniem litery P (S03) | zdjęcie/crop | `fbe2fd62-e8ab-465b-b340-b6d0b4458622.jpg` | WŁASNE | `assets/lessons/l1-04/l1-04-v02-pokretlo-p.jpg` | `APPROVAL_PENDING` |
| L1-04-V03 | Tylny wybierak ze statycznym oznaczeniem przycisku Q/SET (S04) | zdjęcie/crop | `57652b89-ae48-4cd1-b998-e883aee8aa1f.jpg` | WŁASNE | `assets/lessons/l1-04/l1-04-v03-przycisk-q.jpg` | `APPROVAL_PENDING` |
| L1-04-V04 | Ekran szybkich ustawień z zaznaczonym napisem Metoda AF i rzędem ikon u dołu (S04) | rysunek ekranu | instrukcja PL, s. 65 | CANON — DO PODMIANY | `assets/lessons/l1-04/l1-04-v04-ekran-q-canon.png` | `APPROVAL_PENDING` |
| L1-04-V05 | Ekran z podpisem „1-punktowy AF”, punktem na środku i zaznaczoną ikoną jednego punktu (S04) | rysunek ekranu | instrukcja PL, s. 188 | CANON — DO PODMIANY | `assets/lessons/l1-04/l1-04-v05-1-punktowy-af-canon.png` | `APPROVAL_PENDING` |
| L1-04-V06 | Tył aparatu: statyczne oznaczenie przycisku punktu AF, Q/SET i przycisku kosza (S05) | zdjęcie/crop albo rysunek | `57652b89…` albo instrukcja PL, s. 33 | WŁASNE (oba przyciski są w kadrze zdjęcia `57652b89…`) | `assets/lessons/l1-04/l1-04-v06-przycisk-punktu-af.jpg` (albo `…-canon.png`) | `APPROVAL_PENDING` |
| L1-04-V07 | Ekran po naciśnięciu przycisku punktu AF: punkt na środku ekranu, u dołu ikony kosza i SET (S05) | rysunek ekranu | instrukcja PL, s. 193 | CANON — DO PODMIANY | `assets/lessons/l1-04/l1-04-v07-przesuwanie-punktu-canon.png` | `APPROVAL_PENDING` |
| L1-04-V08 | Ekran w trybie P z zielonym punktem AF na obiekcie po ustawieniu ostrości (S06) | rysunek ekranu | instrukcja PL, s. 194 | CANON — DO PODMIANY | `assets/lessons/l1-04/l1-04-v08-zielony-punkt-canon.png` | `APPROVAL_PENDING` |
| L1-04-V09 | Ekran z palcem na ikonie migawki dotykowej w lewym dolnym rogu (Pomoc) | rysunek ekranu | instrukcja PL, s. 163 | CANON — DO PODMIANY | `assets/lessons/l1-04/l1-04-v09-migawka-dotykowa-canon.png` | `APPROVAL_PENDING` |
| L1-04-V10 | Karta przed ćwiczeniem: „P → jeden punkt → punkt na przedmiot → spust do połowy → zielony punkt → zdjęcie → powiększ” | komponent UI | bez osobnego pliku | — | komponent aplikacji | komponent UI |
| L1-04-V11 | Napis ONE SHOT na ekranie szybkich ustawień, ze statycznym oznaczeniem (lewa kolumna, druga ikona od góry) (S04, podpunkt 4) | rysunek ekranu | instrukcja PL, s. 65 — ten sam rysunek co V04 | CANON — DO PODMIANY | `assets/lessons/l1-04/l1-04-v04-ekran-q-canon.png` (plik wspólny z V04) | `APPROVAL_PENDING` |
| L1-04-V12 | Wycinek tyłu aparatu Ani: przycisk MENU po lewej stronie wizjera, statyczne oznaczenie (Pomoc, menu 1 i 6) | zdjęcie/crop | `57652b89-ae48-4cd1-b998-e883aee8aa1f.jpg` | WŁASNE | `assets/lessons/l1-04/l1-04-v12-przycisk-menu.jpg` | `APPROVAL_PENDING` |
| L1-04-V13 | Ekran menu aparatu Ani: czerwona część z ikoną aparatu, strony 1–5, statyczne oznaczenie czerwonej karty (Pomoc, menu 2) | zdjęcie ekranu | `10a55454-d36b-4e92-9568-1b4dd40ffa5e.jpg` | WŁASNE | `assets/lessons/l1-04/l1-04-v13-menu-czerwona-czesc.jpg` | `APPROVAL_PENDING` + `TO_VERIFY` (układ stron w trybie P) |
| L1-04-V14 | Ekran menu aparatu Ani: strona 3 z zaznaczonym napisem Metoda AF, statyczne oznaczenie napisu (Pomoc, menu 3) | zdjęcie ekranu | `336149b5-debf-4a74-b168-12d210f1b591.jpg` | WŁASNE | `assets/lessons/l1-04/l1-04-v14-menu-metoda-af.jpg` | `APPROVAL_PENDING` + `TO_VERIFY` (układ stron w trybie P) |
| L1-04-V15 | Ekran wyboru metody: podpis „1-punktowy AF”, rząd ikon u dołu, statyczne oznaczenie ikony z jednym kwadratem. Na s. 189–190 nie ma osobnego rysunku wyboru metody w menu (Pomoc, menu 4) | rysunek ekranu | instrukcja PL, s. 188 — ten sam rysunek co V05 | CANON — DO PODMIANY | `assets/lessons/l1-04/l1-04-v05-1-punktowy-af-canon.png` (plik wspólny z V05) | `APPROVAL_PENDING` + `TO_VERIFY` (czy menu otwiera ten ekran) |
| L1-04-V16 | Dwa ekrany menu: strona z zaznaczonym napisem Działanie AF (oznaczenie napisu) oraz ekran wyboru z zaznaczonym ONE SHOT i podpisem One-Shot AF (oznaczenie) (Pomoc, menu 5) | 2 rysunki ekranu | instrukcja PL, s. 185 (krok 1 i krok 2) | CANON — DO PODMIANY | `assets/lessons/l1-04/l1-04-v16-dzialanie-af-menu-canon.png`, `l1-04-v16-one-shot-af-canon.png` | `APPROVAL_PENDING` |
| L1-04-V17 | Ekran fotografowania w trybie P z ramką na twarzy, statyczne oznaczenie ramki (Pomoc, „Widzę dużą ramkę…”) | rysunek ekranu | instrukcja PL, s. 191 (krok 1) | CANON — DO PODMIANY | `assets/lessons/l1-04/l1-04-v17-ramka-na-twarzy-canon.png` | `APPROVAL_PENDING` |
| L1-04-V18 | Ekran z pomarańczowym punktem (Pomoc, „Kwadrat robi się pomarańczowy”) | — | BRAK — w instrukcji PL nie ma rysunku z pomarańczowym punktem AF (sprawdzone s. 70, 163, 185, 191–197, 565: tylko tekst); w pakiecie zdjęć Ani też go nie ma | — | — | brak źródła — do decyzji właściciela; w aplikacji nie wstawiono zamiennika |

## Następny wpis
Kolejne assety dopisywać przy opracowywaniu następnej lekcji. Nie tworzyć osobnego, równoległego rejestru.