# Zadania i stan

Aktualizacja: 27.09.2026.

## Aktualny stan — koniec sesji 25.09.2026
- [x] Zatwierdzić bazę L1-01.
- [x] Zatwierdzić L1-02 po korekcie dydaktycznej.
- [x] Przygotować standard produkcji lekcji i wspólny manifest assetów.
- [x] Przygotować lokalny pakiet zdjęć aparatu/menu dla Codexa.
- [x] Wdrożyć L1-01 i L1-02 w istniejącej aplikacji.
- [x] Zachować obecną ikonę, kolorystykę i istniejący Site.
- [x] Opublikować wersję dwóch lekcji.
- [x] Przeprowadzić pierwszy rzeczywisty test na iPhonie 15 Pro Max.
- [x] Potwierdzić, że ogólny kierunek aplikacji i sposobu prowadzenia lekcji jest dobry.
- [x] Zebrać wszystkie drobne niedociągnięcia z testu na iPhonie w jeden pakiet — 27.09.2026.
- [x] Przygotować skonsolidowany dokument wdrożeniowy korekt i poprawić źródłowe dokumenty L1-01/L1-02 — 27.09.2026.
- [x] Wdrożyć jedną rundę korekt bez rozszerzania zakresu: przejście teoria→ćwiczenie, ukrycie ID produkcyjnych, pokazanie „tylnego wybieraka” i innych używanych elementów obsługi.
- [x] Lokalnie odebrać korekty K-01–K-04 — Paweł sprawdził i zaakceptował 27.09.2026.
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

## Dokumentacja startowa

- [x] Odczytać całą dostępną rozmowę planistyczną.
- [x] Zapisać wizję, mapę kursu i zasady nauczania.
- [x] Utworzyć wzór lekcji, plan menu i materiałów.
- [x] Opisać nauczyciela AI, wymagania aplikacji i bezpieczeństwo API.
- [x] Oddzielić ustalenia od propozycji i przyszłych rozszerzeń.
- [x] Utworzyć katalogi materiałów i puste miejsce na aplikację.
- [x] Zweryfikować komplet plików, linki oraz wykluczenia Git.
- [x] Utworzyć lokalne i prywatne zdalne repo.
- [x] Zgoda użytkownika na pierwszy commit oraz push (17.09.2026).

## Następny etap — po zatwierdzeniu

- [x] Przyjąć zdjęcia aparatu, obiektywu i menu — pakiet źródłowy 24.09.2026.
- [ ] Zanotować faktyczny obiektyw, firmware i tryb zdjęć menu.
- [x] Pobrać PL i EN z serwera Canona, potwierdzić model, język i liczbę stron, uzupełnić rejestr źródeł.
- [ ] Pozyskać późniejsze polskie wydanie dla firmware 1.4.0; obecna kopia jest wydaniem początkowym.
- [ ] Porównać istotne dla lekcji różnice między polską i angielską instrukcją.
- [ ] Opisać rzeczywiste główne strony menu.
- [ ] Opracować i zatwierdzić kolejność lekcji Poziomu 1.
- [x] Przygotować pełny szkic [L1-01](L1-01_ROBIE_SWOJE_PIERWSZE_ZDJECIE.md) na podstawie sprawdzonych fragmentów instrukcji.
- [x] Zatwierdzić formę L1-01 jako wzorzec kolejnych lekcji — D-15, 18.09.2026.
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

- [x] Zatwierdzić minimalny zakres aplikacji na iPhone — D-18.
- [x] Przygotować ekran startowy i dwie lekcje według wzorca D-15.
- [x] Dodać fioletową ikonę i manifest uruchamiania z ekranu początkowego.
- [x] Dodać próbne animowane zbliżenie z pauzą i powtórzeniem.
- [x] Sprawdzić obie lekcje w przeglądarce przy szerokościach 320, 430, 440 i 1024 px, ograniczenie ruchu, pomoc i powiększony tekst.
- [x] Sprawdzić opublikowaną aplikację na rzeczywistym iPhonie 15 Pro Max — 25.09.2026.
- [x] Ocenić ogólny kierunek, kolorystykę i działanie na iPhonie; drobne korekty UX przechodzą do jednej rundy następnej sesji.
- [ ] Ustalić dostęp dla Ani i sprawdzić jej iPhone 17 Pro Max.

Szczegóły: [13 — Pierwsza aplikacja](13_PIERWSZA_APLIKACJA.md). Test przeglądarkowy nie zastępuje testu Safari ani aparatu Ani.

## Następna sesja — priorytety po przeglądzie aplikacji

- [x] Zapisać pozytywną ocenę wyglądu aplikacji przez użytkownika; finalny dobór odcieni nadal otwarty.
- [x] Dodać klikalny spis lekcji z wejściami do lekcji i bezpośrednio do ćwiczeń.
- [ ] Ustalić źródło i sposób wykonania jednej animacji „Włącz aparat”.
- [ ] Przygotować i ocenić animację: obrót → zbliżenie → ruch przełącznika; automatyczny start, bez wymaganego przycisku „Odtwórz” (D-19).
- [ ] Zastąpić duże kółko precyzyjnym obrysem/strzałką śledzącą właściwy element.
- [x] Potwierdzić działanie aktualnej wersji z istniejącej ikony na iPhonie 15 Pro Max — 25.09.2026.

Sekcja powyżej opisuje historię etapu z 18.09.2026. Część zadań została później wykonana; bieżące zadania są wyłącznie w sekcji „Aktualny stan — koniec sesji 25.09.2026”.

