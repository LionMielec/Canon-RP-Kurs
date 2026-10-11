# L1-01-V04 — Spust do połowy i do końca — plan ujęć

## STAN 10.10.2026: WSTRZYMANE (decyzja właściciela)
- W lekcji zostaje rysunek Canon `l1-01-v04-shutter-canon.png` (odebrany, D-070). Temat animacji wróci później.
- Odrzucone przez właściciela:
  - filmy z Higgsfield (Kling 3.0): stukanie, oderwanie palca, podwójny ruch,
  - montaż z kilku ujęć: podwójny ruch,
  - wariant trzech nieruchomych klatek z dźwiękiem.
- Zostaje do wykorzystania: obraz startowy H (kobieca dłoń, D-079) oraz prawdziwe dźwięki aparatu Ani (sygnał „bip” i migawka), wycięte z nagrania `materials/audio/`.
- Koszt prób: około 57 kredytów Higgsfield.
- Wniosek: generatory wideo nie odtwarzają wiarygodnie precyzyjnego, milimetrowego ruchu palca. Przy powrocie do tematu rozważyć prawdziwe nagranie (kobieca dłoń, statyw; nie Ania, D-044).

Poniżej plan w wersji z 10.10.2026, przed wstrzymaniem.

## Cel dydaktyczny
Ania ma zobaczyć, że spust ma dwa etapy: najpierw naciska do połowy i zatrzymuje palec, a dopiero potem dociska do końca (L1-01-S05 i S06).

## Ważne ustalenie przed produkcją
Rzeczywisty ruch spustu między połową a końcem to około milimetra. Na żadnym realistycznym filmie tej różnicy nie widać. Sam film z palcem nie wystarczy, dlatego plan łączy trzy warstwy:
1. film: palec na spuście aparatu Ani, z wyraźną pauzą w połowie,
2. oznaczenie w aplikacji: wskaźnik dwóch etapów („1 — do połowy”, „2 — do końca”), czytelny również bez animacji (D-038),
3. dźwięk (decyzja właściciela z 10.10.2026, sposób wykonania do ustalenia): sygnał potwierdzenia ostrości po naciśnięciu do połowy i dźwięk migawki po dociśnięciu.

## Źródło
- Podstawa: prawdziwe zdjęcie aparatu Ani z przodu, `materials/camera-source-pack-2026-09-24/raw/0155ae68-262e-4364-8a96-8d31dac9ec98.jpg` (EOS RP z RF 50 mm F1.8 STM). Spust jest widoczny na górze uchwytu, po lewej stronie zdjęcia.
- Odrzucone: zdjęcie z góry `fbe2fd62…` (z góry nie widać ruchu w dół) i zdjęcia z boku `8fdcc252…`, `909571b5…` (spust ucięty w kadrze).
- W pakiecie nie ma zdjęcia z dłonią na aparacie. Dłoń dodaje Higgsfield: kobieca, zgodnie z D-079.

## Format
- Plik: MP4 (H.264), około 6 sekund, w pętli, start automatyczny po wejściu w krok (D-19), na iPhonie bez przycisku „Odtwórz”.
- Proporcje 3:2, 1200 × 800, jak pozostałe materiały kursu. Modele wideo Higgsfield nie mają formatu 3:2, więc generujemy w szerszym formacie i przycinamy lokalnie.
- Docelowa ścieżka: `assets/lessons/l1-01/l1-01-v04-shutter-half-full.mp4`.

## Ujęcia

| Czas | Obraz | Oznaczenie w aplikacji | Dźwięk |
|---|---|---|---|
| 0,0–1,0 s | Zbliżenie górnej części uchwytu z przodu. Palec wskazujący prawej dłoni leży na spuście, nie naciska. | brak | cisza |
| 1,0–2,0 s | Palec delikatnie naciska i zatrzymuje się. | „1 — do połowy”, wskaźnik w połowie | pod koniec sygnał ostrości |
| 2,0–3,5 s | Pauza, palec nieruchomo w połowie. | „1 — do połowy” zostaje widoczne | cisza |
| 3,5–4,5 s | Palec spokojnie dociska do końca. Aparat się nie porusza („nie szarp”, S06). | „2 — do końca”, wskaźnik pełny | dźwięk migawki |
| 4,5–6,0 s | Palec puszcza spust i wraca do pozycji z początku (płynna pętla). | wskaźnik pusty | cisza |

