# Status — historia

Sekcje przeniesione z `docs/17_STATUS.md` (D-068).

## Aktualny stan — 29.09.2026
Projekt przeszedł na nowy układ pracy i jedno repozytorium (D-047). Szczegóły i otwarte zadania: koniec `docs/14_PRZEKAZANIE_SESJI.md`. Sekcje poniżej opisują historię projektu. Tam, gdzie wymieniają ChatGPT lub Codexa jako role, obowiązuje D-047.

## Etap projektu
Dwie pierwsze zatwierdzone lekcje zostały wdrożone, opublikowane i sprawdzone na iPhonie 15 Pro Max. Projekt jest na etapie domknięcia jednej rundy drobnych korekt wzorca implementacyjnego przed rozpoczęciem kolejnych lekcji.

## Nadrzędny priorytet projektu
Głównym celem jest nauczenie Ani robienia zdjęć ze zrozumieniem przy użyciu Canon EOS RP. Rdzeniem projektu są treści edukacyjne łączące naukę fotografii z praktyczną obsługą konkretnego aparatu. Aplikacja, wizualizacje i AI są warstwami wspierającymi i nie mogą wyprzedzać ani zastępować programu, lekcji, ćwiczeń i zweryfikowanych źródeł.

## Zatwierdzone w review
Punkty 1–7 są zamknięte i nie wracamy do ich ponownego ustalania bez wyraźnej decyzji właściciela projektu.

Punkt 8 — Wizualizacje i 3D:
- zasady użycia wizualizacji i 3D: ZATWIERDZONE,
- Higgsfield: preferowane narzędzie, ale bez twardego uzależnienia aplikacji od niego,
- pipeline produkcyjny: ZATWIERDZONY,
- podział odpowiedzialności: ZATWIERDZONY — ChatGPT + właściciel projektu projektują i zatwierdzają; Codex implementuje,
- samodzielna produkcja finalnych animacji przez Codexa: NIEDOZWOLONA,
- hierarchia form wizualizacji w aplikacji: ZATWIERDZONA — zdjęcie/ekran → gotowa animacja 3D → interaktywne 3D tylko wyjątkowo, gdy daje realną wartość edukacyjną.
- Punkt 8: ZAMKNIĘTY.

## Punkt 9 — Analiza zdjęć przez AI
- kierunek funkcji: ZATWIERDZONY,
- tryb analizy zdjęcia powiązany z konkretnym ćwiczeniem: ZATWIERDZONY,
- zasada: AI sprawdza realizację celu ćwiczenia, nie wystawia ogólnej oceny zdjęcia,
- zakres kontekstu przekazywanego do modelu: ZATWIERDZONY na poziomie koncepcyjnym,
- zakaz zgadywania parametrów i wyprzedzania kursu: ZATWIERDZONY,
- osobna funkcja „Przeanalizuj moje zdjęcie” poza konkretnym ćwiczeniem: KIERUNEK ZATWIERDZONY, szczegóły przebiegu do doprecyzowania,
- sposób formułowania porad przez AI: ZATWIERDZONY — każda kluczowa rada musi być przełożona na konkretne czynności, ustawienia i oczekiwany efekt; agent ma odpowiadać na pytanie „co dokładnie mam teraz zrobić?”.
- funkcja „Pokaż mi jak”: ZATWIERDZONA — porada AI może prowadzić bezpośrednio do zweryfikowanego materiału kursu pokazującego, jak wykonać zalecenie; bez generowania aparatu/menu z domysłu.
- porównywanie kolejnych prób „przed” i „po”: ZATWIERDZONE — aplikacja tworzy serię nauki powiązaną z konkretną wskazówką AI; agent wyjaśnia, co się zmieniło, czy wskazówka zadziałała i jaki jest następny krok, bez ogólnego werdyktu „lepsze/gorsze” i bez zgadywania przyczyn. Seria może obejmować więcej niż dwie próby.

## Poziom 1 — zatwierdzone lekcje
- **L1-01 „Robię swoje pierwsze zdjęcie” — ZATWIERDZONA baza lekcji.**
- Przyjęty cel: pierwsze świadome zdjęcie w A+, z nauką dwustopniowego naciskania spustu i oczekiwania na wizualne potwierdzenie ostrości.
- Ćwiczenie: trzy powtórzenia tego samego podstawowego cyklu wykonania zdjęcia.
- **L1-02 „Sprawdzam, czy zdjęcie jest ostre” — ZATWIERDZONA 25.09.2026 po korekcie dydaktycznej.**

