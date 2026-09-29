# HANDOFF — Canon RP kurs — korekty wzorca — 27.09.2026

## Punkt startowy
L1-01 i L1-02 są zatwierdzone, wdrożone i opublikowane. Nie wracać do ich projektowania od zera.

Paweł zakończył zbieranie drobnych uwag po teście na iPhonie 15 Pro Max. Pakiet został utrwalony w `docs/19_KOREKTY_WZORCA_2026-09-27.md`. Następnym działaniem jest **jedna skonsolidowana runda korekt w istniejącej aplikacji**.

## Pakiet korekt do wdrożenia

### K-01 — Przejście z teorii do ćwiczenia
Obecne przejście w L1-01 od „Dociśnij do końca” do „Powtórz jeszcze dwa razy” jest zbyt nagłe.

Należy dodać krótkie domknięcie części dydaktycznej, np. sens:
- Ania zna już cały podstawowy cykl wykonania zdjęcia,
- krótko przypominamy: wyceluj → półnaciśnij → poczekaj na potwierdzenie ostrości → dociśnij,
- następnie jawne zdanie: „Teraz przejdźmy do ćwiczenia.”

Przycisk rozpoczynający ćwiczenie powinien być opisowy, np. **„Przejdź do ćwiczenia →”**, zamiast neutralnego „Dalej”.

Samo ćwiczenie może potem używać krótkiego polecenia, np. „Zrób jeszcze dwa zdjęcia”.

### K-02 — Usunąć identyfikatory produkcyjne z UI
Identyfikatory typu `L1-01`, `L1-02`, `S03`, `V04` są wewnętrzne.

Nie mogą być widoczne dla Ani w żadnej części aplikacji. Warstwa użytkowa pokazuje naturalne nazwy: „Lekcja 1”, „Lekcja 2”, tytuł lekcji, „Krok x z y”, „Ćwiczenie” itd.

### K-03 — Pokazać „tylny wybierak” i wszystkie elementy obsługi używane w tekście
W L1-02 tekst odwołuje się do „tylnego wybieraka” przy przechodzeniu między zdjęciami i przesuwaniu powiększonego widoku.

Jeśli Ania ma użyć fizycznego elementu aparatu:
1. najpierw pokazać go na zweryfikowanym zdjęciu aparatu Ani,
2. zaznaczyć dokładnie element,
3. wyjaśnić prostym językiem, gdzie jest i co nim zrobić,
4. dopiero potem utrwalać nazwę techniczną.

Ta zasada obowiązuje wszystkie kolejne lekcje.

## Co pozostaje bez zmian
- styl i kolorystyka aplikacji są zaakceptowane,
- ikona pozostaje,
- ten sam prywatny Canon RP Site,
- nie tworzyć nowej aplikacji ani nowej identyfikacji,
- nie rozszerzać zakresu tej rundy o nowe funkcje.

## Po wdrożeniu
1. Opublikować poprawki do tego samego Site.
2. Sprawdzić na iPhonie 15 Pro Max.
3. Jeżeli wynik jest dobry, zamknąć L1-01/L1-02 jako wzorzec implementacyjny.
4. Przejść do redagowania kolejnych lekcji.

## Standard kolejnych lekcji
Każda kolejna lekcja ma uwzględniać powyższe drobne zasady UX i dydaktyczne od samego początku.

Treść techniczna ma być oparta na zatwierdzonych materiałach źródłowych. Jeśli czegoś nie wiemy albo źródła nie wystarczają, nie zgadujemy: wykonujemy research internetowy, w pierwszej kolejności w oficjalnych materiałach Canon, weryfikujemy z aparatem/menu Ani i dopiero potem zatwierdzamy treść.

## Punkt zatrzymania dla Codexa
Po implementacji i lokalnej weryfikacji raportować wynik. Publikacja ma trafić wyłącznie do istniejącego Site; nie tworzyć nowego Site.


## Instrukcja startowa dla Codexa — wdrożenie korekt

Pracować w istniejącym checkoutcie aplikacji:
`/Users/pawelsiedleczka/.codex/.chatgpt-projects/g-p-6aabf9b9dd848191b1f8a77f4f9213d0/canon-rp-app`

Przed zmianami zsynchronizować lokalną dokumentację `Canon-RP-Kurs` z gałęzią `main`, następnie przeczytać:
1. `docs/19_KOREKTY_WZORCA_2026-09-27.md`,
2. zaktualizowane `docs/L1-01_ROBIE_SWOJE_PIERWSZE_ZDJECIE.md`,
3. zaktualizowane `docs/L1-02_SPRAWDZAM_CZY_ZDJECIE_JEST_OSTRE.md`,
4. `docs/L1-02_KARTA_WIZUALNO_PRODUKCYJNA.md`,
5. `docs/16_ASSET_MANIFEST.md`,
6. `docs/15_STANDARD_PRODUKCJI_LEKCJI.md`.

