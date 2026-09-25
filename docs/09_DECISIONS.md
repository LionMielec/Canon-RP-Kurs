# Canon RP kurs — DECISIONS

Stan na: 2026-09-24

Ten plik jest bieżącym rejestrem zatwierdzonych decyzji projektowych. Dokument `Canon-RP-kurs-REVIEW-BEFORE-CODEX-v4.md` oraz obowiązujący handoff pozostają źródłami szczegółowego kontekstu.

## D-001 — Cel projektu
Zatwierdzone: prywatny, niekomercyjny kurs dla Ani dotyczący Canon EOS RP i praktycznej fotografii; start od poziomu początkującego.

## D-002 — Forma produktu
Zatwierdzone: aplikacja webowa mobile-first, z iPhone 17 Pro Max jako głównym urządzeniem referencyjnym; interfejs responsywny również na tablet i komputer.

## D-003 — Zakres kursu
Zatwierdzone: jeden system łączący obsługę Canon EOS RP z praktyczną nauką fotografii. Aparat jest narzędziem, fotografia celem.

## D-004 — Język i sposób tłumaczenia
Zatwierdzone: język polski, prosty i naturalny; najpierw efekt lub sytuacja, potem wyjaśnienie, na końcu termin fachowy.

## D-005 — Sposób nauki
Zatwierdzone: nauka sytuacyjna, wizualna, praktyczna i krok po kroku; rytm: zobacz → ustaw → zrób zdjęcie → sprawdź efekt → porównaj → popraw → spróbuj ponownie.

## D-006 — Poziomy kursu
Zatwierdzone: jedna ciągła ścieżka: początkujący → średnio zaawansowany → zaawansowany → ewentualne specjalizacje.

## D-007 — Materiały z rzeczywistego Canon EOS RP
Zatwierdzone: podstawą wizualną i techniczną są zdjęcia konkretnego aparatu Ani, rzeczywiste ekrany menu, zaakceptowane materiały projektowe i oficjalna dokumentacja Canona. Nie wolno zgadywać wyglądu ani działania aparatu i menu.

## D-008 — Wizualizacje i 3D: zasady użycia
Zatwierdzone:

- wizualizacja ma przede wszystkim uczyć, a nie ozdabiać,
- animację stosujemy wtedy, gdy czytelniej pokazuje gdzie wykonać działanie, co nacisnąć, co przekręcić lub co powinno pojawić się na ekranie,
- podstawą odwzorowania jest rzeczywisty Canon EOS RP Ani; nie wolno wymyślać elementów aparatu,
- można stosować m.in. zbliżenia, obrót aparatu, podświetlenia, wskazania kierunku obrotu, wskazania miejsca dotknięcia i przejścia od całego aparatu do konkretnego elementu,
- rzeczywiste menu musi pochodzić z aparatu Ani; animacja może jedynie wskazywać kroki i zaznaczać elementy,
- materiały 3D są osobnymi zasobami lekcji i Codex ma je implementować, a nie wymyślać,
- 3D nie jest obowiązkowe w każdej lekcji; prostsze materiały mają pierwszeństwo, jeśli równie dobrze wyjaśniają temat,
- Higgsfield jest preferowanym obecnie narzędziem produkcyjnym, ale nie jest twardą zależnością aplikacji ani jedynym dozwolonym narzędziem.

## D-009 — Wizualizacje i 3D: pipeline produkcyjny i odpowiedzialność
Zatwierdzone:

1. W ChatGPT powstaje zatwierdzona treść lekcji oraz decyzja, jaka wizualizacja jest potrzebna i czemu ma służyć.
2. Określamy dokładnie potrzebne zdjęcia aparatu Ani, ekrany menu i inne materiały źródłowe.
3. Na podstawie zweryfikowanych materiałów powstaje storyboard / precyzyjna instrukcja wykonania grafiki lub animacji.
4. Materiał jest produkowany w Higgsfield albo w innym zaakceptowanym narzędziu odpowiednim do danego zadania.
5. Gotowy materiał jest sprawdzany pod kątem zgodności z rzeczywistym Canon EOS RP Ani, prawidłowości pokazywanej czynności i zgodności z treścią lekcji.
6. Właściciel projektu zatwierdza materiał przed implementacją.
7. Zatwierdzony materiał trafia do `assets/` z jasnym przypisaniem do konkretnej lekcji i miejsca użycia.
8. Codex osadza materiał w aplikacji i odpowiada za jego techniczne działanie, responsywność i integrację z lekcją.