## Bieżąca runda korekt — 27.09.2026
Paweł zakończył zbieranie uwag po teście pierwszych dwóch lekcji. Do jednego pakietu korekt wchodzą:
1. łagodniejsze przejście z teorii do ćwiczenia: krótkie podsumowanie + jawne „Teraz przejdźmy do ćwiczenia” + odpowiednia etykieta przycisku,
2. usunięcie wszystkich identyfikatorów produkcyjnych typu `L1-02` z warstwy widocznej dla Ani,
3. pokazanie i proste objaśnienie każdego fizycznego elementu aparatu używanego w tekście; w L1-02 dotyczy to m.in. „tylnego wybieraka”.

Styl, kolorystyka, ikona i ogólny kierunek wizualny pozostają zaakceptowane.

## Pakiet wdrożeniowy korekt
- skorygowano źródłową treść L1-01: dodano podsumowanie przed ćwiczeniem i jawne przejście do praktyki,
- skorygowano źródłową treść L1-02: „tylny wybierak” jest najpierw prostym językiem opisany i ma być pokazany,
- zaktualizowano kartę wizualno-produkcyjną L1-02 i manifest assetów,
- przygotowano `docs/archiwum/19_KOREKTY_WZORCA_2026-09-27.md` jako jednoznaczną instrukcję wdrożenia.

## Lokalny odbiór korekt — 27.09.2026
Po pierwszym błędnym raporcie Codexa wykryto, że lokalny podgląd nadal renderował stare treści. Codex skorygował rzeczywiste źródło danych aplikacji. Paweł ponownie sprawdził lokalny podgląd i potwierdził, że korekty K-01–K-04 są prawidłowe.

Lokalna wersja jest zaakceptowana do publikacji. Nie wykonano jeszcze commit/push/publikacji tej rundy w aplikacji.

## Następny krok
Wykonać commit i push zmian aplikacji, opublikować poprawioną wersję do tego samego Canon RP Site, a następnie sprawdzić wersję opublikowaną na rzeczywistym iPhonie 15 Pro Max. Jeżeli wynik jest dobry, formalnie zamknąć L1-01/L1-02 jako wzorzec implementacyjny i przejść do L1-03. Kolejne lekcje powstają ze zweryfikowanych źródeł; brak lub niepewność informacji uruchamia research internetowy z preferencją dla oficjalnych źródeł Canon.

## Pozostałe otwarte decyzje
- konkretny framework webowy,
- hosting i ewentualna domena,
- pełne PWA i zakres pracy offline,
- dokładny zakres MVP,
- model/API do analizy zdjęć,
- sposób przechowywania postępu,
- bezpieczny backend do obsługi AI.

## Warstwa wizualna lekcji
Od L1-01 każda opracowywana lekcja ma równolegle otrzymywać notatki wizualno-produkcyjne: miejsce użycia materiału, jego cel edukacyjny, format (zdjęcie aparatu/menu, grafika, animacja, 3D, porównanie zdjęć), wymagane źródło i status przygotowania. Nie tworzymy zbiorczych assetów na zapas; potrzeby wynikają z konkretnej treści lekcji.


## Struktura produkcyjna lekcji dla Codexa
Od L1-01 każda pełna lekcja ma powstawać jako pakiet zawierający: treść dla Ani, uporządkowane kroki, ćwiczenie, sprawdzenie efektu oraz notatki wizualno-produkcyjne. Materiały wizualne mają być przypisane do konkretnych kroków lekcji przez identyfikatory i opis celu dydaktycznego. Codex ma implementować te przypisania, a nie samodzielnie decydować o rozmieszczeniu lub znaczeniu materiałów. Brakujące assety pozostają oznaczone jako jawne zadania produkcyjne.