Wdrożyć wyłącznie pakiet K-01–K-04, bez zmiany stylu, kolorystyki, ikony, Site ani architektury poza tym, co konieczne.

Po zmianach:
- sprawdzić lokalnie,
- przeszukać renderowaną warstwę użytkową pod kątem `L1-`, `S0`, `V0`,
- sprawdzić L1-01 i L1-02 w szerokości iPhone 15 Pro Max,
- raportować wynik przed publikacją, jeśli lokalny workflow nadal wymaga osobnej zgody na publish.


## Stan po lokalnym odbiorze — 27.09.2026
Paweł sprawdził poprawioną lokalną wersję aplikacji po skorygowaniu faktycznego źródła renderowanych treści i potwierdził: **jest OK**.

K-01–K-04 są zaakceptowane lokalnie.

Następne działania dla Codexa:
1. wykonać commit zmian aplikacji,
2. wykonać push,
3. opublikować do istniejącego Canon RP Site — bez tworzenia nowego Site,
4. podać commit aplikacji i potwierdzenie publikacji,
5. nie zmieniać przy tym stylu, kolorów, ikony ani zakresu.

Po publikacji Paweł wykonuje test na rzeczywistym iPhonie 15 Pro Max. Dopiero po jego pozytywnym wyniku oznaczamy L1-01/L1-02 jako zamknięty wzorzec i rozpoczynamy L1-03.


## KONIEC SESJI 27.09.2026 — obowiązujący punkt startowy następnej sesji

### Stan aplikacji
- K-01–K-04 zostały wdrożone, opublikowane i sprawdzone na iPhonie.
- Po tym teście wykryto dodatkową potrzebę: materiał o odtwarzaniu i materiał o tylnym wybieraku mają być rozdzielone i umieszczone bezpośrednio przy odpowiadających im instrukcjach.
- Codex przygotował lokalnie wspólny mechanizm nakładek na zdjęcia aparatu: procentowe pozycjonowanie, wspólny komponent, obsługa reduced motion.
- Kierunek wspólnego mechanizmu jest właściwy, ale aktualny efekt pulsowania został oceniony jako wizualnie nieakceptowalny / nieprofesjonalny.
- Ta ostatnia mikrokorekta NIE została zaakceptowana do publikacji.
- Nie kontynuować od razu pracy nad animacją ani nie rozpoczynać L1-03.

### Problem procesu
W bieżącej sesji Codex kilkukrotnie wymagał dodatkowej kontroli:
- raportował wykonanie korekt, których nie było w faktycznie uruchomionej aplikacji,
- testy techniczne nie odpowiadały rzeczywistemu efektowi widocznemu w UI,
- użytkownik musiał ręcznie wykrywać rozbieżności.

### Pierwszy krok następnej sesji
**Nie zaczynać od aplikacji. Najpierw przygotować i dodać skill precyzyjnej pracy dla Codexa.**

Wymagania skilla są zapisane w:
- `docs/20_CODEX_PRECISION_SKILL_PLAN.md`
- D-035 w `docs/09_DECISIONS.md`

Skill ma wymuszać:
- pracę ściśle według dokumentacji i zatwierdzonego zakresu,
- weryfikację faktycznie renderowanej aplikacji,
- zakaz zgadywania i samowolnego rozszerzania zadania,
- rozdzielenie raportowania: pliki → testy → podgląd → commit → push → publish,
- profesjonalny standard wykonania,
- zatrzymanie i zgłoszenie problemu przy niepewności.

### Kolejność po dodaniu skilla
1. Uruchomić/zweryfikować skill na prostym zadaniu kontrolnym.
2. Wrócić do lokalnej mikrokorekty L1-02.
3. Dopracować styl wskazania elementu aparatu do poziomu profesjonalnego.
4. Obejrzeć lokalny rezultat.
5. Dopiero po akceptacji wykonać commit/push/publish.
6. Sprawdzić na fizycznym iPhonie.
7. Zamknąć L1-01/L1-02 jako wzorzec.
8. Dopiero wtedy rozpocząć L1-03.

### Nadrzędna zasada jakości
Canon RP kurs jest profesjonalnym produktem, którego pierwszą użytkowniczką jest Ania. Prywatny obecny zakres nie uzasadnia rozwiązań „byle działało”.


## AKTUALIZACJA 28.09.2026 — instalacja skilla
Wersje `AGENTS.md` i `canon-rp-precision` zostały zatwierdzone do instalacji.

