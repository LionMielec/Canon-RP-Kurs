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
