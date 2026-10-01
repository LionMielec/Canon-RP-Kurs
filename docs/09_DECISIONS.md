# Canon RP kurs — DECISIONS

Stan na: 2026-09-27

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

## D-023 — Zachowanie obecnej identyfikacji wizualnej aplikacji
Zatwierdzone 25.09.2026:

- obecna ikona aplikacji jest właściwa i ma pozostać bez zmian,
- obecna kolorystyka i ogólny kierunek wizualny aplikacji są zaakceptowane,
- implementacja wzorcowych dwóch lekcji ma rozwijać istniejącą aplikację, a nie tworzyć nowej identyfikacji wizualnej,
- aktualizacje mają być publikowane do istniejącego prywatnego Site pod tym samym adresem; nie tworzymy nowej aplikacji ani nowego Site.

Zasada: **zmieniamy treść i strukturę lekcji, nie zaakceptowaną identyfikację wizualną aplikacji.**

## D-024 — Nie blokować prototypu przez niegotowy asset V01/V02
Zatwierdzone 25.09.2026:

- nie zatrzymujemy implementacji i testu dwóch pierwszych lekcji z powodu rozbieżności identyfikatora zdjęcia góry aparatu,
- obecny `camera-top.jpeg` pozostaje roboczym podglądem w wersji testowej,
- nie jest przez to uznany za finalnie zatwierdzony asset,
- finalne źródło, crop i oznaczenia V01/V02 zostaną domknięte później,
- następnym krokiem jest uruchomienie wersji testowej na iPhonie 15 Pro Max i ocena wzorca lekcji.

Zasada: **brak finalnego assetu nie może blokować oceny konstrukcji lekcji, jeżeli jest jawnie oznaczony jako roboczy.**

## D-025 — Jedno źródło dla L1-01 V01/V02
Zatwierdzone 25.09.2026:

- jedynym dozwolonym źródłem dla L1-01-V01 i L1-01-V02 jest `fbe2fd62-e8ab-465b-b340-b6d0b4458622.jpg`,
- Library ID: `libfile_167abe23e1488191ba89b2d851b2155c`,
- `camera-top.jpeg` ani inne zdjęcie nie może być użyte jako finalne źródło tych dwóch assetów,
- z tego jednego mastera przygotowujemy osobno kadr włącznika ON/OFF oraz kadr pokrętła A+.

Zasada: **dla V01/V02 nie wybieramy już między zdjęciami; źródło jest zamknięte.**

## D-026 — Lokalny pakiet źródłowych zdjęć dla Codexa
Zatwierdzone 25.09.2026:

- zdjęcia aparatu i menu przekazane 24.09.2026 mają zostać utrzymywane jako jeden lokalny pakiet źródłowy dostępny dla Codexa,
- z 47 wpisów JPG z tej sesji wyodrębniono 27 unikalnych zdjęć; powtórne kopie nie są potrzebne w pakiecie,
- pakiet zawiera oryginały, manifest z identyfikatorami i sumami SHA-256 oraz kopie materiałów już przypisanych do konkretnych assetów,
- docelowe miejsce na Macu: `/Users/pawelsiedleczka/Documents/ChatGPT/Canon-RP-Kurs/materials/camera-source-pack-2026-09-24/`,
- katalog pozostaje lokalny i jest wykluczony z Git; nie publikujemy prywatnego kompletu zdjęć w repozytorium,
- Codex nie ma wybierać samodzielnie materiałów z pakietu; używa wyłącznie źródeł wskazanych przez ASSET_MANIFEST lub kartę produkcyjną.

Zasada: **dokumentacja wskazuje źródło, a Codex musi mieć fizyczny lokalny plik źródłowy — identyfikator Library nie zastępuje pliku na dysku.**

## D-027 — Jedna runda korekt przed kolejnymi lekcjami
Zatwierdzone 25.09.2026:

- opublikowana wersja L1-01 i L1-02 została sprawdzona na rzeczywistym iPhonie 15 Pro Max,
- ogólny kierunek aplikacji, kolorystyka, ikona i sposób prowadzenia lekcji są akceptowane,
- przed uznaniem tego układu za wzorzec kolejnych lekcji wykonujemy jedną zamkniętą rundę drobnych korekt i uzupełnień,
- w następnej sesji najpierw zbieramy wszystkie zauważone niedociągnięcia, a następnie przekazujemy je Codexowi jako jeden pakiet zmian,
- nie przechodzimy jeszcze do L1-03 ani nie przebudowujemy aplikacji od zera,
- po ponownym pozytywnym teście na iPhonie wzorzec L1-01/L1-02 zostaje zamknięty i dalsza praca ma skupiać się na tworzeniu kolejnych lekcji według tego modelu.

Zasada: **najpierw domykamy wzorzec, potem skalujemy go na kolejne lekcje.**


## D-028 — Domknięcie teorii przed ćwiczeniem
Zatwierdzone 27.09.2026:

- przejście z części wyjaśniającej do ćwiczenia nie może być nagłe,
- przed rozpoczęciem ćwiczenia lekcja ma krótko domknąć to, czego Ania właśnie się nauczyła,
- ekran przejściowy ma jasno zapowiedzieć zmianę trybu pracy, np. „Teraz przejdźmy do ćwiczenia”,
- przycisk prowadzący do ćwiczenia powinien nazywać czynność, np. „Przejdź do ćwiczenia”, zamiast neutralnego „Dalej”, gdy zaczyna się wyraźnie nowy etap lekcji,
- samo ćwiczenie może potem używać krótkich, zadaniowych poleceń.

