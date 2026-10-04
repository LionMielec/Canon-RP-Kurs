# Zadania i stan

Aktualizacja: 27.09.2026.

## Aktualny stan — koniec sesji 25.09.2026
- [ ] Commit + push zmian aplikacji.
- [ ] Opublikować poprawioną wersję do istniejącego Canon RP Site.
- [ ] Sprawdzić opublikowaną wersję na rzeczywistym iPhonie 15 Pro Max.
- [ ] Po pozytywnym teście formalnie zamknąć L1-01/L1-02 jako wzorzec i rozpocząć L1-03.
- [ ] Ponownie sprawdzić skorygowaną wersję na iPhonie 15 Pro Max.
- [ ] Po pozytywnym teście formalnie uznać L1-01/L1-02 za wzorzec implementacyjny kolejnych lekcji.
- [ ] Dopiero potem rozpocząć wspólny przegląd L1-03.
- [ ] Produkować brakujące finalne assety L1-01/L1-02 według potrzeb, bez materiałów „na zapas”.
- [ ] Docelowo sprawdzić kurs również na iPhonie 17 Pro Max Ani.

## Zasada na następną sesję
Nie wracamy do ponownego analizowania zakończonych decyzji, nie przebudowujemy aplikacji od zera i nie otwieramy nowych modułów. Najpierw domykamy zauważone niedociągnięcia w istniejącym wzorcu dwóch lekcji.

## Historia wcześniejszych zadań

## Następny etap — po zatwierdzeniu

- [ ] Zanotować faktyczny obiektyw, firmware i tryb zdjęć menu.
- [ ] Pozyskać późniejsze polskie wydanie dla firmware 1.4.0; obecna kopia jest wydaniem początkowym.
- [ ] Porównać istotne dla lekcji różnice między polską i angielską instrukcją.
- [ ] Opisać rzeczywiste główne strony menu.
- [ ] Opracować i zatwierdzić kolejność lekcji Poziomu 1.
- [ ] Uzupełnić L1-01 o własne materiały wizualne i sprawdzić przebieg na aparacie Ani.

## Przed przyszłą implementacją

- [ ] Zatwierdzić technologię, hosting, dostęp i przechowywanie postępów.
- [ ] Określić retencję zdjęć i zakres danych przekazywanych AI.
- [ ] Zatwierdzić budżet i model; sprawdzić aktualne ceny oraz dostęp na koncie.
- [ ] Zaplanować małą próbę jakości i kosztu na rzeczywistych zdjęciach.

Nie uruchamiamy następnego etapu automatycznie tylko dlatego, że katalog aplikacji jest już przygotowany.

## Repozytorium

Folder roboczy: `/Users/pawelsiedleczka/Documents/ChatGPT/Canon-RP-Kurs`.