## Audyt materiałów L1-01 — 24.09.2026
- audyt istniejącego pakietu zdjęć Ani: ZAKOŃCZONY,
- `L1-01-V01` włącznik: źródło wybrane,
- `L1-01-V02` A+: źródło wybrane,
- `L1-01-V03` prawidłowe trzymanie: brak finalnego materiału — do wykonania,
- `L1-01-V04` pół/pełne naciśnięcie spustu: potrzebny dedykowany close-up/klip i animacja,
- `L1-01-V05` potwierdzenie AF: potrzebne dwa rzeczywiste stany ekranu fotografowania,
- `L1-01-V06` łatwy/trudny cel AF: do przygotowania plansza z czterech prostych przykładów,
- utworzono `/Canon-RP-kurs/docs/ASSET_MANIFEST.md` jako jeden wspólny rejestr assetów dla wszystkich lekcji,
- braki wizualne L1-01 są dokładnie opisane i nie blokują opracowania L1-02.

## L1-02 — historia opracowania 24–25.09.2026
- 24.09 wykonano research techniczny obsługi odtwarzania i powiększania zdjęć na Canon EOS RP.
- Po korekcie dydaktycznej przyjęto zasadę: gotowy przykład → wyjaśnienie → obsługa aparatu → ćwiczenie Ani.
- 25.09 L1-02 została zatwierdzona, wdrożona i opublikowana razem z L1-01.
- Aktualny stan L1-02 jest opisany wyżej w sekcji „Poziom 1 — zatwierdzone lekcje” oraz w najnowszym handoffie.
- Stare robocze statusy typu „do przeglądu” / „niezatwierdzona” nie obowiązują.

## Pakiet źródłowych zdjęć dla Codexa — 25.09.2026
- przygotowano jeden lokalny pakiet materiałów z sesji zdjęciowej 24.09.2026,
- pakiet zawiera 27 unikalnych JPG po usunięciu ponownych kopii,
- dołączono manifest: nazwa, Library ID, wymiary, rozmiar, SHA-256 i znane przypisanie projektowe,
- L1-01-V01/V02 mają w pakiecie jednoznaczny master `fbe2fd62-e8ab-465b-b340-b6d0b4458622.jpg`,
- L1-02-V03 ma master `57652b89-ae48-4cd1-b998-e883aee8aa1f.jpg`,
- pakiet ma zostać rozpakowany lokalnie pod `materials/camera-source-pack-2026-09-24/`; nie trafia do GitHub.

## Publikacja wzorca dwóch lekcji — 25.09.2026
- dwie zatwierdzone lekcje zostały zacommitowane, wypchnięte i opublikowane w istniejącym Canon RP Site,
- commit źródła aplikacji: `651b4f6e746f4a6cffac612812169afc74874545`,
- zachowano ten sam adres Site, ikonę, kolorystykę, konfigurację i dostęp tylko dla właściciela,
- lokalny pakiet zdjęć źródłowych pozostał poza publikowaną aplikacją; opublikowano wyłącznie przygotowane kadry,
- następny krok: test rzeczywisty na iPhonie 15 Pro Max.

## Test na iPhonie 15 Pro Max — 25.09.2026
- pierwsza opublikowana wersja wzorcowych dwóch lekcji została uruchomiona na rzeczywistym iPhonie 15 Pro Max,
- ogólna ocena użytkownika: kierunek i działanie są dobre,
- przed uznaniem implementacji za wzorzec dla kolejnych lekcji pozostaje jedna runda drobnych korekt i uzupełnień,
- do czasu ich domknięcia nie przechodzimy do implementacji L1-03.


## Dodatkowa mikrokorekta po teście na iPhonie — 27.09.2026
Opublikowana wersja działa poprawnie na iPhonie, ale przed formalnym zamknięciem wzorca pozostają dwie korekty prezentacji:
- materiał pokazujący tylny wybierak ma zostać przeniesiony bezpośrednio pod tekst, który instruuje użycie wybieraka,
- wizualne oznaczenia elementów aparatu mają zostać zmiękczone: bez ostrych ramek, z delikatnym rozmyciem/glow i subtelną pulsacją.

Kryterium odbioru: właściciel projektu ma zobaczyć w lokalnym podglądzie dokładnie oczekiwany przebieg i wygląd. Dopiero potem publikujemy i zamykamy wzorzec.


## Standard jakości produktu — 27.09.2026
Ustalono, że prywatny charakter obecnej wersji nie jest podstawą do kompromisów jakościowych. Projekt ma być od początku realizowany profesjonalnie i przygotowany do wielopoziomowego rozwoju kursu.

Możliwa jest późniejsza komercjalizacja dla szerszej grupy użytkowników. Nie wdrażamy teraz infrastruktury komercyjnej, ale rdzeń treści, UX, danych, assetów i kodu nie może być rozwiązaniem jednorazowym wymagającym późniejszego przepisywania z powodu niskiego standardu wykonania.