Zasada: **najpierw krótkie podsumowanie i świadome przejście, dopiero potem zadanie praktyczne.**

## D-029 — Identyfikatory produkcyjne są niewidoczne dla Ani
Zatwierdzone 27.09.2026:

- identyfikatory takie jak `L1-01`, `L1-02`, `S03`, `V04` i podobne służą wyłącznie dokumentacji, danym aplikacji i pracy projektowej,
- nie mogą pojawiać się w widocznej dla Ani treści, etykietach, opisach ani komunikatach interfejsu,
- warstwa użytkowa korzysta wyłącznie z naturalnych nazw: „Lekcja 1”, tytuł lekcji, „Krok 3 z 5”, „Ćwiczenie” itp.

Zasada: **warstwa produkcyjna i warstwa dla Ani są rozdzielone również językowo.**

## D-030 — Każdy używany element obsługi aparatu trzeba pokazać
Zatwierdzone 27.09.2026:

- jeśli lekcja odwołuje się do fizycznego elementu Canon EOS RP, element musi zostać pokazany na zweryfikowanym zdjęciu lub innym zatwierdzonym materiale wizualnym,
- dotyczy to również elementów pozornie oczywistych, np. „tylnego wybieraka”,
- najpierw należy powiedzieć prostym językiem, co to jest i gdzie się znajduje, a dopiero potem używać nazwy technicznej,
- jeśli element służy do konkretnej czynności, materiał wizualny powinien wskazać dokładnie, gdzie nacisnąć, obrócić lub przesunąć,
- dla L1-02 określenia „tylny wybierak” w krokach dotyczących przeglądania i przesuwania powiększonego widoku wymagają odpowiedniego pokazania elementu.

Zasada: **Ania nie ma zgadywać, który element aparatu opisuje tekst.**

## D-031 — Standard jakości kolejnych lekcji i weryfikacja źródeł
Zatwierdzone 27.09.2026:

- obecny styl, kolorystyka i kierunek wizualny aplikacji pozostają zaakceptowane,
- po wdrożeniu bieżących drobnych korekt przechodzimy do redagowania kolejnych lekcji według zamkniętego wzorca,
- każda kolejna lekcja ma uwzględniać także drobne zasady UX i dydaktyczne wykryte podczas testu pierwszych dwóch lekcji,
- treść techniczna powstaje na podstawie zatwierdzonych materiałów źródłowych projektu,
- jeśli potrzebnej informacji brakuje albo istnieje niepewność, nie wolno zgadywać: trzeba wykonać research w internecie, preferując oficjalne materiały Canon, porównać je z aparatem/materialami Ani i dopiero wtedy skorygować lub zatwierdzić treść,
- źródło i wynik istotnej weryfikacji technicznej zapisujemy w dokumentacji lekcji.

Zasada: **dopracowanie szczegółów jest częścią standardu, a nie opcjonalnym etapem kosmetycznym.**


## D-032 — Lokalny odbiór korekt K-01–K-04
Zatwierdzone 27.09.2026:

- po poprawieniu rzeczywistego źródła danych aplikacji Paweł ponownie sprawdził lokalny podgląd,
- korekty K-01–K-04 zostały zaakceptowane wizualnie w wersji lokalnej,
- oznacza to zgodę na przejście do commit/push/publikacji do istniejącego Canon RP Site,
- nie oznacza jeszcze zamknięcia wzorca: po publikacji pozostaje test rzeczywisty na iPhonie 15 Pro Max,
- dopiero pozytywny test wersji opublikowanej zamyka L1-01/L1-02 jako wzorzec implementacyjny i otwiera przejście do L1-03.

Zasada: **lokalna akceptacja pozwala publikować; finalne zamknięcie wzorca następuje po teście opublikowanej wersji na rzeczywistym iPhonie.**


## D-033 — Odbiór po efekcie widocznym dla użytkowniczki
Zatwierdzone 27.09.2026:

- kryterium poprawności wdrożenia jest przede wszystkim efekt widoczny i działający w aplikacji zgodnie z oczekiwaniem właściciela projektu,
- raport techniczny, liczba testów ani informacja „wdrożone” nie zastępują rzeczywistego sprawdzenia interfejsu i przebiegu lekcji,
- materiały wizualne mają być umieszczane bezpośrednio przy tej instrukcji, której dotyczą,
- wskazania elementów aparatu mają prowadzić wzrok subtelnie: miękkie, lekko rozmyte podświetlenie / glow, bez ostrych technicznych ramek, z delikatną pulsacją,
- przed publikacją istotnych korekt należy obejrzeć faktyczny lokalny rezultat; po publikacji sprawdzić go na urządzeniu docelowym.

Zasada: **liczy się to, co Ania faktycznie widzi i jak przez lekcję przechodzi, a nie samo techniczne wykonanie zadania.**


## D-034 — Profesjonalny standard od początku i możliwość komercjalizacji
Zatwierdzone 27.09.2026:

- Canon RP kurs jest obecnie prywatnym kursem dla Ani, ale ma być tworzony od początku w standardzie profesjonalnego produktu,
- „prywatny” nie oznacza „prototypowy”, „tymczasowy” ani „byle działało”,
- jakość merytoryczna, dydaktyczna, UX, warstwa wizualna, kod, architektura, testy i dokumentacja mają być dopracowane od początku,
- projekt ma wspierać ciągły rozwój Ani od poziomu początkującego do zaawansowanego bez zmiany podstawowego modelu nauczania,
- istnieje realna możliwość późniejszego przekształcenia projektu w kurs komercyjny dla innych użytkowników,
- dlatego rdzeń aplikacji, struktura danych lekcji, komponenty i standard produkcji mają być powtarzalne, utrzymywalne i skalowalne,
- nie budujemy jednak dziś funkcji komercyjnych, które nie są potrzebne (sprzedaż, konta klientów, płatności, panel administracyjny itp.),
- każda decyzja implementacyjna powinna spełniać zasadę: **mały zakres teraz, profesjonalna jakość i brak ślepej uliczki na później**.

Zasada nadrzędna: **nie robimy „wersji dla Ani, którą kiedyś trzeba będzie przepisać”; budujemy profesjonalny fundament, którego pierwszą użytkowniczką jest Ania.**


## D-035 — Przed dalszą pracą dodajemy skill precyzyjnej pracy dla Codexa
Zatwierdzone 27.09.2026:

- bieżąca sesja kończy się bez dalszych zmian w aplikacji,
- przed kontynuacją korekt Canon RP kurs Codex ma otrzymać osobny skill/regułę pracy nastawioną na precyzyjne wykonywanie poleceń i ścisłe trzymanie się dokumentacji,
- skill ma ograniczać samowolne interpretowanie zakresu, zgłaszanie zadania jako wykonanego bez sprawdzenia faktycznie renderowanej aplikacji oraz wprowadzanie zmian poza zatwierdzonym zakresem,
- Codex ma odróżniać: zmianę dokumentacji, zmianę źródła aplikacji, lokalny podgląd, test techniczny, akceptację wizualną, commit/push oraz publikację,
- „wykonane” może oznaczać tylko stan rzeczywiście zweryfikowany odpowiednim testem; raport techniczny nie zastępuje sprawdzenia efektu użytkowego,
- przy niejasności, konflikcie instrukcji albo braku pewności Codex ma zatrzymać się i zgłosić problem zamiast zgadywać,
- profesjonalny standard z D-034 pozostaje nadrzędny: skill nie służy do przyspieszania pracy kosztem jakości, lecz do zwiększenia precyzji, przewidywalności i kontroli.

Następna sesja zaczyna się od przygotowania i dodania tego skilla. Dopiero po jego uruchomieniu wracamy do niedomkniętej mikrokorekty L1-02 i później do L1-03.

Zasada: **najpierw ustawiamy Codexa do precyzyjnej, kontrolowanej pracy; dopiero potem kontynuujemy implementację.**


## D-036 — AGENTS.md i canon-rp-precision zatwierdzone do instalacji
Zatwierdzone 28.09.2026:

- przyjęto dwuwarstwowy mechanizm kontroli pracy Codexa: repozytoryjny `AGENTS.md` + skill `canon-rp-precision`,
- `AGENTS.md` zawiera stałe zasady projektu, standard jakości, zakaz zgadywania, zakaz samowolnego rozszerzania zakresu oraz wymóg rozdzielania etapów pracy,
- skill `canon-rp-precision` definiuje obowiązkowy workflow implementacyjny: zakres → źródło runtime → implementacja → faktyczny lokalny podgląd → testy → raport → punkt zatrzymania → osobna zgoda na commit/push/publish,
- definicja „wykonane” wymaga rzeczywistej weryfikacji właściwego etapu, a test automatyczny nie zastępuje odbioru wizualnego,
- obie wersje są zatwierdzone do instalacji w lokalnym projekcie aplikacji Codexa,
- po instalacji należy przeprowadzić mały test kontrolny; dopiero pozytywny wynik otwiera ponowną pracę nad niedomkniętą mikrokorektą L1-02.

Zasada: **najpierw instalacja i test procesu, potem powrót do produkcji aplikacji.**


## D-037 — Test kontrolny protokołu Codexa zaliczony
Zatwierdzone 28.09.2026:

- repozytoryjny `AGENTS.md` i skill `canon-rp-precision` zostały zainstalowane lokalnie w projekcie aplikacji,
- test kontrolny bez zmian w aplikacji został wykonany prawidłowo: Codex rozdzielił zakres, elementy nietykane, źródła runtime, punkt zatrzymania, weryfikację i stan commit/push/publish,
- Codex poprawnie zidentyfikował faktycznie renderowane pliki L1-02 i zatrzymał się bez wprowadzania zmian,
- test nie potwierdził jeszcze automatycznego wykrywania skilla w całkowicie nowej sesji; to pozostaje ograniczeniem do obserwacji,
- przechodzimy do ponownej pracy produkcyjnej nad ostatnią mikrokorektą L1-02.

Dodatkowa zasada jakościowa: przed edycją trzeba odróżnić pliki runtime od kanonicznego źródła edycji. Jeśli `dist/` jest generowane przez build, nie wolno wprowadzać finalnych zmian wyłącznie w artefakcie buildowym.


