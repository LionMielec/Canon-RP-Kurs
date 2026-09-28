# Canon RP kurs — ASSET MANIFEST

Stan na: 2026-09-27

Ten plik jest rejestrem materiałów wizualnych przypisanych do konkretnych lekcji. Nie jest magazynem wszystkich zdjęć projektu. Do manifestu trafiają materiały dopiero wtedy, gdy mają określone zastosowanie dydaktyczne.

## Zasady
- Każdy asset ma identyfikator lekcji i materiału, np. `L1-01-V02`.
- Każdy asset jest przypisany do konkretnego kroku lekcji.
- Źródło z Library jest etapem roboczym; przed implementacją finalny plik trafia do repozytorium pod czytelną nazwą.
- Codex używa docelowego pliku zgodnie z przypisaniem; nie wybiera samodzielnie zamienników.
- Statusy: `SOURCE_SELECTED`, `TO_CAPTURE`, `TO_DESIGN`, `TO_ANIMATE`, `TO_PREPARE`, `APPROVAL_PENDING`, `APPROVED`.

## L1-01 — Robię swoje pierwsze zdjęcie

| ID | Zastosowanie | Typ | Źródło / brak | Docelowa ścieżka | Status |
|---|---|---|---|---|---|
| L1-01-V01 | Włącz aparat | zdjęcie/crop | wyłącznie `fbe2fd62-e8ab-465b-b340-b6d0b4458622.jpg` / `libfile_167abe23e1488191ba89b2d851b2155c` | `assets/lessons/l1-01/l1-01-v01-power-switch.jpg` | `PREPARED` + `APPROVAL_PENDING` |
| L1-01-V02 | Ustaw A+ | zdjęcie/crop | wyłącznie `fbe2fd62-e8ab-465b-b340-b6d0b4458622.jpg` / `libfile_167abe23e1488191ba89b2d851b2155c` | `assets/lessons/l1-01/l1-01-v02-mode-a-plus.jpg` | `PREPARED` + `APPROVAL_PENDING` |
| L1-01-V03 | Prawidłowe trzymanie | zdjęcie instruktażowe | brak — nowe ujęcie osoby z aparatem | `assets/lessons/l1-01/l1-01-v03-camera-hold.jpg` | `TO_CAPTURE` |
| L1-01-V04 | Pół / pełne naciśnięcie spustu | animacja | brak finalnego źródła ruchu | `assets/lessons/l1-01/l1-01-v04-shutter-half-full.mp4` | `TO_CAPTURE` + `TO_ANIMATE` |
| L1-01-V05 | Potwierdzenie AF | 2 ekrany / sekwencja | brak ekranu fotografowania z AF | `assets/lessons/l1-01/l1-01-v05-af-before.jpg`, `l1-01-v05-af-confirmed.jpg` | `TO_CAPTURE` |
| L1-01-V06 | Łatwy/trudny cel AF | plansza | brak scen referencyjnych | `assets/lessons/l1-01/l1-01-v06-af-easy-hard.jpg` | `TO_CAPTURE` + `TO_DESIGN` |

## L1-02 — Sprawdzam, czy zdjęcie jest ostre

| ID | Zastosowanie | Typ | Źródło / brak | Docelowa ścieżka | Status |
|---|---|---|---|---|---|
| L1-02-V01 | Wzorzec: ważny element ostry / ostrość przesunięta | zestaw dydaktyczny | `Correct.Focus.jpg`, `Front.Focus.jpg` — Bautsch, Wikimedia Commons, CC0 | `assets/lessons/l1-02/l1-02-v01-focus-reference.*` | `SOURCE_IDENTIFIED` |
| L1-02-V02 | Całe zdjęcie → powiększony detal | para edukacyjna | kandydat: `Chive flower close-up.jpg`, Wikimedia Commons, CC0 | `assets/lessons/l1-02/l1-02-v02-full-vs-detail.*` | `SOURCE_IDENTIFIED` + `TO_PREPARE` |
| L1-02-V03 | Przycisk odtwarzania + tylny wybierak | zdjęcie/crop EOS RP Ani z 2 oznaczeniami | `57652b89-ae48-4cd1-b998-e883aee8aa1f.jpg` / `libfile_eb4721328c288191bb5aa19d2aa13f7e` | `assets/lessons/l1-02/l1-02-v03-playback-selector.jpg` | `SOURCE_SELECTED` + `TO_PREPARE` |
| L1-02-V04 | Lupa + główne pokrętło + tylny wybierak | grafika 3-etapowa | tył: `57652b89-ae48-4cd1-b998-e883aee8aa1f.jpg`; góra: `fbe2fd62-e8ab-465b-b340-b6d0b4458622.jpg` | `assets/lessons/l1-02/l1-02-v04-magnify-controls.jpg` | `SOURCE_SELECTED` + `TO_DESIGN` |
| L1-02-V05 | Karta przypominająca wzorzec przy ćwiczeniu | karta UI | wycinki z V01/V02 | `assets/lessons/l1-02/l1-02-v05-sharpness-reference-card.*` | zależny od V01/V02 |

## L1-03 — Układam zdjęcie bez zmiany ustawień

| ID | Zastosowanie | Typ | Źródło / brak | Docelowa ścieżka | Status |
|---|---|---|---|---|---|
| L1-03-V01 | Ten sam przedmiot: rozpraszające vs prostsze tło po zmianie pozycji | para zdjęć | materiał demonstracyjny do przygotowania przez zespół | `assets/lessons/l1-03/l1-03-v01-background-position.*` | `TO_CAPTURE` + `TO_PREPARE` |
| L1-03-V02 | Kontrola czterech brzegów kadru | para edukacyjna + statyczne markery | materiał demonstracyjny do przygotowania przez zespół | `assets/lessons/l1-03/l1-03-v02-frame-edges.*` | `TO_DESIGN` + `TO_PREPARE` |
| L1-03-V03 | Poziomo / pionowo z tego samego miejsca | para zdjęć | materiał demonstracyjny do przygotowania przez zespół | `assets/lessons/l1-03/l1-03-v03-horizontal-vertical.*` | `TO_CAPTURE` + `TO_PREPARE` |
| L1-03-V04A | Jeden krok w bok zmienia tło | para zdjęć | materiał demonstracyjny do przygotowania przez zespół | `assets/lessons/l1-03/l1-03-v04a-step-sideways.*` | `TO_CAPTURE` + `TO_PREPARE` |
| L1-03-V04B | Zmiana wysokości aparatu | 3 zdjęcia | materiał demonstracyjny do przygotowania przez zespół | `assets/lessons/l1-03/l1-03-v04b-camera-height.*` | `TO_CAPTURE` + `TO_PREPARE` |
| L1-03-V05 | RF 50 mm — stała ogniskowa, brak zoomu | zdjęcie obiektywu Ani + diagram | rzeczywisty RF 50 mm Ani + oficjalne dane Canon | `assets/lessons/l1-03/l1-03-v05-fixed-50mm.*` | `SOURCE_REQUIRED` + `TO_DESIGN` |
| L1-03-V06 | Karta „poziomo/pionowo → brzegi/tło → miejsce → zdjęcie” | komponent UI | bez osobnego assetu | komponent aplikacji | `UI_COMPONENT` |

## Następny wpis
Kolejne assety dopisywać przy opracowywaniu następnej lekcji. Nie tworzyć osobnego, równoległego rejestru.