Codex nie produkuje samodzielnie finalnych animacji 3D i nie zleca ich automatycznie zewnętrznym narzędziom. Może zgłaszać potrzeby techniczne, ograniczenia formatu, problemy z wydajnością i propozycje sposobu osadzenia, ale produkcja i zatwierdzanie materiałów wizualnych pozostają częścią procesu projektowego w ChatGPT z właścicielem projektu.


## D-010 — Hierarchia form wizualizacji w aplikacji
Zatwierdzone:

1. Zdjęcie lub rzeczywisty ekran menu jest formą podstawową, gdy wystarcza do jasnego wskazania elementu lub kroku.
2. Gotowa krótka animacja 3D / animowany materiał jest formą preferowaną tam, gdzie ruch, obrót, zbliżenie lub wskazanie kierunku lepiej tłumaczy czynność.
3. Rzeczywiste interaktywne 3D stosujemy wyjątkowo, tylko gdy interakcja daje konkretną wartość edukacyjną niedostępną w prostszej formie.

Nie tworzymy interaktywnego modelu 3D całego Canon EOS RP jako obowiązkowej podstawy kursu. Obowiązuje zasada: **najprostsza forma, która skutecznie uczy; bardziej złożone 3D tylko wtedy, gdy realnie poprawia zrozumienie.** Rozwiązanie ma pozostać lekkie i wygodne przede wszystkim na iPhone 17 Pro Max Ani.


## D-011 — Analiza zdjęć przez AI: tryb związany z ćwiczeniem
Zatwierdzone:

- AI analizuje zdjęcie w kontekście konkretnej lekcji lub ćwiczenia i zna cel zadania,
- analiza skupia się przede wszystkim na celu ćwiczenia, nie na pełnej krytyce fotografii,
- do modelu mogą trafić: zdjęcie, identyfikator lekcji/ćwiczenia, cel zadania, zakres wiedzy już poznanej przez Anię oraz dostępne metadane zdjęcia,
- agent najpierw ocenia, czy cel ćwiczenia został osiągnięty, bez arbitralnej skali punktowej,
- odpowiedź ma prowadzić schematem: co wyszło dobrze → jedna najważniejsza rzecz do poprawienia → dlaczego → co zrobić na Canon EOS RP → kolejna próba,
- AI nie może zgadywać parametrów ani twierdzić, że zna ustawienia, których nie da się potwierdzić,
- AI nie powinno wyprzedzać programu kursu i ma bazować głównie na tym, czego Ania już się nauczyła,
- analiza ma być krótka, praktyczna i zadaniowa.

Zasada nadrzędna: **AI nie ocenia zdjęcia ogólnie „czy jest dobre”; sprawdza, czy Ania osiągnęła cel konkretnego ćwiczenia, wyjaśnia wynik i prowadzi do następnej próby.**

Otwarte po D-011: zakres i sposób działania osobnej funkcji „Przeanalizuj moje zdjęcie” poza konkretną lekcją.

## D-012 — AI ma tłumaczyć każdą poradę na konkretne działanie
Zatwierdzone:

- AI nie może kończyć ważnej wskazówki na skrócie lub fachowym zaleceniu, które początkująca osoba musi sama przełożyć na działanie,
- przy każdej kluczowej poprawce agent ma wyjaśnić: **co Ania ma zrobić fizycznie, co ma ustawić na Canon EOS RP (jeśli to potrzebne), gdzie ma to znaleźć oraz jaki efekt powinna zobaczyć**,
- zalecenia dotyczące kadru, odległości, ustawienia osoby lub sceny mają być opisane jako proste czynności do wykonania,
- zalecenia dotyczące aparatu mają być podawane w granicach materiału już poznanego w kursie i w formie prostej ścieżki działania,
- agent preferuje jedną najważniejszą, wykonalną poprawkę na kolejną próbę zamiast wielu ogólnych porad.

Zasada nadrzędna: **każda porada AI ma odpowiadać Ani na pytanie „co dokładnie mam teraz zrobić?”.**


## D-013 — Funkcja „Pokaż mi jak” w analizie AI
Zatwierdzone:

- przy poradzie AI może być dostępna funkcja **„Pokaż mi jak”**,
- funkcja prowadzi do zweryfikowanego materiału kursu pokazującego wykonanie zalecenia na Canon EOS RP albo w scenie fotograficznej,
- materiałem może być fragment lekcji, zatwierdzone zdjęcie aparatu, rzeczywisty ekran menu, zatwierdzona animacja/3D lub krótka instrukcja krok po kroku,
- „Pokaż mi jak” nie może generować ad hoc wyglądu aparatu, menu ani przebiegu czynności; korzysta z zatwierdzonych zasobów projektu,
- jeśli właściwy materiał nie istnieje, brak ma zostać zgłoszony do uzupełnienia zamiast tworzenia zastępczego materiału z domysłu,
- funkcja łączy analizę AI bezpośrednio z nauką w kursie: od „co poprawić” do „jak dokładnie to zrobić”.

## D-014 — Osobna funkcja „Przeanalizuj moje zdjęcie” — kierunek
Zatwierdzone:

- funkcja działa także poza konkretnym ćwiczeniem kursu,
- AI analizuje zdjęcie szerzej, ale nadal w odniesieniu do wiedzy i umiejętności już poznanych przez Anię,
- agent nie powinien wyprzedzać kursu ani zasypywać Ani tematami, których jeszcze nie zna,
- funkcja ma prowadzić do jednej najważniejszej, praktycznej poprawki i może korzystać z „Pokaż mi jak”,
- szczegółowy ekran, przebieg i porównywanie kolejnych prób pozostają do dopracowania.

## D-015 — Porównanie kolejnych prób „przed” i „po”
Zatwierdzone:

- po wskazówce AI i wykonaniu kolejnego zdjęcia aplikacja ma traktować zdjęcie wcześniejsze, udzieloną wskazówkę i nową próbę jako jedną serię nauki,
- AI ma porównywać zdjęcie „przed” i „po” przede wszystkim pod kątem konkretnej zmiany, nad którą Ania właśnie pracowała, a nie wykonywać od nowa pełną krytykę fotografii,
- wynik porównania ma prostym językiem wyjaśniać: **co konkretnie się zmieniło, czy zastosowana wskazówka przyniosła oczekiwany efekt oraz co zrobić dalej**,
- AI nie ma używać ogólnego werdyktu „drugie zdjęcie jest lepsze/gorsze”; ma odnosić się do celu danej poprawki,
- jeśli poprawa jest częściowa, agent ma to jasno powiedzieć i zaproponować jedną kolejną, wykonalną korektę,
- jeśli warunki między zdjęciami zmieniły się tak bardzo, że nie da się wiarygodnie przypisać różnicy zastosowanej wskazówce, AI ma to zakomunikować i nie zgadywać przyczyny,
- seria może obejmować więcej niż dwie próby, np. zdjęcie 1 → wskazówka → zdjęcie 2 → korekta → zdjęcie 3, tak aby Ania mogła zobaczyć postęp w czasie.

Zasada nadrzędna: **porównanie kolejnych prób ma być elementem pętli uczenia, a nie osobną oceną zdjęcia: wskazówka → nowa próba → porównanie efektu → następny krok.**


## D-016 — Rozpoczęcie przekazania projektu do Codexa
Zatwierdzone:

- nie czekamy z rozpoczęciem implementacji do przygotowania całego kursu; Codex może zacząć budowę na zatwierdzonych fundamentach projektu,
- przed właściwym kodowaniem domykamy punkt 9 do poziomu gotowego do implementacji, definiujemy zakres MVP i minimalne decyzje techniczne potrzebne do startu,
- nowy handoff dla Codexa ma być przygotowany jako kontynuacja wcześniejszego przekazania, a nie jako nowy projekt od zera,
- przy przygotowaniu handoffu trzeba uwzględnić materiały i wiedzę, które Codex już wcześniej otrzymał, w szczególności istniejące dokumenty projektu takie jak `AGENTS.md`, `README.md`, `DECISIONS.md`, `PROJECT_SCOPE.md`, `CONTENT_MAP.md`, `ARCHITECTURE.md`, `ASSET_REQUIREMENTS.md`, `AI_PHOTO_REVIEW.md`, `STATUS.md` i `CODEX_START_PROMPT.md`,
- nie wolno tworzyć równoległych, sprzecznych instrukcji; przed wdrożeniem nowego pakietu należy porównać go z aktualnym stanem projektu Codexa i jasno oznaczyć, które dokumenty są nadrzędne i które ustalenia zastępują wcześniejsze wersje,
- Codex pozostaje wykonawcą technicznym: ma implementować zatwierdzone decyzje, treści i materiały, a nie samodzielnie zmieniać kierunek produktu,
- nowe zdjęcia Ani mają zostać włączone do procesu jako zweryfikowane materiały źródłowe projektu po ich przeglądzie i przypisaniu do konkretnych potrzeb lekcji/UX.