## D-038 — Widoczność oznaczenia ważniejsza niż animacja
Zatwierdzone 28.09.2026:

- podstawowym celem oznaczenia elementu aparatu jest natychmiastowa i jednoznaczna widoczność wskazywanego elementu,
- oznaczenie ma być wyraźne i czytelne również bez animacji,
- pulsowanie/animacja jest opcjonalnym dodatkiem i nie może być warunkiem czytelności,
- jeśli animacja obniża jakość albo utrudnia uzyskanie profesjonalnego efektu, należy z niej zrezygnować,
- oznaczenie nie może być tak subtelne, że użytkowniczka musi szukać, co zostało wskazane,
- priorytet: czytelność → precyzja wskazania → spójność wizualna → dopiero potem ewentualna animacja.

Zasada: **najpierw ma być dobrze widoczne, dopiero później ewentualnie animowane.**


## D-039 — Statyczne oznaczenia zaakceptowane; przejście do L1-03
Zatwierdzone 28.09.2026:

- finalny kierunek oznaczania elementów aparatu może być statyczny; pulsowanie nie jest wymagane,
- priorytetem pozostaje wyraźne, jednoznaczne i profesjonalne wskazanie właściwego elementu,
- aktualne statyczne oznaczenie zostało zaakceptowane przez właściciela projektu,
- nie wracamy do animacji markerów bez nowej, konkretnej potrzeby dydaktycznej,
- kończymy redakcyjne domykanie wzorca L1-01/L1-02 i przechodzimy do redagowania L1-03,
- L1-03 powstaje według pełnego standardu produkcji lekcji oraz zasady gotowych przykładów przed ćwiczeniem.

Zasada: **widoczne i poprawne statyczne oznaczenie jest wystarczającym standardem; animacja jest opcjonalna.**


## D-040 — Kierunek redakcyjny L1-03 zatwierdzony
Zatwierdzone 28.09.2026:

- właściciel projektu zaakceptował kierunek L1-03 „Układam zdjęcie bez zmiany ustawień”,
- lekcja ma uczyć świadomego kadru bez dokładania nowych ustawień aparatu,
- rdzeń: gotowy przykład → kontrola brzegów i tła → poziomo/pionowo → krok w bok → zmiana wysokości → wyjaśnienie stałej ogniskowej 50 mm → ćwiczenie trzech zdjęć → porównanie,
- ćwiczenie nie ocenia „ładne/brzydkie”; Ania ma wskazać konkretną różnicę i uzasadnić wybór,
- przed implementacją lekcja ma zostać opracowana jako kompletny pakiet: finalny tekst, weryfikacja źródeł, karta wizualno-produkcyjna i asset manifest,
- Codex otrzyma wytyczne dopiero po powrocie właściciela do komputera i ostatecznym review pakietu.

Zasada: **L1-03 rozwija widzenie kadru, nie ustawienia aparatu; gotowe przykłady poprzedzają ćwiczenie Ani.**


## D-041 — L1-03 zatwierdzona do implementacji
Zatwierdzone 28.09.2026:

- finalny przebieg i treść L1-03 „Układam zdjęcie bez zmiany ustawień” zostały zaakceptowane do implementacji,
- obowiązuje kolejność: gotowy przykład → brzegi kadru → poziomo/pionowo → krok w bok → wysokość aparatu → stała ogniskowa 50 mm → podsumowanie → ćwiczenie → porównanie,
- nie wprowadzamy jeszcze reguły trójpodziału, przysłony, rozmywania tła, technicznego wykładu o perspektywie ani nowych ustawień/menu,
- wszystkie materiały demonstracyjne mają być gotowe przed ćwiczeniem Ani,
- Codex implementuje wyłącznie zatwierdzony pakiet i nie wybiera samodzielnie brakujących assetów,
- implementacja ma korzystać z `$canon-rp-precision` i zatrzymać się przed commit/push/publish do odbioru lokalnego.

Zasada: **treść L1-03 jest zatwierdzona; Codex wykonuje implementację, nie redaguje lekcji.**


## D-042 — Lokalna implementacja L1-03 zaakceptowana
Zatwierdzone 28.09.2026:

- właściciel projektu sprawdził lokalną implementację L1-03 i potwierdził: „L1-03 lokalnie OK”,
- układ, kolejność ekranów, treść i przejście do ćwiczenia są zaakceptowane lokalnie,
- sześć brakujących materiałów wizualnych pozostaje jawnie oznaczonych placeholderami i nie zostało zastąpionych materiałami wymyślonymi przez Codexa,
- L1-03 nie jest jeszcze gotowa do publikacji dla Ani, dopóki brakujące materiały demonstracyjne nie zostaną przygotowane, osadzone i odebrane,
- do tego momentu nie wykonujemy finalnego commit/push/publish L1-03.

Zasada: **warstwa tekstowa i UX L1-03 są zamknięte lokalnie; kolejnym etapem jest produkcja i odbiór sześciu materiałów wizualnych.**


## D-043 — Bez dalszych grafik generatywnych dla materiałów dydaktycznych L1-03
Zatwierdzone 28.09.2026:

- nie generujemy dalej w ChatGPT obrazów mających udawać rzeczywiste zmiany położenia aparatu, tła lub perspektywy dla L1-03,
- materiały dydaktyczne L1-03, które mają pokazywać zależności przestrzenne, mają bazować na rzeczywistych zdjęciach wykonanych w kontrolowanej scenie,
- ChatGPT może przygotować dokładny plan ujęć, kolejność, wymagania porównawcze i wskazania redakcyjne, ale nie ma generować finalnych obrazów zastępujących realne fotografie,
- rzeczywiste zdjęcie sprzętu pozostaje obowiązkowe wszędzie tam, gdzie lekcja pokazuje konkretny aparat lub obiektyw Ani,
- proste oznaczenia UI na realnym zdjęciu są dopuszczalne, jeśli nie zmieniają treści fotografii i służą wyłącznie wskazaniu elementu.

Zasada: **dla tematów zależnych od rzeczywistej geometrii i położenia aparatu używamy realnych zdjęć, nie generowanych substytutów.**


## D-044 — Kursant nie produkuje materiałów szkoleniowych
Zatwierdzone 28.09.2026:

- Ania jako kursantka nie wykonuje zdjęć ani innych materiałów, na których dopiero ma się uczyć nowego zagadnienia,
- materiały demonstracyjne kursu muszą być przygotowane wcześniej przez autorów projektu, fotografa/producenta materiałów albo pochodzić z odpowiednio licencjonowanych źródeł,
- zdjęcia Ani mogą służyć wyłącznie jako materiał ćwiczeniowy i rozwojowy po przedstawieniu gotowego przykładu,
- shot list L1-03 jest instrukcją dla producenta materiałów / właściciela projektu / fotografa, nie zadaniem dla Ani,
- przy możliwej przyszłej komercjalizacji materiały muszą mieć jasne pochodzenie i prawa do użycia.

Zasada: **kursant otrzymuje gotowy kurs; nie uczestniczy w produkcji podstawowych materiałów dydaktycznych.**


## D-045 — Materiały L1-03 bez zewnętrznego fotografa
Korekta procesu 28.09.2026:

- przygotowanie kilku materiałów do L1-03 nie uzasadnia zatrudniania zewnętrznego profesjonalnego fotografa,
- materiały może wykonać właściciel projektu samodzielnie, w prostym kontrolowanym setupie domowym, telefonem lub aparatem,
- celem sesji nie jest fotografia reklamowa, tylko prawdziwa i powtarzalna demonstracja jednej zmiennej: położenia aparatu, orientacji albo wysokości,
- profesjonalny standard oznacza poprawną, spójną i wiarygodną demonstrację, a nie kosztowną produkcję,
- ewentualna komercyjna wersja kursu może w przyszłości otrzymać nową sesję zdjęciową, jeśli będzie to ekonomicznie uzasadnione.

Zasada: **najprostsza produkcja, która daje prawdziwy i profesjonalnie czytelny efekt; bez zbędnych kosztów.**


## D-046 — Zatrzymanie pracy nad assetami L1-03 i powrót w nowym wątku
Zatwierdzone 28.09.2026:

- bieżąca sesja kończy się bez dalszej produkcji materiałów wizualnych L1-03,
- generowane obrazy do demonstracji zależności przestrzennych zostały odrzucone jako niewystarczająco wiarygodne,
- nie planujemy kosztownej sesji zewnętrznego fotografa,
- Ania nie produkuje materiałów, na których dopiero ma się uczyć,
- otwarty problem brzmi: jak profesjonalnie, wiarygodnie i niskokosztowo przygotować komplet materiałów demonstracyjnych L1-03,
- następna sesja ma rozpocząć się od rozwiązania tego problemu produkcyjnego, a nie od ponownego redagowania lekcji ani zmian w Codexie.

Zasada: **najpierw ustalamy realistyczny, profesjonalny sposób pozyskania materiałów L1-03; dopiero potem wracamy do implementacji i publikacji.**


## D-047 — Przejście na Claude i jedno repozytorium
Zatwierdzone 29.09.2026:

- Paweł podejmuje decyzje końcowe. Claude w czacie (projekt claude.ai) jest architektem i audytorem. Claude Code implementuje zatwierdzone rozwiązania. Codex i ChatGPT nie uczestniczą dalej w projekcie.
- Kod aplikacji został przeniesiony z historią zmian do `app/` w repozytorium Canon-RP-Kurs. Repozytorium jest jedynym źródłem prawdy dla dokumentacji i kodu.
- Dotychczasowy folder aplikacji w katalogu Codexa jest zamrożonym archiwum: nie jest edytowany ani usuwany. Zakaz tworzenia kopii kodu z dokumentu 13 zostaje zastąpiony tą decyzją.
- Niezapisana praca nad mikrokorektą L1-02 i implementacją L1-03 jest przechowywana na gałęzi `wip/l1-02-l1-03`. Gałąź `main` zawiera ostatni zatwierdzony stan aplikacji.
- Publikacja jest wstrzymana do czasu decyzji o hostingu. Dotychczasowa wersja na ChatGPT Sites pozostaje bez zmian.
- Wyniki testów Codexa w `artifacts/` pozostają lokalnie i są wyłączone z Git.
- Repozytorium jest tymczasowo publiczne, aby ułatwić współpracę z Claude w czacie.

Zasada: **jedno repozytorium, jeden wykonawca, decyzje właściciela.**

## D-048 — Źródła treści lekcji i ćwiczeń
Zatwierdzone 29.09.2026 (uzupełnia D-031):