Źródła:
- `docs/21_AGENTS_MD_DRAFT.md`
- `docs/22_CANON_RP_PRECISION_SKILL_DRAFT.md`

Codex ma:
1. zsynchronizować dokumentację z `main`,
2. utworzyć w rzeczywistym katalogu aplikacji root `AGENTS.md` z treścią dokumentu 21 (bez nagłówka statusowego dokumentacji),
3. utworzyć `.agents/skills/canon-rp-precision/SKILL.md` z treścią właściwego skilla z dokumentu 22,
4. nie zmieniać jeszcze aplikacji,
5. potwierdzić ścieżki i treść instalacji,
6. wykonać test kontrolny protokołu bez commit/push/publish,
7. dopiero po pozytywnym odbiorze testu wrócić do mikrokorekty L1-02.


## AKTUALIZACJA 28.09.2026 — test skilla zaliczony
`AGENTS.md` i `canon-rp-precision` są zainstalowane lokalnie. Test kontrolny został zaliczony bez zmian w aplikacji.

Codex poprawnie wskazał runtime:
- `dist/index.html`
- `dist/lessons.js`
- `dist/app.js`
- `dist/style.css`
- dwa runtime assety L1-02

Przed rozpoczęciem kolejnej edycji należy jeszcze ustalić, czy `dist/` jest kanonicznym źródłem edycji czy wynikiem procesu build. Jeśli jest wynikiem builda, finalne poprawki muszą powstać w źródłach i zostać wygenerowane do `dist/`.

Po tym sprawdzeniu wracamy do niedomkniętej mikrokorekty L1-02: profesjonalny, subtelny sposób wskazywania elementów aparatu i właściwe osadzenie materiałów przy instrukcji.


## AKTUALIZACJA 28.09.2026 — audyt źródła zamknięty
Potwierdzono, że `dist/` jest kanonicznym źródłem aplikacji, a nie artefaktem builda. Nie ma odrębnej warstwy źródłowej ani procesu build.

Od tego momentu nie prowadzimy dalszej karuzeli testów ani audytów bez konkretnego problemu. Następna czynność to bezpośrednia produkcyjna korekta L1-02 w istniejącym mechanizmie runtime.


## AKTUALIZACJA — L1-03 gotowa do finalnego review
Kierunek L1-03 został zaakceptowany i opracowany jako pełny pakiet redakcyjno-produkcyjny.

Przy powrocie właściciela do komputera NIE zaczynać od ponownego researchu ani projektowania lekcji od zera.

Najpierw przeczytać:
- `docs/L1-03_UKLADAM_ZDJECIE_BEZ_ZMIANY_USTAWIEN.md`
- `docs/L1-03_KARTA_WIZUALNO_PRODUKCYJNA.md`
- sekcję L1-03 w `docs/16_ASSET_MANIFEST.md`
- D-040 w `docs/09_DECISIONS.md`

Następnie wykonać krótki finalny review z właścicielem. Po zatwierdzeniu przygotować jednoznaczny prompt/handoff dla Codexa zgodnie z `$canon-rp-precision`.

Do momentu tej akceptacji Codex nie ma implementować L1-03 ani samodzielnie wybierać brakujących assetów.


## HANDOFF PRODUKCYJNY L1-03 — 28.09.2026
L1-03 została zatwierdzona do implementacji.

Źródła obowiązujące:
- `docs/L1-03_UKLADAM_ZDJECIE_BEZ_ZMIANY_USTAWIEN.md`
- `docs/L1-03_KARTA_WIZUALNO_PRODUKCYJNA.md`
- sekcja L1-03 w `docs/16_ASSET_MANIFEST.md`
- `docs/15_STANDARD_PRODUKCJI_LEKCJI.md`
- D-041 w `docs/09_DECISIONS.md`

Codex:
- używa `$canon-rp-precision`,
- nie redaguje treści,
- nie wybiera samodzielnie brakujących assetów,
- implementuje w istniejącym Canon RP Site / istniejącej aplikacji,
- zachowuje styl, kolory, ikonę i wzorzec UX,
- zatrzymuje się po lokalnym podglądzie i raporcie,
- bez commit/push/publish do osobnej akceptacji.


## AKTUALIZACJA — L1-03 lokalnie OK
Właściciel projektu zaakceptował lokalną implementację L1-03.

Nie wracać do redagowania tekstu ani przebudowy UX bez nowej uwagi. Kolejny etap to wyłącznie produkcja brakujących materiałów:
- L1-03-V01,
- L1-03-V02,
- L1-03-V03,
- L1-03-V04A,
- L1-03-V04B,
- L1-03-V05.

V06 jest komponentem UI i został zaimplementowany w ramach lekcji.