Zasada nadrzędna: **przejście do implementacji ma być kontrolowanym handoffem istniejącego projektu, z zachowaniem ciągłości wiedzy i bez resetowania wcześniejszego kontekstu Codexa.**

## D-017 — Nadrzędny priorytet edukacyjny kursu
Zatwierdzone:

- głównym celem kursu jest nauczenie Ani robienia zdjęć ze zrozumieniem przy użyciu jej Canon EOS RP,
- rdzeniem produktu są pełne treści edukacyjne łączące praktyczną obsługę aparatu z nauką fotografowania,
- każda lekcja ma prowadzić od konkretnego efektu lub sytuacji fotograficznej do właściwej obsługi aparatu, wykonania zdjęcia, sprawdzenia rezultatu i świadomej korekty,
- treść kursu, ćwiczenia, źródła merytoryczne, rzeczywiste materiały aparatu i menu mają pierwszeństwo przed funkcjami AI, efektami wizualnymi i dodatkami technicznymi,
- aplikacja jest sposobem wygodnego prowadzenia Ani przez naukę; nie jest celem samym w sobie,
- AI pozostaje funkcją wspomagającą: może pomagać w analizie zdjęć, kierować do właściwych materiałów i wspierać kolejne próby, ale nie może wyznaczać głównej struktury ani priorytetów kursu,
- Codex ma implementować zatwierdzoną treść edukacyjną i UX; nie ma zastępować procesu tworzenia programu i lekcji.

Zasada nadrzędna: **najpierw uczymy Ani świadomie fotografować Canonem EOS RP; technologia, AI i wizualizacje mają wyłącznie wspierać ten cel.**

## D-018 — L1-01 „Robię swoje pierwsze zdjęcie” — zatwierdzona baza lekcji
Zatwierdzone:

- L1-01 pozostaje pierwszą lekcją Poziomu 1,
- pełna wersja przygotowana 24.09.2026 jest przyjęta jako baza treści lekcji,
- celem lekcji jest wykonanie pierwszego świadomego zdjęcia w trybie A+, z rozróżnieniem dwóch etapów naciskania spustu migawki i oczekiwaniem na wizualne potwierdzenie ustawienia ostrości przed wykonaniem zdjęcia,
- ćwiczenie obejmuje trzy powtórzenia tego samego prostego cyklu: wyceluj → naciśnij spust do połowy → zobacz potwierdzenie ostrości → dociśnij spust do końca,
- pierwsza lekcja nie jest oprowadzaniem po całym aparacie; kontrola akumulatora, karty i gotowości sprzętu jest warunkiem startowym, a nie główną treścią dydaktyczną,
- główna ścieżka korzysta z tylnego ekranu; nauka wizjera może zostać wprowadzona później,
- L1-01 kończy się przygotowaniem do L1-02, w której Ania będzie sprawdzać ostrość wykonanego zdjęcia.

Zasada: **pierwsza lekcja ma od początku budować prawidłowy nawyk świadomego wykonania zdjęcia, a nie tylko nauczyć naciskania spustu.**


## D-019 — Notatki wizualno-produkcyjne dla każdej lekcji
Zatwierdzone:

- każda pełna lekcja ma mieć osobną sekcję roboczą przeznaczoną dla zespołu projektowego, niewidoczną jako zwykła treść dla Ani,
- sekcja ma wskazywać dokładnie, **gdzie w lekcji** potrzebny jest materiał wizualny, **jaki ma mieć format** oraz **czemu ma służyć dydaktycznie**,
- dopuszczalne formaty obejmują przede wszystkim: rzeczywiste zdjęcie aparatu Ani, rzeczywisty ekran/menu aparatu, prostą grafikę objaśniającą, krótką animację, animację/ujęcie 3D oraz porównanie zdjęć,
- dla każdego materiału zapisujemy: miejsce użycia w lekcji, cel edukacyjny, wymagane źródło, preferowaną formę, opis ujęcia/animacji oraz status: istnieje / trzeba przygotować / trzeba sfotografować / do weryfikacji,
- materiał wizualny nie może być dekoracyjny; ma pokazywać konkretną czynność, element aparatu, zmianę efektu na zdjęciu albo różnicę, którą Ania ma zauważyć,
- ostateczny dobór zdjęcia, grafiki lub animacji następuje podczas opracowywania konkretnej lekcji, a nie zbiorczo „na zapas”.

Zasada nadrzędna: **treść i warstwa wizualna powstają równolegle; każda lekcja ma od razu określać, co Ania ma zobaczyć w kluczowych momentach nauki.**