## Koniec sesji — 27.09.2026, 21:56
Praca nad aplikacją została zatrzymana świadomie przed kolejną publikacją.

Bieżący stan:
- opublikowana wersja K-01–K-04 działa na iPhonie,
- po publikacji wykryto dodatkową korektę rozmieszczenia materiałów w L1-02,
- lokalnie przygotowano wspólny mechanizm wskazywania elementów aparatu,
- obecny efekt pulsowania nie spełnia oczekiwanego profesjonalnego standardu wizualnego i nie został zaakceptowany,
- ostatnia lokalna mikrokorekta nie została opublikowana,
- L1-01/L1-02 nie są jeszcze formalnie zamkniętym wzorcem,
- L1-03 nie została rozpoczęta.

Powód zatrzymania: jakość i przewidywalność pracy Codexa są niewystarczające. Przed dalszą implementacją przygotowujemy skill precyzyjnej pracy zgodnie z D-035 i `docs/archiwum/20_CODEX_PRECISION_SKILL_PLAN.md`.

Pierwszym zadaniem następnej sesji jest przygotowanie i dodanie tego skilla, a nie dalsza edycja aplikacji.


## Start sesji produkcyjnej — 28.09.2026
Zatwierdzono wersję `AGENTS.md` oraz skilla `canon-rp-precision` do instalacji w lokalnym projekcie Codexa.

Następna operacja:
1. zainstalować oba pliki w rzeczywistym projekcie aplikacji,
2. uruchomić mały test kontrolny działania protokołu,
3. po pozytywnym wyniku wrócić do niedomkniętej mikrokorekty L1-02,
4. dopiero potem zamknąć wzorzec i rozpocząć L1-03.


## Test skilla/protokołu — 28.09.2026
Test kontrolny `AGENTS.md` + `canon-rp-precision` zakończony pozytywnie w bieżącej sesji. Codex nie zmienił aplikacji, poprawnie zidentyfikował runtime L1-02 i jawnie rozdzielił zakres, weryfikację oraz stan commit/push/publish.

Otwarte ograniczenie: automatyczne wykrywanie skilla w całkowicie nowej sesji nie zostało jeszcze sprawdzone.

Następny krok: wrócić do produkcyjnej mikrokorekty L1-02. Przed edycją potwierdzić, czy `dist/` jest kanonicznym źródłem aplikacji czy artefaktem buildowym; jeśli artefaktem, edytować właściwe źródła i dopiero z nich odbudować runtime.


## Audyt źródła aplikacji — 28.09.2026
Jednorazowy audyt źródła aplikacji zakończony.

Ustalenie:
- `dist/` jest kanonicznym źródłem aplikacji i jednocześnie katalogiem publikowanym,
- nie istnieje osobna warstwa `src/`, bundler, generator ani proces build,
- `dist/lessons.js`, `dist/app.js`, `dist/style.css` i assety w `dist/assets/` są właściwymi plikami do edycji,
- lokalny serwer jedynie udostępnia te pliki; nie generuje ich.

Nie kontynuujemy dalszej diagnostyki architektury. Następny krok jest produkcyjny: dokończenie ostatniej mikrokorekty L1-02.


## Korekta kierunku oznaczeń — 28.09.2026
Po ocenie lokalnego efektu doprecyzowano problem: główną wadą oznaczenia nie jest brak odpowiedniej animacji, lecz zbyt mała widoczność markera. Dalsza poprawka ma przede wszystkim zwiększyć czytelność i jednoznaczność wskazania. Pulsowanie jest opcjonalne i może zostać całkowicie usunięte, jeśli statyczne oznaczenie daje lepszy profesjonalny efekt.


## Akceptacja markerów i start L1-03 — 28.09.2026
Właściciel projektu zaakceptował statyczny sposób oznaczania elementów aparatu. Pulsowanie nie jest wymagane i nie blokuje dalszej pracy.

L1-01/L1-02 są od tej chwili zamkniętym wzorcem redakcyjnym i UX dla kolejnych lekcji. Ewentualna publikacja ostatniej lokalnej poprawki pozostaje operacją techniczną i nie blokuje redagowania treści L1-03.