- Obsługa aparatu: oficjalna instrukcja Canon EOS RP w wersji polskiej i angielskiej. Wersja angielska jest nowsza.
- Jeśli wersje polska i angielska różnią się w opisie funkcji lub działania, rozstrzyga sprawdzenie na aparacie Ani. Do tego czasu informacja jest oznaczona jako niezweryfikowana i nie trafia do lekcji.
- Polskie nazwy menu i przycisków pochodzą z polskiej instrukcji i z rzeczywistych ekranów aparatu Ani, nigdy z własnego tłumaczenia wersji angielskiej.
- Wiedza fotograficzna, lekcje i ćwiczenia opierają się na oficjalnych i sprawdzonych źródłach, przede wszystkim internetowych: materiałach edukacyjnych Canon oraz uznanych wydawcach i instytucjach fotograficznych. Każde źródło musi być autentyczne i sprawdzalne (adres strony, wydawca).
- Każda merytoryczna informacja w lekcji ma wskazane źródło w karcie lekcji. Informacja bez źródła nie trafia do lekcji.
- Nic nie jest wymyślane ani uzupełniane z pamięci. Brak źródła oznacza zatrzymanie i zgłoszenie problemu.
- Standard pracy ze źródłami: przy każdej lekcji Claude Code czyta instrukcje Canon lokalnie i przekazuje dokładne fragmenty z numerami stron (PL i EN). Wyciągi PDF przygotowujemy tylko wtedy, gdy potrzebny jest obraz. Instrukcje i wyciągi nie trafiają do Git.
- Źródła, numery stron i adresy stron są wyłącznie w dokumentacji produkcyjnej (karta lekcji). Nigdy nie trafiają do warstwy widocznej dla Ani: bez numerów stron, adresów, przypisów ani przycisków „źródło” w aplikacji.

Zasada: **żadna informacja w kursie bez sprawdzonego, autentycznego źródła.**

## D-049 — Proces redakcji lekcji w układzie D-047
Zatwierdzone 29.09.2026. Uzupełnia dokumenty 03, 04 i 15 oraz D-048; zmienia D-009 w zakresie produkcji animacji.

Proces jednej lekcji:
1. Zakres — Claude w czacie proponuje cel lekcji, zakres i tematy celowo pominięte, na podstawie programu Poziomu 1. Właściciel zatwierdza (brama 1).
2. Źródła — Claude Code czyta instrukcje Canon PL i EN i przekazuje fragmenty z numerami stron. Claude w czacie wyszukuje oficjalne i sprawdzone źródła internetowe do części fotograficznej. Powstaje tabela źródeł (D-048).
3. Szkic — Claude w czacie pisze lekcję według wzorca L1-01/L1-02 oraz dokumentów 03, 04 i 15. Równolegle powstaje karta produkcyjna z tabelą źródeł, listą materiałów i polem „Kontekst AI”.
4. Autokontrola — przed pokazaniem właścicielowi lekcja przechodzi listę kontrolną z dokumentu 03: każde twierdzenie ma źródło, każdy użyty element aparatu jest pokazany.
5. Przegląd treści — właściciel zatwierdza lub poprawia (brama 2).
6. Sprawdzenie na aparacie — tylko gdy brakuje zdjęcia potrzebnego ekranu menu, gdy instrukcje PL i EN różnią się albo gdy trzeba ustalić wersję firmware. Claude w czacie krótko wskazuje, jakie zdjęcie lub sprawdzenie jest potrzebne; wykonuje je właściciel. Ania nie uczestniczy.
7. Wersja finalna — właściciel zatwierdza (brama 3). Claude Code zapisuje lekcję do dokumentacji; dalej materiały i wdrożenie według dokumentu 15.

Animacje:
- Claude w czacie wskazuje miejsca, w których animacja realnie pomaga, i przygotowuje storyboard oparty na rzeczywistych zdjęciach aparatu Ani. Właściciel zatwierdza storyboard.
- Claude Code produkuje animację w Higgsfield albo innym zaakceptowanym narzędziu, dokładnie według zatwierdzonego storyboardu. Właściciel zatwierdza gotową animację przed osadzeniem w lekcji.
- Animacja nie zmienia wyglądu aparatu ani nie wymyśla jego elementów. Obowiązują D-008, D-010 i D-038.
- Każde płatne użycie Higgsfield wymaga zgody właściciela.
- Zmiana D-009: agent kodujący może produkować animacje, wyłącznie według zatwierdzonego storyboardu i z akceptacją gotowego materiału przez właściciela.

Nauczyciel AI:
- Każda lekcja ma w karcie wypełnione pole „Kontekst AI”: cel ćwiczenia i najwyżej dwa priorytety oceny (dokumenty 04 i 06).

Tryb pracy: jedna lekcja naraz; kolejna dopiero po zamknięciu poprzedniej.

Zasada: **trzy bramy akceptacji właściciela; nic nie trafia do kursu bez jego zgody.**

## D-050 — Zasady pracy Claude w czacie; warunkowe dopuszczenie generowanych scen
Zatwierdzone 30.09.2026. Uzupełnia D-047; zmienia D-043 i D-046 w zakresie generowanych obrazów.

