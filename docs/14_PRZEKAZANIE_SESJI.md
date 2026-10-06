# HANDOFF — Canon RP kurs — korekty wzorca — 27.09.2026

## HANDOFF 01.10.2026 — materiały L1-01–L1-04, szkic L1-04, aplikacja na gałęzi roboczej

### Co zostało wykonane
- Decyzje D-053–D-062.
- `review/`: lekkie kopie materiałów i zdjęć aparatu Ani (bez GPS i numerów seryjnych); Claude w czacie ocenia materiały bezpośrednio w repozytorium.
- L1-03: rendery finalne V03-pionowo i V04B-1–3 (2400×1600); V01-po v2, V02-A i V02-B v3 (1200×800); V05 część A (zdjęcie obiektywu `40b8cbb9…`) i część B (schemat SVG). Wszystkie przejrzane przez Claude w czacie; odbiór właściciela w aplikacji.
- L1-04: zakres zatwierdzony (brama 1); źródła z instrukcji w `docs/L1-04_ZRODLA_INSTRUKCJA.md`; szkic lekcji i karta wizualno-produkcyjna; rendery „bliżej / dalej”; rysunki z instrukcji Canon (lokalnie, końcówka `-canon`, D-056); zdjęcia aparatu Ani z oznaczeniami.
- L1-01: rysunki Canon V03 (trzymanie z patrzeniem na ekran), V04 (jeden rysunek spustu), V05 (ramka bez oznaczenia trybu P); plansza V06 z czterech renderów (D-058).
- L1-02: V01 — para renderów (ostrość dobra / przesunięta); V02 — render V04A i powiększony napis. Zdjęcia z Wikimedia odrzucone po przeglądzie; pozostają lokalnie, nieużywane.
- Aplikacja: materiały L1-01–L1-03 i pełna L1-04 wstawione na gałęzi `wip/l1-02-l1-03` (lokalny podgląd, bez publikacji). `.gitignore` wyklucza `*-canon.*` i `production/assets/`.
- Oprogramowanie aparatu Ani: wersja 1.6.3 (odczyt 01.10.2026).
- Hosting: główny kandydat — VPS właściciela w Hetzner. Nauczyciel AI: model Claude (D-059).

### Do poprawy po przeglądzie właściciela w lokalnym podglądzie
1. L1-04, krok 5: oznaczenia w złych miejscach; brak oznaczenia przycisku Q/SET.
2. L1-04, drugi kadr kroku 5: podpis „punkt przesunięty w bok” nie zgadza się z rysunkiem (punkt na środku).
3. L1-04, część „Jeśli coś nie działa”: niezrozumiała, brzmi jak instrukcja obsługi — do przepisania według D-062.
4. Odwołania do kroków i części mają być linkami (D-060), także w L1-01–L1-03.
5. Strona główna: karty lekcji naprzemiennie różowa i biała (lekcja 1 różowa, 2 biała, 3 różowa, 4 biała i tak dalej).

### Otwarte
- Poprawki z listy powyżej — pierwszy cel następnej sesji.
- Odbiór wszystkich materiałów L1-01–L1-04 przez właściciela w aplikacji; potem rozdzielenie mikrokorekty L1-02, scalenie gałęzi i decyzja o publikacji.
- Hosting: domena, co już działa na serwerze, wygodne logowanie Ani z ikony na iPhonie; wersja z rysunkami Canon dostępna wyłącznie dla Ani (D-056).
- Po powrocie właściciela do domu (około połowy października): porównanie rysunków Canon z ekranami aparatu Ani i sprawdzenie punktów z `docs/L1-04_ZRODLA_INSTRUKCJA.md`.
- Nowsza polska instrukcja dla oprogramowania 1.4.0 lub nowszego.
- L1-01-V04: animacja spustu później, według D-049.

### Start następnej sesji
Claude w czacie czyta całą dokumentację (D-061), potwierdza stan i cel.

## HANDOFF 02.10.2026 — poprawki L1-04, jedna nazwa dla elementu
Uzupełnione 03.10.2026 wyłącznie na podstawie historii commitów.