## D-020 — Struktura lekcji i materiałów dla implementacji w Codexie
Zatwierdzone:

- każda pełna lekcja ma być przygotowywana jako uporządkowany pakiet treści, a nie jako sam tekst,
- pakiet lekcji ma rozdzielać treść widoczną dla Ani od notatek produkcyjnych dla projektu,
- każdy istotny fragment lekcji ma mieć stały identyfikator sekcji/kroku, aby Codex mógł jednoznacznie osadzić właściwy materiał w odpowiednim miejscu,
- każdy materiał wizualny ma być opisany co najmniej przez: identyfikator, miejsce użycia, typ materiału (zdjęcie / ekran / grafika / animacja / 3D), cel dydaktyczny, źródło, status oraz powiązanie z konkretnym krokiem lekcji,
- Codex nie może samodzielnie zgadywać, gdzie umieścić materiał ani zmieniać jego roli edukacyjnej; implementuje przypisania wynikające z zatwierdzonego pakietu lekcji,
- jeżeli materiał nie jest jeszcze gotowy, w pakiecie pozostaje jawny placeholder produkcyjny z opisem czego brakuje, zamiast zastępowania go przypadkową grafiką lub wygenerowanym odpowiednikiem,
- układ danych ma umożliwiać późniejszą wymianę zdjęcia, grafiki lub animacji bez przebudowy treści lekcji,
- kolejność ekranów i elementów interaktywnych w aplikacji ma wynikać ze struktury lekcji i jej kroków, a nie z osobnych decyzji implementacyjnych Codexa.

Zasada nadrzędna: **ChatGPT + właściciel projektu określają treść, kolejność i rolę materiałów; Codex składa z tego aplikację zgodnie z jednoznacznym planem lekcji.**


## D-021 — Gotowy materiał dydaktyczny przed ćwiczeniem Ani
Zatwierdzone:

- Ania otrzymuje gotowy kurs z gotowymi przykładami dydaktycznymi; nie uczestniczy w produkcji materiałów, na których ma się dopiero uczyć,
- gdy nowy temat wymaga przykładu wizualnego, kolejność jest następująca: gotowy materiał wzorcowy w kursie → wyjaśnienie, na co patrzeć → pokaz obsługi Canon EOS RP, jeśli potrzebny → ćwiczenie Ani na własnych zdjęciach,
- własne zdjęcia Ani są materiałem ćwiczeniowym i rozwojowym, a nie obowiązkowym źródłem podstawowej demonstracji,
- materiały wzorcowe przygotowują autorzy kursu wcześniej, z wykorzystaniem własnych zweryfikowanych materiałów, rzeczywistego aparatu lub legalnych i sprawdzonych źródeł zewnętrznych,
- przy źródłach zewnętrznych zapisujemy pochodzenie i licencję w manifeście assetów,
- rzeczywiste zdjęcia egzemplarza Ani pozostają podstawą do pokazywania fizycznej obsługi jej aparatu.

Zasada nadrzędna: **najpierw gotowy przykład i zrozumienie, potem samodzielne ćwiczenie Ani.**

## D-022 — L1-02 „Sprawdzam, czy zdjęcie jest ostre” — zatwierdzona
Zatwierdzone 25.09.2026:

- L1-02 pozostaje drugą lekcją Poziomu 1,
- kolejność dydaktyczna: gotowy wzorzec → wyjaśnienie, na co patrzeć → obsługa odtwarzania i powiększenia na EOS RP → ćwiczenie na własnych zdjęciach z L1-01,
- wzorzec V01 zostaje uproszczony do dwóch przykładów: ważny element ostry / ostrość przesunięta gdzie indziej,
- S02 wyjaśnia, że mały podgląd utrudnia ocenę drobnych szczegółów, a powiększenie ułatwia ocenę krawędzi i faktury,
- przy porównaniu trzech zdjęć Ania sprawdza ten sam konkretny szczegół,
- lekcja nie wprowadza jeszcze przyczyn nieostrości, ustawień AF, czasu migawki ani głębi ostrości,
- obsługa powiększenia została zweryfikowana z Canon EOS RP Advanced User Guide v1.6, sekcja `Magnifying Images`,
- przed finalną produkcją V04 trzeba zapisać dokładne identyfikatory zdjęcia tyłu i zdjęcia góry egzemplarza Ani.

Zasada nadrzędna: **najpierw Ania uczy się rozpoznać rezultat i sprawdzić go na aparacie; diagnozowanie przyczyn przychodzi później.**