[GitHub: LionMielec/Canon-RP-Kurs](https://github.com/LionMielec/Canon-RP-Kurs) — prywatne; lokalnie zainicjalizowana gałąź `main`, połączenie `origin` sprawdzone. Użytkownik zatwierdził pierwszy commit i push dokumentacji 17.09.2026. PDF pozostają lokalnie, poza Git.

Weryfikacja: 23 pliki, 12 dokumentów w `docs/`, poprawne odnośniki lokalne, brak wzorców sekretów; `.env`, zdjęcia, filmy i PDF w materiałach wykluczone z Git. Aplikacja nie zawiera kodu.

## Baza materiałów — uzupełnienie 17.09.2026

Dodano 2 instrukcje PDF (łącznie 61 035 389 bajtów), opis plików i katalog 17 odcinków online. Zweryfikowano liczbę stron, wybrane renderowane strony i sumy SHA-256. Pełny przegląd treści instrukcji jest kolejnym zadaniem. Historyczna liczba 23 plików powyżej dotyczy etapu startowej dokumentacji.

## Pierwszy szkielet aplikacji — 18.09.2026

- [ ] Ustalić dostęp dla Ani i sprawdzić jej iPhone 17 Pro Max.

Szczegóły: [13 — Pierwsza aplikacja](archiwum/13_PIERWSZA_APLIKACJA.md). Test przeglądarkowy nie zastępuje testu Safari ani aparatu Ani.

## Następna sesja — priorytety po przeglądzie aplikacji

- [ ] Ustalić źródło i sposób wykonania jednej animacji „Włącz aparat”.
- [ ] Przygotować i ocenić animację: obrót → zbliżenie → ruch przełącznika; automatyczny start, bez wymaganego przycisku „Odtwórz” (D-19).
- [ ] Zastąpić duże kółko precyzyjnym obrysem/strzałką śledzącą właściwy element.

Sekcja powyżej opisuje historię etapu z 18.09.2026. Część zadań została później wykonana; bieżące zadania są wyłącznie w sekcji „Aktualny stan — koniec sesji 25.09.2026”.

## Uzupełnienie po przeniesieniu pracy do Codex — 18.09.2026

- [ ] Po zgłoszeniu gotowości 19.09.2026 poprowadzić Pawła i Anię przez zdjęcia aparatu, po jednym ujęciu, z oceną przesyłanych materiałów.
- [ ] Nową rozmowę rozpocząć w lokalnym projekcie i odczytać zaktualizowane przekazanie sesji. Dotychczasowa rozmowa pozostaje powiązana z projektem ChatGPT.

Priorytety D-19 i D-20 pozostają aktualne; sesja zdjęciowa nie stanowi zgody na zmianę aplikacji, publikację ani płatne generowanie. Najnowsze ustalenia uzupełniają starsze sekcje tego dokumentu; nie oznaczają zatwierdzenia całego programu Poziomu 1.

## Treści kursu i nauczyciel AI — doprecyzowanie 18.09.2026

- [ ] Po zatwierdzeniu programu przygotować pozostałe lekcje według tego procesu. Dwie istniejące lekcje nie stanowią całego kursu; spis treści i animacje nie zastępują pracy nad treścią.
- [ ] W przyszłym zatwierdzonym etapie wdrożyć nauczyciela AI i przeprowadzić próby opisane w dokumencie 06. Moduł nie działa jeszcze w aplikacji.

## PRIORYTET NASTĘPNEJ SESJI — skill dla Codexa
- [ ] Sprawdzić aktualny oficjalny mechanizm skilli / trwałych instrukcji dla Codexa.
- [ ] Dokończyć lokalną mikrokorektę L1-02 w kanonicznych plikach `dist/`.
- [ ] Odbiór lokalny przez Pawła.
- [ ] Po akceptacji: commit → push → publikacja do istniejącego Site.
- [ ] Test na fizycznym iPhonie.

**Blokada:** do czasu dodania i sprawdzenia skilla nie kontynuować implementacji aplikacji w Codexie.

- [ ] Przygotować i odebrać sześć brakujących materiałów wizualnych L1-03.
- [ ] Osadzić zatwierdzone assety w L1-03 i wykonać krótki lokalny odbiór końcowy.
- [ ] Po odbiorze: commit → push → publikacja do istniejącego Site.
- [ ] Sprawdzić opublikowaną L1-03 na fizycznym iPhonie.

- [ ] Przygotować shot list jednej kontrolowanej sesji zdjęciowej L1-03 z rośliną w doniczce.
- [ ] Wykonać samodzielnie realne zdjęcia V01, V02, V03, V04A, V04B oraz rzeczywiste zdjęcie obiektywu V05 w jednej krótkiej kontrolowanej sesji domowej — bez angażowania Ani jako producentki materiałów kursu.
- [ ] Opracować wyłącznie statyczne oznaczenia/UI na realnych zdjęciach.

## PRIORYTET NASTĘPNEGO WĄTKU — materiały L1-03
- [ ] Generowane sceny L1-03 tylko na warunkach D-050.
- [ ] Nie wracać do pomysłu zewnętrznego fotografa jako domyślnego rozwiązania.
- [ ] Nie angażować Ani jako producentki materiałów szkoleniowych.
- [ ] Wypracować profesjonalny, wiarygodny i niskokosztowy sposób pozyskania V01, V02, V03, V04A, V04B i V05.
- [ ] Dopiero po wyborze sposobu produkcji przygotować finalny shot list / plan pozyskania assetów.
- [ ] Po pozyskaniu materiałów: osadzenie w L1-03 → lokalny odbiór → commit → push → publikacja → test na iPhonie.

**Blokada:** L1-03 nie idzie do finalnej publikacji bez gotowych materiałów demonstracyjnych.

## PRIORYTETY PO 29.09.2026 (D-047)
Wcześniejsze sekcje są historyczne; role według D-047.

- [ ] Decyzje właściciela: odbicie książki, kadry V01/V03/V04B, przebudowa V02 (handoff 30.09).
- [ ] Rendery finalne V01, V02, V03, V04B i odbiór.
- [ ] V05: wybór zdjęcia obiektywu, źródło Canon, schemat.
- [ ] Osadzenie assetów w L1-03, aktualizacja manifestu 16 i karty L1-03 z tabelą źródeł.
- [ ] Rozdzielić mikrokorektę L1-02 od L1-03 na gałęzi `wip/l1-02-l1-03`; odbiór L1-01 i L1-02 przez właściciela.
- [ ] Poprawić zbędne znaki w polach statusu L1-03.
- [ ] Zdecydować o hostingu i sposobie publikacji.
- [ ] Uporządkować ścieżki z dawnego folderu Codexa w testach i `app/README.md`.
- [ ] Przy pierwszej nowej lekcji sprawdzić w praktyce standard pracy ze źródłami z D-048.
- [ ] Przy pierwszej animacji ustalić techniczne połączenie Claude Code z Higgsfield oraz koszt.

## OTWARTE PO 01.10.2026
- [ ] L1-03: odbiór wszystkich materiałów przez właściciela i zamknięcie lekcji.
- [ ] L1-04: redakcja według D-049, równolegle z materiałami L1-03 (D-055).
- [ ] L1-04: po powrocie właściciela porównać rysunki z instrukcji z ekranami aparatu Ani i ustalić wersję oprogramowania (D-056).
- [ ] Hosting: wersja aplikacji z rysunkami Canon dostępna wyłącznie dla Ani (D-056).
- [ ] L1-04: sprawdzić na aparacie Ani punkty z docs/L1-04_ZRODLA_INSTRUKCJA.md (D-056).
- [ ] Nauczyciel AI: przepisać dokumenty 06 i 11 pod model Claude przy integracji (D-059).
- [ ] Hosting: główny kandydat — VPS właściciela w Hetzner; do ustalenia: domena, co już działa na serwerze, wygodne logowanie Ani z ikony na iPhonie.

## POPRAWKI PO PRZEGLĄDZIE WŁAŚCICIELA — 01.10.2026
- [ ] Po powrocie właściciela: zdjęcie ekranu aparatu Ani z pomarańczowym punktem ostrości (L1-04-V18; skierować aparat na gładką ścianę i nacisnąć spust do połowy).
- [ ] Po powrocie właściciela: zdjęcie ekranu aparatu Ani z punktem ostrości przesuniętym w bok (L1-04-V07).

## L1-05 — 03.10.2026
- [x] Krok 2: odczyt źródeł z instrukcji Canon (`docs/L1-05_ZRODLA_INSTRUKCJA.md`).
- [x] Krok 3: tekst, karta wizualno-produkcyjna i lista kontrolna — brama 2 (D-069).
- [x] Krok 4: wdrożenie w aplikacji na gałęzi `wip/l1-02-l1-03` i arkusz zrzutów.
- [x] Krok 5: odbiór właściciela w aplikacji — brama 3 (D-070).

## OTWARTE PO 03.10.2026
- [ ] L1-01: jawne miejsce dla rysunków Canon V04–V05 w wersji publicznej (jak D-069); V03 rozwiązane przez D-071.
- [ ] Decyzja: scalenie `wip/l1-02-l1-03` do `main`.
- [ ] Decyzja: podpis „Kadr roboczy · do zatwierdzenia” pod obrazami w aplikacji i pole status w lessons.js (propozycja z 03.10).
- [ ] Decyzja: wykluczenie w .gitignore lokalnych renderów i podglądów production/l1-0*/ oraz __pycache__ (propozycja z 03.10).
- [ ] L1-06: grafiki z Higgsfield po płatnym koncie i zatwierdzeniu zakresu (D-019).

## PO POWROCIE WŁAŚCICIELA — połowa października 2026
- [ ] Sprawdzenie na aparacie L1-04 + L1-05 (listy w L1-04_ZRODLA_INSTRUKCJA.md i L1-05_ZRODLA_INSTRUKCJA.md).
- [ ] Zdjęcia: L1-04-V07, L1-04-V18, L1-05-V03.