### Co zostało wykonane
- Decyzje D-063–D-067.
- L1-04: poprawki tekstu; materiały V11–V18 w karcie wizualno-produkcyjnej i manifeście assetów; opisy V06 i V07.
- Słownik nazw `docs/24_SLOWNIK_NAZW.md` (D-065, D-066) i lista kontrolna lekcji `docs/25_LISTA_KONTROLNA_LEKCJI.md` (D-067); nazwy zastosowane w dokumentach L1-01–L1-04.
- Aplikacja (gałąź `wip/l1-02-l1-03`): poprawki L1-04 po przeglądzie właściciela, odwołania jako linki (D-060), obrazy przy podpunktach (D-064), naprzemienne karty lekcji na stronie głównej; nazwy z D-065 i D-066 w L1-01–L1-04; zrzuty wszystkich ekranów w szerokości 430 px.

## HANDOFF 03.10.2026 — L1-05 wdrożona na gałęzi roboczej

### Co zostało wykonane
- Decyzje D-068 (oszczędzanie limitu) i D-069 (rozstrzygnięcia właściciela dla L1-05).
- Cele lekcji L1-01–L1-04 w bezpośredniej formie zwracania się do Ani (dokumenty i aplikacja); w `CLAUDE.md` zapis o zgodzie na commit i push.
- Dokumenty historyczne przeniesione do `docs/archiwum/` (D-068).
- L1-05: zakres (brama 1) i tekst (brama 2) zatwierdzone; źródła z instrukcji w `docs/L1-05_ZRODLA_INSTRUKCJA.md`; tekst lekcji, karta wizualno-produkcyjna, nazwy w słowniku, wpisy w manifeście; podglądy V01 i V02 w `review/`.
- Skrypt sceny `production/l1-03/scene/build_v04a_scene.py`: opcja przesunięcia ekspozycji dla L1-05-V01.
- Aplikacja (gałąź `wip/l1-02-l1-03`): lekcja L1-05; arkusz zrzutów `review/app/l1-05/arkusz.jpg`. W L1-04 i L1-05 rysunek z instrukcji Canon, którego brak w wersji publicznej, zastępuje jawne miejsce „Materiał w przygotowaniu” (D-069).

- Odbiór właściciela w aplikacji (brama 3): L1-01–L1-05 odebrane 03.10.2026 (D-070).

### Stan
- L1-01–L1-05 — odebrane w aplikacji na gałęzi `wip/l1-02-l1-03` (D-070).
- L1-04 i L1-05 — czekają na sprawdzenie na aparacie Ani.

### Otwarte
- Decyzja o scaleniu gałęzi `wip/l1-02-l1-03` do `main` (D-070).
- L1-01: trzy rysunki z instrukcji Canon (V03, V04, V05) nie mają jawnego miejsca w wersji publicznej — ta sama poprawka co w L1-04 (D-069).
- Wspólne sprawdzenie L1-04 i L1-05 na aparacie Ani po powrocie właściciela (połowa października) — listy w `docs/L1-04_ZRODLA_INSTRUKCJA.md` i `docs/L1-05_ZRODLA_INSTRUKCJA.md`; tam też wpływ [Autom. optymalizator jasności] przy −1 (D-069).
- Zdjęcia do zrobienia: L1-04-V07, L1-04-V18, L1-05-V03.
- Hosting i publikacja — wstrzymane (D-047).

### Start następnej sesji
Claude w czacie czyta całą aktywną dokumentację (D-061, D-068). Następny cel: do decyzji właściciela.

## HANDOFF 03.10.2026 (wieczór) — zdjęcie trzymania aparatu z Higgsfield