Rozpoczęto fazę redakcyjną L1-03 „Układam zdjęcie bez zmiany ustawień”. Treść powstaje w ChatGPT, na podstawie zweryfikowanych źródeł, i wymaga zatwierdzenia przed przekazaniem do Codexa.


## L1-03 — pełny pakiet redakcyjny przygotowany 28.09.2026
Po akceptacji kierunku lekcji przygotowano:
- pełny tekst L1-03 do ostatecznego review,
- zweryfikowane źródła Canon dla stałej ogniskowej 50 mm i podstaw kompozycji,
- pełną kartę wizualno-produkcyjną,
- zaktualizowany asset manifest L1-03,
- kontekst dla późniejszego nauczyciela AI i ograniczenia dydaktyczne.

Nie przekazano jeszcze implementacji do Codexa. Następny etap po powrocie właściciela do komputera: krótki finalny review treści i przekazanie zatwierdzonego pakietu Codexowi.


## L1-03 zatwierdzona do implementacji — 28.09.2026
Właściciel projektu zaakceptował finalny przebieg i treść L1-03. Pakiet jest gotowy do przekazania Codexowi.

Implementacja ma używać `$canon-rp-precision`, zachować zatwierdzony wzorzec L1-01/L1-02, wykorzystać wyłącznie zatwierdzone materiały oraz zatrzymać się na lokalnym podglądzie przed commit/push/publish.


## L1-03 lokalnie zaakceptowana — 28.09.2026
Właściciel projektu przeszedł lokalną implementację L1-03 i zaakceptował jej układ, treść oraz przebieg.

Stan:
- 13 ekranów L1-03 działa lokalnie,
- tekst i UX są zaakceptowane,
- sześć brakujących materiałów wizualnych pozostaje jako jawne placeholdery,
- Codex nie dobrał własnych zamienników,
- commit/push/publish L1-03 nadal wstrzymane.

Następny krok: produkcja sześciu materiałów wizualnych zgodnie z kartą L1-03 i asset manifestem. Po ich osadzeniu wykonujemy krótki odbiór lokalny, a dopiero potem publikację.


## Korekta produkcji wizualnej L1-03 — 28.09.2026
Po próbie generowanych materiałów porównawczych właściciel projektu odrzucił ten kierunek jako niewiarygodny przestrzennie.

Dalsze materiały L1-03 nie będą generowane przez AI. Powstaną z rzeczywistej, kontrolowanej sceny z rośliną w doniczce oraz z rzeczywistych zdjęć sprzętu Ani. Następny krok to przygotowanie precyzyjnego shot listu i wykonanie jednej spójnej sesji zdjęciowej.


## Odpowiedzialność za materiały L1-03 — 28.09.2026
Doprecyzowano, że Ania nie produkuje materiałów demonstracyjnych kursu. Shot list i sesja zdjęciowa są zadaniem produkcyjnym projektu, wykonywanym przez właściciela projektu, fotografa lub innego producenta materiałów. Zdjęcia Ani pojawiają się dopiero jako materiał ćwiczeniowy po gotowej demonstracji.


## Produkcja assetów L1-03 — korekta kosztowa 28.09.2026
Nie planujemy zewnętrznego fotografa. Materiały L1-03 mają powstać w prostej kontrolowanej scenie domowej, wykonanej przez właściciela projektu telefonem lub aparatem. Liczy się prawdziwa geometria sceny i spójność porównania, nie kosztowna produkcja reklamowa.


## Koniec sesji — 28.09.2026, 21:38
Sesja zakończona świadomie na etapie produkcji materiałów wizualnych L1-03.

Stan:
- L1-03 jest lokalnie zaimplementowana i zaakceptowana pod względem treści oraz UX,
- sześć materiałów wizualnych nadal pozostaje do przygotowania,
- kierunek generatywny dla realnych zmian położenia aparatu został odrzucony,
- zewnętrzny profesjonalny fotograf nie jest planowany jako domyślne rozwiązanie ze względu na nieuzasadniony koszt,
- Ania nie wykonuje materiałów demonstracyjnych kursu,
- finalna publikacja L1-03 jest wstrzymana.

Następna sesja, w nowym wątku, zaczyna się od rozwiązania problemu pozyskania profesjonalnych i wiarygodnych materiałów V01–V05 w rozsądnym koszcie. Nie wracamy do redagowania L1-03 ani do kolejnych testów Codexa, dopóki ten problem nie zostanie rozwiązany.