- Zasady pracy Claude w czacie są zapisane w `docs/23_ZASADY_CLAUDE_W_CZACIE.md` i obowiązują w każdej sesji.
- Generowane obrazy są dopuszczalne jako materiał demonstracyjny scen, jeśli spełniają wszystkie warunki:
  - pokazują scenę, a nie sprzęt Ani ani ekrany menu,
  - w serii porównawczej zmienia się tylko jedna zmienna,
  - zgodność z rzeczywistością jest sprawdzona na realnym zdjęciu referencyjnym lub według oficjalnego źródła,
  - narzędzie pozwala na użycie komercyjne, a pochodzenie materiału jest zapisane w karcie lekcji,
  - płatne generowanie wymaga zgody właściciela,
  - gotowy obraz zatwierdza właściciel przed osadzeniem.
- Sprzęt Ani i ekrany menu pozostają wyłącznie rzeczywiste. D-008, D-010, D-038 i D-044 obowiązują bez zmian.
- Decyzja nie wybiera sposobu produkcji materiałów L1-03; ten wybór pozostaje otwarty.

Zasada: **generowana scena tylko wtedy, gdy wiernie pokazuje rzeczywistość; sprzęt Ani i menu zawsze prawdziwe.**

## D-051 — Produkcja materiałów L1-03 metodą renderu 3D
Zatwierdzone 30.09.2026. Realizuje D-050 dla L1-03; zmienia plan produkcji w karcie L1-03 i manifeście 16.

- **V01, V02, V03, V04A i V04B** powstają jako rendery jednej sceny 3D w Blenderze 4.5 LTS, ostatniej oficjalnej wersji dla Maca z procesorem Intel. Każde ujęcie to zmiana położenia tego samego wirtualnego aparatu; zmienia się dokładnie jedna rzecz.
- Wirtualny aparat odwzorowuje Canon RP z obiektywem RF 50 mm: ogniskowa 50 mm i wymiary matrycy według oficjalnych danych Canon.
- Rozmycie tła jest takie samo we wszystkich ujęciach i nie jest efektem pokazywanym w lekcji (karta L1-03).
- Scena powstaje z własnych prostych elementów. Gotowe modele lub tekstury wolno użyć tylko z licencją pozwalającą na użycie komercyjne, zapisaną w karcie lekcji (D-044).
- Skrypty budujące scenę są przechowywane w repozytorium, żeby rendery dało się odtworzyć i poprawiać. Jako skrypty korzystające z Blendera mają licencję GNU GPL. Rendery są własnością projektu.
- **Kolejność:** plan ujęć (akceptacja właściciela) → instalacja Blendera 4.5 LTS z blender.org → jedno ujęcie próbne, para V04A → ocena wiarygodności przez właściciela → pozostałe ujęcia → odbiór każdego materiału przez właściciela.
- Jeśli ujęcie próbne nie będzie wiarygodne, praca się zatrzymuje i wracamy do decyzji. Nie szukamy zamienników.
- **V05:** część A to istniejące zdjęcie obiektywu Ani z pakietu źródłowego, bez widocznych numerów seryjnych (wybiera właściciel). Część B to prosty schemat „dalej/bliżej” rysowany jako grafika.
- Po zatwierdzeniu zostaną zaktualizowane karta L1-03 i manifest 16.

Zasada: **najpierw jedno wiarygodne ujęcie próbne, potem reszta.**

## D-052 — Dwa tryby pracy z Claude Code
Zatwierdzone 30.09.2026. Uzupełnia D-047 i `docs/23`.

- Tryb szybki — zmiany wyłącznie w dokumentacji (`docs/`): zgoda na commit i push jest dawana z góry w poleceniu; Claude Code zapisuje zmiany od razu; Claude w czacie audytuje po fakcie w repozytorium; błędy poprawia kolejny commit. Drobne aktualizacje (TODO, status, handoff) zbierane są w jedno zadanie na koniec sesji.
- Tryb pełny — kod, aplikacja, assety, instalacje, publikacja: punkty zatrzymania, podgląd i odbiór właściciela bez zmian.
- Claude Code zgłasza pracę wykraczającą poza zakres polecenia przed jej wykonaniem.

Zasada: **ostrożność proporcjonalna do ryzyka.**

## D-053 — Lekkie kopie materiałów do przeglądu w repozytorium
Zatwierdzone 01.10.2026. Uzupełnia D-047 i D-052; rozstrzyga punkt 5 handoffu z 30.09.2026.

- Claude w czacie ocenia materiały bezpośrednio w repozytorium. Właściciel nie przekazuje obrazów ręcznie.
- Do repozytorium trafiają wyłącznie lekkie kopie (JPEG, dłuższy bok najwyżej 2000 px) w folderze `review/`: podglądy i rendery materiałów oraz zdjęcia źródłowe aparatu i menu.
- Pełne rendery i oryginalne zdjęcia pozostają lokalnie, bez zmian, poza Git. Instrukcje Canon w PDF nigdy nie trafiają do Git.
- Z kopii usuwa się wyłącznie lokalizację GPS i numery seryjne. Pozostałe dane techniczne zostają.
- Kopia nie może pokazywać numerów seryjnych ani prywatnych szczegółów domu; takie zdjęcie nie trafia do `review/`.
- Przy publicznym repozytorium kopie w `review/` są publiczne.
- Folder `review/` nie jest częścią aplikacji.
- Odbiór materiału przed osadzeniem w lekcji pozostaje decyzją właściciela (D-049–D-051).