Czego nie pokazujemy: ekranu aparatu ani zielonego potwierdzenia ostrości. To osobny materiał L1-01-V05 i musi pochodzić z prawdziwego ekranu (D-050).

## Dźwięk — propozycja do decyzji właściciela
- **Źródło dźwięku (propozycja):** prawdziwe dźwięki aparatu Ani, nagrane telefonem przy aparacie. Sygnał jest w aparacie Ani włączony (ekran menu: Sygnał „bip” — Wł.). Nagrania potrzebne w połowie października, razem z pozostałymi zdjęciami. Zero kredytów i pełna wierność (D-008).
  - Do tego czasu film powstaje bez dźwięku, a nagranie dokładamy lokalnie, zgrane z ruchem palca.
- **Alternatywa:** dźwięk wygenerowany przez model wideo. Jest tańszy w czasie, ale nie odpowiada prawdziwemu aparatowi i nie da się go dokładnie zgrać z pauzą.
- **iPhone:** Safari pozwala na automatyczny start filmu tylko bez dźwięku. Film rusza więc bez dźwięku (D-19), a w aplikacji potrzebny jest przycisk „Włącz dźwięk”. To nowy element interfejsu do zatwierdzenia.
- **Tekst lekcji:** krok S05 mówi, że dźwięk może być wyłączony i ważniejsze jest to, co widać na ekranie. Dźwięk w filmie jest dodatkiem i tego zdania nie zmienia.

## Produkcja — kolejne kroki
1. **Obraz startowy (Higgsfield, obraz z obrazu):** wykonane. Wariant H (kobieca dłoń, palec na spuście). Czeka na akceptację właściciela.
2. **Ruch (Higgsfield, film z obrazu):** około 6 sekund, nieruchoma kamera, zmienia się tylko palec, według tabeli ujęć.
   - Kontrola klatka po klatce, czy aparat nie zmienia kształtu.
3. **Przycięcie, pętla i dźwięk:** lokalnie, bez Higgsfield. Długość, płynne przejście końca w początek, rozmiar 1200 × 800, ścieżka dźwiękowa według tabeli.
4. **Oznaczenie etapów i przycisk dźwięku:** elementy aplikacji zsynchronizowane z filmem.
5. **Odbiór właściciela, a potem osadzenie:** podmiana rysunku Canon `l1-01-v04-shutter-canon.png` i aktualizacja manifestu 16 (pochodzenie: GENEROWANE (Higgsfield, data)).

## Koszt
- Krok 1, wykonany: 6 obrazów w Nano Banana 2.1 po 2 kredyty i 2 w GPT Image 2.5 po 0,25 kredytu, razem 12,5 kredytu.
- Krok 2, ceny sprawdzone 10.10.2026 dla filmu 6 s:
  - Kling 3.0 pro: 10,5 kredytu bez dźwięku, 15 z dźwiękiem,
  - Seedance 2.5: 42 kredyty w 720p, 72 w 1080p.
- Propozycja: najpierw Kling 3.0 pro bez dźwięku, 2 warianty, czyli 21 kredytów.

## Kryteria odbioru
- Aparat wygląda jak aparat Ani: uchwyt, spust, przyciski, brak wymyślonych elementów (D-008).
- Pauza w połowie jest wyraźnie dłuższa niż oba naciśnięcia.
- Dłoń jest kobieca i wygląda naturalnie: pięć palców, ułożenie zgodne z L1-01-V03 (D-079).
- Wskaźnik etapów jest czytelny także na zatrzymanej klatce (D-038).
- Dźwięki padają dokładnie w chwili naciśnięcia do połowy i dociśnięcia.
- Działa płynnie na iPhonie; plik możliwie lekki (cel: poniżej 1,5 MB).

## Ryzyka
- Film z AI może zmienić wygląd aparatu. Wtedy ponawiamy próbę albo przechodzimy do wariantu zapasowego.
- Obraz startowy H: obiektyw wygląda na nieco większy niż na oryginale, a logo „R” po prawej jest prawie zasłonięte.
- **Wariant zapasowy, bez Higgsfield:** prawdziwe zdjęcie `0155ae68…` z dodanym oznaczeniem spustu i animowanym wskaźnikiem etapów w aplikacji. Zero kredytów i pełna wierność aparatu, ale bez palca.