## Uzupełnienie po przeniesieniu pracy do Codex — 18.09.2026

- [x] Zapisać intencję niespodzianki, oczekiwanie efektu „wow” i rolę animacji — D-21.
- [x] Zapisać zdalny sposób zbierania zdjęć oraz niezależność pracy nad treścią — D-22.
- [x] Użytkownik utworzył lokalny projekt Codex „Canon RP - Kurs” i potwierdził dodanie folderów dokumentacji oraz aplikacji.
- [ ] Po zgłoszeniu gotowości 19.09.2026 poprowadzić Pawła i Anię przez zdjęcia aparatu, po jednym ujęciu, z oceną przesyłanych materiałów.
- [ ] Nową rozmowę rozpocząć w lokalnym projekcie i odczytać zaktualizowane przekazanie sesji. Dotychczasowa rozmowa pozostaje powiązana z projektem ChatGPT.

Priorytety D-19 i D-20 pozostają aktualne; sesja zdjęciowa nie stanowi zgody na zmianę aplikacji, publikację ani płatne generowanie. Najnowsze ustalenia uzupełniają starsze sekcje tego dokumentu; nie oznaczają zatwierdzenia całego programu Poziomu 1.

## Treści kursu i nauczyciel AI — doprecyzowanie 18.09.2026

- [x] Utrwalić proces: sprawdzenie źródeł → wyjaśnienie i ćwiczenie → zgodność z aparatem Ani (D-23, dokument 03).
- [ ] Po zatwierdzeniu programu przygotować pozostałe lekcje według tego procesu. Dwie istniejące lekcje nie stanowią całego kursu; spis treści i animacje nie zastępują pracy nad treścią.
- [x] Doprecyzować analizę nowych i wcześniejszych zdjęć Ani, również z innego sprzętu i bez EXIF, oraz współpracę przez pytania i kolejne próby (D-24, dokument 06).
- [ ] W przyszłym zatwierdzonym etapie wdrożyć nauczyciela AI i przeprowadzić próby opisane w dokumencie 06. Moduł nie działa jeszcze w aplikacji.


## PRIORYTET NASTĘPNEJ SESJI — skill dla Codexa
- [ ] Sprawdzić aktualny oficjalny mechanizm skilli / trwałych instrukcji dla Codexa.
- [x] Opracować skill na podstawie `20_CODEX_PRECISION_SKILL_PLAN.md`.
- [x] Przygotować i zatwierdzić `AGENTS.md` dla projektu.
- [x] Dodać `AGENTS.md` i skill do właściwego środowiska Codexa.
- [x] Zweryfikować działanie skilla na małym zadaniu kontrolnym.
- [x] Potwierdzić, czy `dist/` jest źródłem kanonicznym czy wynikiem builda — `dist/` jest źródłem kanonicznym.
- [ ] Dokończyć lokalną mikrokorektę L1-02 w kanonicznych plikach `dist/`.
- [x] Przyjąć finalny kierunek oznaczeń elementów aparatu — statyczne, wyraźne oznaczenie zaakceptowane 28.09.2026; pulsowanie nie jest wymagane.
- [ ] Odbiór lokalny przez Pawła.
- [ ] Po akceptacji: commit → push → publikacja do istniejącego Site.
- [ ] Test na fizycznym iPhonie.
- [x] Formalnie zamknąć L1-01/L1-02 jako wzorzec redakcyjny/UX — 28.09.2026.
- [x] Rozpocząć redagowanie L1-03 — 28.09.2026.

**Blokada:** do czasu dodania i sprawdzenia skilla nie kontynuować implementacji aplikacji w Codexie.

- [x] Zweryfikować źródła i przygotować pełny szkic L1-03 — 28.09.2026.
- [x] Omówić i zatwierdzić treść L1-03 z właścicielem projektu przed implementacją — 28.09.2026.
- [x] Przygotować kartę wizualno-produkcyjną i asset manifest L1-03 — 28.09.2026.

- [x] Po powrocie do komputera wykonać finalny review L1-03 i przygotować handoff dla Codexa — 28.09.2026.
- [x] Przekazać zatwierdzony pakiet L1-03 Codexowi i wykonać implementację lokalną — 28.09.2026.

- [x] Odebrać lokalnie układ, treść i UX L1-03 — 28.09.2026.
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

- [x] Przenieść kod aplikacji do `app/` z historią zmian.
- [x] Zainstalować i sprawdzić instrukcje dla Claude Code.
- [ ] Wypracować sposób pozyskania materiałów L1-03: V01, V02, V03, V04A, V04B, V05.
- [ ] Rozdzielić mikrokorektę L1-02 od L1-03 na gałęzi `wip/l1-02-l1-03`; odbiór L1-01 i L1-02 przez właściciela.
- [ ] Poprawić zbędne znaki w polach statusu L1-03.
- [ ] Zdecydować o hostingu i sposobie publikacji.
- [ ] Uporządkować ścieżki z dawnego folderu Codexa w testach i `app/README.md`.
- [ ] Przy pierwszej nowej lekcji sprawdzić w praktyce standard pracy ze źródłami z D-048.
- [ ] Przy pierwszej lekcji ustalić wersję firmware aparatu Ani (ścieżkę w menu wskaże instrukcja Canon).
- [ ] Przy pierwszej animacji ustalić techniczne połączenie Claude Code z Higgsfield oraz koszt.