Zasada: **Claude w czacie widzi materiały sam; oryginały zostają u właściciela.**

## D-054 — Decyzje o kadrach L1-03
Zatwierdzone 01.10.2026. Uzupełnia D-051.

- Odbicie książki na kubku zostaje.
- Przyjęte kadry: V03-pionowo, V04B-1, V04B-2, V04B-3.
- V01-przed to V04A pozycja 1, a V03-poziomo to V04A pozycja 2; oba są odebrane.
- V01-po: przyjęcie wstrzymane. Po obejrzeniu kadru Claude rekomenduje przysunięcie aparatu bliżej kubka, bo przy lewej krawędzi widać uciętą książkę, a kubek jest wyraźnie mniejszy niż w kadrze „przed”. Decyzja właściciela jest otwarta.
- V02: przebudowa jako wariant sceny — aparat ok. 0,7 m od kubka, książka i pilot bliżej kubka; druga wersja kadru przez mały krok lub obrót aparatu, bez ruszania przedmiotów.

Zasada: **kadr ocenia się w pełnej wielkości, nie z miniatury.**

## D-055 — Tekst kolejnej lekcji równolegle z materiałami poprzedniej
Zatwierdzone 01.10.2026. Zmienia zdanie „Tryb pracy” w D-049.

- Redakcja tekstu następnej lekcji może się zacząć, gdy materiały poprzedniej lekcji są jeszcze w produkcji.
- Niedokończone materiały poprzedniej lekcji pozostają na liście otwartych zadań w docs/10_TODO.md aż do odbioru przez właściciela.
- Pozostała część D-049 bez zmian.

Zasada: **tekst nie czeka na obrazy; obrazy nie znikają z planu.**

## D-056 — Rysunki z instrukcji Canon w lekcjach do użytku prywatnego
Zatwierdzone 01.10.2026. Zmienia D-010 i D-050 w zakresie ekranów menu.

- Kurs jest niekomercyjny i przeznaczony wyłącznie do prywatnego użytku Ani.
- W lekcjach wolno używać rysunków ekranów i aparatu z oficjalnych instrukcji Canon. Źródło (instrukcja i strona) jest zapisane wyłącznie w dokumentacji produkcyjnej i nie jest widoczne w kursie (D-048).
- Rysunki z instrukcji nie trafiają do publicznego repozytorium ani do publicznie dostępnej wersji aplikacji; są przechowywane lokalnie, tak jak instrukcje (D-048).
- Zgodność rysunków z aparatem Ani sprawdza właściciel po powrocie do domu; przy tej okazji ustalana jest wersja oprogramowania aparatu.
- Jeśli kurs miałby stać się publiczny lub komercyjny, rysunki trzeba zastąpić własnymi zdjęciami.

Zasada: **rysunki Canon tylko dla Ani, nigdy publicznie.**

## D-057 — Oznaczanie pochodzenia materiałów
Zatwierdzone 01.10.2026. Uzupełnia D-048 i D-056.

- Każdy materiał w rejestrze `docs/16_ASSET_MANIFEST.md` ma pochodzenie: WŁASNE, RENDER, WOLNA LICENCJA (z autorem i licencją) albo CANON — DO PODMIANY (z instrukcją i numerem strony). Ta sama informacja jest w karcie lekcji. Zgodnie z D-048 nie jest widoczna w kursie.
- Nazwa każdego pliku z instrukcji Canon kończy się na `-canon` przed rozszerzeniem.
- Przy zmianie kursu na publiczny lub komercyjny listę do podmiany daje filtr „CANON — DO PODMIANY” w rejestrze albo wyszukanie „-canon” w projekcie.

Zasada: **każdy obraz ma zapisane pochodzenie; rysunki Canon da się znaleźć jednym wyszukiwaniem.**

## D-058 — Materiały L1-01 i L1-03: decyzje z 01.10.2026
Zatwierdzone 01.10.2026. Uzupełnia D-054 i D-056.

- L1-03 V01-po: aparat przysunięty bliżej kubka, na tej samej wysokości (rekomendacja z D-054 przyjęta).
- L1-01-V04 (pół- i pełne naciśnięcie spustu): na razie rysunek z instrukcji Canon zamiast animacji; animacja pozostaje na później, według D-049.
- L1-01-V06 (łatwy i trudny cel dla ostrości): cztery rendery sceny 3D.
- L1-01-V03 i L1-01-V05: rysunki z instrukcji Canon, zgodnie z D-056.

Zasada: **materiał z tego, co jest dostępne teraz; lepsza wersja później, bez blokowania kursu.**

## D-059 — Nauczyciel AI na modelu Claude
Zatwierdzone 01.10.2026. Zmienia kierunek roboczy z dokumentu 06 (model OpenAI).

- Nauczyciel AI (ocena zdjęć Ani) działa na modelu Claude firmy Anthropic.
- Konkretny model i koszt wybieramy przed budową nauczyciela, po próbie na prawdziwych zdjęciach.
- Dokumenty 06 i 11 (model, zabezpieczenia i limity wydatków opisane dla OpenAI) zostaną przepisane przy integracji.

Zasada: **nauczyciel AI na Claude; szczegóły po próbie na prawdziwych zdjęciach.**