### Co zostało wykonane
- D-071: wyjątek od D-050 dla materiału L1-01-V03 (ułożenie ciała, nie wygląd aparatu); nowa kategoria pochodzenia GENEROWANE; licencja obrazu z darmowych kredytów do potwierdzenia przed ewentualną komercjalizacją.
- L1-01-V03: obraz z Higgsfield zastępuje rysunek z instrukcji Canon i działa także w wersji publicznej; status APPROVED; zrzut `review/app/l1-01/s03-trzymanie.jpg`.
- Gałąź `main` wciągnięta do `wip/l1-02-l1-03` (commit 961a7f1).

### Stan
- Aktualna dokumentacja jest na gałęzi `wip/l1-02-l1-03`; `main` jest w tyle do czasu scalenia.

### Otwarte
- Decyzja o scaleniu `wip/l1-02-l1-03` do `main` (D-070).
- Propozycja: podpis „Kadr roboczy · do zatwierdzenia” jest wpisany na sztywno pod każdym obrazem w aplikacji (`app/dist/app.js`), także po odbiorze (D-070, D-071); przy tej samej zmianie ujednolicić pole status w `app/dist/lessons.js` z manifestem. Do decyzji właściciela, pełny tryb.
- Propozycja: wykluczyć w `.gitignore` lokalne rendery i podglądy w `production/l1-0*/` oraz pliki `__pycache__` (zgodnie z D-053).
- Grafiki do L1-06 z Higgsfield — po wykupieniu płatnego konta (planowane w tygodniu od 05.10.2026) i po zatwierdzeniu zakresu L1-06 (D-019).
- Bez zmian: sprawdzenie L1-04 i L1-05 na aparacie Ani oraz zdjęcia L1-04-V07, L1-04-V18, L1-05-V03 (połowa października); hosting i publikacja wstrzymane (D-047).

### Start następnej sesji
Claude w czacie czyta całą aktywną dokumentację z gałęzi `wip/l1-02-l1-03` (D-061, D-068). Następny cel: do decyzji właściciela.

## HANDOFF 04.10.2026 — porządki i scalenie do main

### Co zostało wykonane
- Scalenie `wip/l1-02-l1-03` do `main`: commity scalenia 7b9c330 i ecb2b36.
- Aplikacja: usunięty podpis „Kadr roboczy” pod obrazami i pole status w `app/dist/lessons.js`; statusy materiałów prowadzi wyłącznie `docs/16_ASSET_MANIFEST.md` (D-074).
- L1-01: rysunki Canon V04 i V05 tylko lokalnie; w wersji publicznej jawne miejsce „Materiał w przygotowaniu” (jak D-069).
- Test `app/tests/camera-guidance.cjs` dostosowany do statycznych oznaczeń (D-038) i do rysunków tylko lokalnych.
- Numery wersji przy `app.js` i `lessons.js` w `app/dist/index.html` zmienione na `2026-10-04`; w `CLAUDE.md` zasada zmiany numeru wersji po każdej zmianie tych plików.
- Decyzje D-072 (nowa reguła obejmuje wszystkie istniejące lekcje), D-073 (błędy naprawiamy od razu), D-074 (statusy w jednym miejscu i arkusze zrzutów).
- Manifest materiałów: materiały wyświetlane w L1-01–L1-05 ze statusem APPROVED (D-070).

### Otwarte
- Bez zmian: sprawdzenie L1-04 i L1-05 na aparacie Ani oraz zdjęcia L1-04-V07, L1-04-V18, L1-05-V03 (połowa października).
- Propozycja: wykluczyć w `.gitignore` lokalne rendery i podglądy w `production/l1-0*/` oraz pliki `__pycache__`.
- Grafiki z Higgsfield — po wykupieniu płatnego konta.
- Hosting i publikacja — wstrzymane (D-047).

### Start następnej sesji
Nowa rozmowa w projekcie claude.ai (D-068). Claude w czacie czyta całą aktywną dokumentację. Następny cel: L1-06, od zakresu (brama 1).

## HANDOFF 05.10.2026 — L1-06: tekst i materiały odebrane

