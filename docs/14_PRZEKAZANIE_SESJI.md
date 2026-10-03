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