Do czasu przygotowania, osadzenia i odbioru powyższych materiałów nie wykonywać finalnego commit/push/publish L1-03.


## HANDOFF KOŃCOWY 28.09.2026 — start nowego wątku

### Co jest zamknięte
- L1-01/L1-02 są wzorcem redakcyjnym i UX.
- Skill `canon-rp-precision` i `AGENTS.md` są zainstalowane i sprawdzone.
- L1-03 jest zredagowana, zatwierdzona, zaimplementowana lokalnie i zaakceptowana pod względem treści oraz przebiegu.
- Nie wracamy do tekstu L1-03 bez nowej konkretnej uwagi.

### Co jest otwarte
Brakuje sześciu materiałów demonstracyjnych L1-03:
- V01 — ten sam przedmiot, prostsze tło po zmianie pozycji,
- V02 — kontrola brzegów kadru,
- V03 — poziomo / pionowo,
- V04A — krok w bok,
- V04B — zmiana wysokości aparatu,
- V05 — rzeczywisty RF 50 mm / stała ogniskowa.

### Co odrzucono
- dalsze generowanie przez AI scen mających udawać rzeczywiste zależności przestrzenne,
- angażowanie Ani w produkcję materiałów, na których dopiero ma się uczyć,
- zatrudnianie zewnętrznego profesjonalnego fotografa jako domyślnego rozwiązania dla kilku zdjęć.

### Pierwszy cel następnej sesji
Wypracować **profesjonalny, wiarygodny i niskokosztowy sposób pozyskania brakujących materiałów L1-03**.

Nie zaczynać od:
- kolejnych grafik generatywnych,
- ponownego researchu treści L1-03,
- zmian w Codexie,
- publikacji.

### Kryteria rozwiązania
Wybrany sposób ma:
1. pokazywać prawdziwe zależności przestrzenne i geometryczne,
2. dawać spójny komplet materiałów,
3. nie wymagać od Ani produkcji kursu,
4. nie wymagać nieuzasadnionych kosztów,
5. nadawać się później również do wersji komercyjnej albo dać się łatwo wymienić na wersję komercyjną.

### Po rozwiązaniu problemu
pozyskanie assetów → osadzenie w L1-03 → lokalny odbiór → commit/push/publish → test na iPhonie.

## HANDOFF 29.09.2026 — przejście na Claude i jedno repozytorium (D-047)

### Co zostało wykonane
- Codex i ChatGPT zakończyły udział w projekcie. Paweł podejmuje decyzje końcowe, Claude w czacie jest architektem i audytorem, Claude Code implementuje.
- Kod aplikacji przeniesiono z historią zmian do `app/` (import commita `3368372`). Zgodność potwierdzono identycznym drzewem Git i sumami SHA-256 wszystkich plików.
- Niezapisaną pracę (mikrokorekta L1-02 i lokalna implementacja L1-03) zapisano na gałęzi `wip/l1-02-l1-03` (commit `7b4cabc`). Gałąź `main` zawiera ostatni zatwierdzony stan aplikacji.
- Kopie zapasowe obu dawnych folderów są na komputerze właściciela w `~/Backups/canon-rp-2026-09-29/`.
- Dawny folder aplikacji w katalogu Codexa jest zamrożonym archiwum.
- Zainstalowano `AGENTS.md`, `CLAUDE.md` i skill `canon-rp-precision` dla Claude Code. Test w nowej sesji zaliczony.
- Zapisano zasadę źródeł treści D-048.
- Repozytorium jest tymczasowo publiczne.

### Co jest otwarte
1. Materiały demonstracyjne L1-03: V01, V02, V03, V04A, V04B, V05. Obowiązują ograniczenia z D-043–D-046. To główna blokada postępu kursu.
2. Mikrokorekta L1-02 na gałęzi WIP: rozdzielić od L1-03. Zmienia też wygląd L1-01, więc wymaga odbioru obu lekcji przez właściciela.
3. W danych L1-03 na gałęzi WIP pola statusu zawierają zbędne znaki — do poprawy przy osadzaniu materiałów.
4. Hosting i sposób publikacji — decyzja przed najbliższą publikacją. Obecna wersja na ChatGPT Sites działa bez zmian; nie ustalono, jak publikować bez narzędzi OpenAI.
5. Testy Playwright i `app/README.md` zawierają ścieżki z dawnego folderu Codexa — do uporządkowania przy najbliższej pracy nad testami.
6. Przy pierwszej nowej lekcji sprawdzić w praktyce standard pracy ze źródłami z D-048.

### Pierwszy cel następnej sesji
Wypracować sposób pozyskania materiałów L1-03 (punkt 1).