### Co zostało wykonane
- L1-06: zakres i tekst zatwierdzone (D-075); źródła z instrukcji w `docs/L1-06_ZRODLA_INSTRUKCJA.md`; karta wizualno-produkcyjna.
- L1-06: materiały V01, V02, V03 odebrane przez właściciela 05.10.2026 (D-075); statusy w `docs/16_ASSET_MANIFEST.md`.
- Aplikacja: pasek „Wróć” po odsyłaczu (D-076), odebrany przez właściciela 05.10.2026; w `main` po scaleniu.
- Gałąź `wip/l1-02-l1-03` scalona do `main`.

### Następny cel — wdrożenie L1-06 w aplikacji
- Treść lekcji w `app/dist/lessons.js`.
- Karta 06 na stronie głównej: napis kategorii „Patrzę na światło”, około 15 minut, zachowana naprzemienność kolorów kart.
- Kopie V01, V03 oraz schematów V02 (z `production/l1-06/v02/`) do `app/dist/assets/lessons/l1-06/`.
- Komponent V04.
- Materiały z wcześniejszych lekcji: L1-05-V02, L1-05-V04 (lokalnie), L1-02-V03.
- Arkusz zrzutów i odbiór właściciela w aplikacji (brama 3).

### Otwarte
- Sprawdzenie L1-06 na aparacie — lista w `docs/L1-06_ZRODLA_INSTRUKCJA.md`, zwłaszcza ile plusa przy świetle od tyłu.
- Bez zmian: sprawdzenie L1-04 i L1-05 na aparacie Ani oraz zdjęcia L1-04-V07, L1-04-V18, L1-05-V03 (połowa października).
- Propozycja: wykluczyć w `.gitignore` lokalne rendery i podglądy w `production/l1-0*/` oraz pliki `__pycache__`.
- Grafiki z Higgsfield — po wykupieniu płatnego konta.
- Hosting i publikacja — wstrzymane (D-047).

### Start następnej sesji
Nowa rozmowa w projekcie claude.ai (D-068). Claude w czacie czyta całą aktywną dokumentację. Następny cel: wdrożenie L1-06 w aplikacji.

## HANDOFF 06.10.2026 — L1-06 wdrożona i odebrana

### Co zostało wykonane
- L1-06 w aplikacji: tekst lekcji, materiały V01–V04 oraz L1-05-V02, L1-05-V04 (lokalnie) i L1-02-V03; karta 06 na stronie głównej (D-077).
- Rozmieszczenie obrazów, podpisy i rozmiar renderów 1200 × 800 zatwierdzone przez właściciela (D-077).
- Arkusz zrzutów `review/app/l1-06/arkusz.jpg`; testy `camera-guidance.cjs` i `back-bar.cjs` zaliczone.
- Odbiór właściciela w aplikacji 06.10.2026 (brama 3, D-077); gałąź `wip/l1-02-l1-03` scalona do `main`.
- Uwaga techniczna: testy aplikacji wymagają pakietu `playwright-core`; pobierany za zgodą właściciela do katalogu tymczasowego, poza projektem, i uruchamiany na zainstalowanym Google Chrome.

### Otwarte
- Sprawdzenie L1-06 na aparacie — lista w `docs/L1-06_ZRODLA_INSTRUKCJA.md`, zwłaszcza ile plusa przy świetle od tyłu (tekst lekcji podaje 1, pomoc 2).
- Bez zmian: sprawdzenie L1-04 i L1-05 na aparacie Ani oraz zdjęcia L1-04-V07, L1-04-V18, L1-05-V03 (połowa października).
- Propozycja: wykluczyć w `.gitignore` lokalne rendery i podglądy w `production/l1-0*/` oraz pliki `__pycache__`.
- Grafiki z Higgsfield — po wykupieniu płatnego konta.
- Hosting i publikacja — wstrzymane (D-047).

### Start następnej sesji
Nowa rozmowa w projekcie claude.ai (D-068). Claude w czacie czyta całą aktywną dokumentację. Następny cel: do decyzji właściciela; według programu w `docs/12_PROGRAM_POZIOMU_1.md` kolejna jest L1-07 „Rozmywam tło”.
