# Rejestr decyzji

Data bazowa: 17.09.2026. Źródło: rozmowa „Planowanie kursu Canon RP” i polecenie rozpoczęcia dokumentacji oraz repo. Status odróżnia zaakceptowaną koncepcję od propozycji asystenta.

## Ustalone

| ID | Ustalenie | Uzasadnienie |
| --- | --- | --- |
| D-01 | Prywatny, niekomercyjny kurs dla Ani na Canon EOS RP | Konkretny odbiorca i egzemplarz |
| D-02 | Nauka fotografii i aparatu w jednym kursie | Działanie ma prowadzić do efektu na zdjęciu |
| D-03 | Rozwój od podstaw przez średni do zaawansowanego poziomu | Kurs ma rosnąć z umiejętnościami Ani |
| D-04 | Zwykły język na każdym poziomie | Żargon nie ma odstraszać ani utrudniać nauki |
| D-05 | Cel → aparat → ustawienie → efekt → ćwiczenie | Nauka przez praktykę |
| D-06 | Prawdziwe polskie menu i zdjęcia egzemplarza | Zgodność instrukcji z tym, co widzi Ania |
| D-07 | Animacja prowadzi po aparacie; menu pozostaje autentyczne | Czytelność i poprawność instruktażu |
| D-08 | Osobny moduł „Mój nauczyciel / Analiza mojego zdjęcia” | Informacja zwrotna na własnych pracach |
| D-09 | Dane zdjęcia odczytywane programowo; brak danych nie jest zgadywany | Uczciwa analiza i rozróżnienie faktów od hipotez |
| D-10 | Krótka informacja zwrotna bez punktacji, najwyżej dwa zalecenia | Pomoc bez przytłaczania początkującej |
| D-11 | Osobne prywatne repo Canon-RP-Kurs, najpierw dokumentacja | Zachowanie decyzji przed implementacją |
| D-12 | Klucz API poza klientem i GitHubem; osobny projekt i budżet API | Bezpieczeństwo i kontrola kosztów |
| D-13 | Na początek główne strony menu, Q, ekran fotografowania i firmware | Materiały potrzebne do planowania bez zbierania setek ekranów |

## Kierunki robocze i decyzje otwarte

| ID | Temat | Status |
| --- | --- | --- |
| P-01 | WWW/PWA zamiast aplikacji App Store | Preferowany kierunek; technologia i zakres offline nieustalone |
| P-02 | Higgsfield do krótkich klipów | Rozważane narzędzie; brak prób i zakupu w tym etapie |
| P-03 | GPT-6 Astra jako model referencyjny nauczyciela | Ostatnia propozycja z rozmowy; przed integracją ocena jakości, dostępności i kosztu |
| P-04 | Saldo 5–10 USD i wyłączone automatyczne doładowanie | Przykład budżetu; nie jest zgodą na płatność ani zmianę konta |
| P-05 | Lista i kolejność lekcji Poziomu 1 | Do opracowania i akceptacji |
| P-06 | Obiektyw, firmware i dokładne polskie etykiety menu | Oczekuje na materiały egzemplarza |
| P-07 | Hosting, logowanie, baza, synchronizacja postępów, retencja zdjęć | Do ustalenia przed implementacją |

## Później

Specjalizacje jako kolejny poziom, model aparatu obracany palcem, osiągnięcia, adaptacyjne ćwiczenia, niezależny nauczyciel fotografii i ewentualna optymalizacja modeli. Zachowanie pomysłu nie oznacza zatwierdzenia jego implementacji.

## Doprecyzowania po przeglądzie rozmowy

- Linki do materiałów nie oznaczają pobranych plików. Początkowo nie mamy lokalnych zdjęć ani instrukcji.
- Liczby stron menu są roboczym planem zbierania zdjęć, nie zweryfikowaną mapą egzemplarza.
- Nazwy i numery lekcji użyte w przykładach nie ustanawiają programu kursu.
- Budżet/alert API i egzekwowany twardy limit to różne ustawienia. Nawet twardy limit nie daje gwarancji rozliczenia co do centa; szczegóły w dokumencie 11.
- Kwota za 42 zdjęcia była szacunkiem, nie wynikiem pomiaru. Nie stanowi gwarancji kosztu.
- Wcześniejsza propozycja kilku modeli ustępuje prostszemu kierunkowi jednego modelu referencyjnego; wdrożenie nadal wymaga decyzji.

## Jak dopisywać decyzje

Nowy wpis zawiera datę, ID, decyzję, status, uzasadnienie i wpływ na zakres. Zmiana wcześniejszej decyzji wskazuje, który wpis zastępuje. Decyzje produktowe podejmuje użytkownik; Codex implementuje zaakceptowany etap.

## D-14 — Lokalna baza instrukcji (17.09.2026)

Na wyraźne polecenie użytkownika pobrano oryginalne PDF PL i EN do `materials/canon-official/` we właściwym repo. Pliki pozostają lokalne i ignorowane przez Git. Pochodzenie, daty i ograniczenia zapisano w rejestrze. Materiały wideo mają na razie tylko lokalny katalog i odnośnik do źródła; nie są dostępne offline. Decyzja nie obejmuje commit/push ani redystrybucji instrukcji.

## D-15 — Forma kolejnych lekcji (18.09.2026)

**Status: zaakceptowane przez użytkownika.** Forma [L1-01](L1-01_ROBIE_SWOJE_PIERWSZE_ZDJECIE.md) jest wzorcem kolejnych lekcji: bezpośredni język do Ani, przygotowanie, kroki „zrób → sprawdź”, krótkie wyjaśnienie, ćwiczenie, pomoc, kryteria ukończenia i zdanie podsumowania. Źródła i uwagi redakcyjne pozostają w osobnej części.

Uzasadnienie: użytkownik pozytywnie ocenił pierwszą lekcję i wyraźnie zaakceptował jej formę. Decyzja doprecyzowuje strukturę z dokumentu 04. Nie oznacza sprawdzenia lekcji na egzemplarzu Ani ani zatwierdzenia całej listy lekcji lub implementacji aplikacji. Kolejne treści przygotowujemy w tym wzorcu w ramach zatwierdzanych prac.

## D-16 — Telefon jako pierwszy widok kursu (18.09.2026)

**Status: zaakceptowane przez użytkownika.** Rozpoczynamy projektowanie wyglądu od lekcji na telefonie. Ania korzysta z iPhone’a 17 Pro Max, użytkownik ma do prób iPhone’a 15 Pro Max. Uzasadnienie: rozpoczęcie oceny formy wizualnej na rzeczywistych urządzeniach użytkowników. Wpływ: doprecyzowanie urządzeń dla pierwszego projektu; bez decyzji o technologii lub wdrożeniu aplikacji.

## D-17 — Życzliwy humor w porównaniach (18.09.2026)

**Status: zaakceptowane przez użytkownika.** W porównaniach można dodać odrobinę humoru, aby kurs był miły i przyjemny. Wpływ: uzupełnienie zasad języka w dokumencie 03; humor nie zastępuje precyzyjnych instrukcji ani nie ocenia Ani. Nie wymaga przebudowy zaakceptowanego wzorca lekcji.

## D-18 — Pierwszy szkielet aplikacji na iPhone (18.09.2026)

**Status: zaakceptowane przez użytkownika.** Użytkownik zatwierdził przejście od makiety do małej aplikacji internetowej z ikoną: nazwa „Canon RP — Kurs”, fioletowa ikona, ekran startowy, dwie lekcje, układ jeden krok naraz, lawenda/fiolet z delikatnym różem, próbne animowane zbliżenie z pauzą i adres do testu na iPhonie. Następnie polecił kontynuować.

Wykonano minimalny wariant statyczny na Sites, prywatny dla właściciela. Ikona i manifest pozwalają uruchamiać stronę z ekranu początkowego jako aplikację internetową; próbę na prawdziwym iPhonie wykonuje użytkownik. Bez API AI, synchronizacji, bazy danych i trybu offline. Animacja jest zbliżeniem prawdziwego zdjęcia, nie filmem fizycznego przełączania elementów. Wybór dostępu dla Ani pozostaje osobnym krokiem; nie publikować kursu publicznie bez zgody.

Źródło aplikacji ma osobne repozytorium wymagane przez Sites. Szczegóły lokalizacji i wdrożenia zawiera dokument 13. Główne repo dokumentacji nie zostało w tym etapie automatycznie commitowane ani wypchnięte.

## D-19 — Docelowe animacje i precyzyjne oznaczenia (18.09.2026)

**Status: zaakceptowane przez użytkownika, niewdrożone.** Sekwencja: krótki obrót aparatu → zbliżenie na właściwy element → pokazanie działania, np. przełączenia na ON lub naciśnięcia spustu. Animacja rozpoczyna się sama po wejściu w krok, bez wymaganego przycisku „Odtwórz”. Aktualne powiększanie nieruchomego zdjęcia uruchamiane przyciskiem nie spełnia docelowego oczekiwania. Ustalenie zastępuje ten aspekt próbnej animacji z D-18.

Wskazanie ma obejmować wyłącznie konkretny element: cienki dopasowany obrys albo krótka strzałka zamiast dużego kółka mieszczącego kilka elementów. Oznaczenie pozostaje przy elemencie podczas ruchu i zbliżenia. Najpierw jedna animacja wzorcowa „Włącz aparat”, do oceny na telefonie, potem kolejne.

Technika wykonania nie została wybrana. Potrzebne jest prawdziwe nagranie albo zweryfikowany klip zachowujący geometrię aparatu i poprawne oznaczenia. Nie ma jeszcze gotowego klipu. Higgsfield jest rozważaną możliwością, nie zatwierdzonym zakupem. Menu musi pozostać autentyczne. Zachować możliwość zatrzymania ruchu i uwzględnić preferencję ograniczenia animacji; automatyczny start na iPhonie wymaga sprawdzenia podczas wdrożenia.

## D-20 — Klikalny spis treści (18.09.2026)

**Status: zaakceptowane wymaganie, niewdrożone.** Dodać klikalny spis treści prowadzący bezpośrednio do poszczególnych lekcji oraz ćwiczeń. Użytkownik ma móc wybrać potrzebny temat bez przechodzenia wszystkich wcześniejszych kroków. Miejsce spisu, sposób prezentacji i nawigację powrotną ustalić przy projekcie; nie są jeszcze zatwierdzonym interfejsem. Zachować prostą obsługę na telefonie. Obecne dwie karty lekcji na starcie nie stanowią docelowego spisu lekcji i ćwiczeń.

## D-21 — Osobisty prezent i niespodzianka dla Ani (18.09.2026)

**Status: ustalone przez użytkownika.** Ania nie wie o powstającym kursie. Ma to być osobisty, piękny prezent z efektem „wow”, przy zachowaniu rzetelnej nauki fotografii. Ograniczamy jej udział w przygotowaniach do potrzebnych zdjęć aparatu; nie angażujemy jej w projektowanie ani ocenę aplikacji przed ujawnieniem niespodzianki. Wygląd, jej kolory, życzliwy język, lekki humor i płynne prowadzenie stanowią ważną część doświadczenia.

Doprecyzowanie D-19: animacje są częścią sposobu prowadzenia, nie tylko pomocą przy trudnych czynnościach. „Włącz aparat” pozostaje wzorcem jakości i stylu, choć samo przełączenie OFF → ON jest łatwe. Obowiązuje obrót → zbliżenie → pokazanie działania, automatyczny start i precyzyjne oznaczenie podążające za elementem, z możliwością zatrzymania. Nie redukować tej wizji do powiększania nieruchomego zdjęcia ani animowania wyłącznie trudniejszych operacji. Technika wykonania pozostaje otwarta; ta decyzja nie zatwierdza nowej infrastruktury ani płatnych usług.

## D-22 — Zdalne zbieranie materiałów i niezależna praca nad treścią (18.09.2026)

**Status: ustalone z użytkownikiem.** Paweł jest poza domem i może pomagać Ani wyłącznie telefonicznie lub przez wiadomości. Ania samodzielnie fotografuje aparat telefonem. Codex przygotowuje krótką instrukcję jednego ujęcia do przekazania przez Pawła; Ania przesyła zdjęcie Pawłowi, a on dodaje je do rozmowy do oceny. Kolejne ujęcie lub poprawka wynika z przeglądu otrzymanego materiału. Nie zakładać obecności drugiej osoby na miejscu ani obciążać Ani produkcją docelowych animacji.

Sesję zdjęciową zaplanowano na następny dzień, 19.09.2026, po zgłoszeniu gotowości przez użytkownika. Przygotujemy kadry ogólne i zbliżenia potrzebne do istniejących lekcji, oceniając czytelność elementów i odbicia. Dobór dalszych nagrań i techniki animacji pozostaje osobnym ustaleniem; prostota zbierania materiałów nie obniża oczekiwań wobec końcowej aplikacji.

Zdjęcia nie są warunkiem opracowania programu i treści lekcji. Można pisać je własnymi słowami na podstawie instrukcji Canona dla EOS RP + RF 50 mm F1.8 STM, oznaczając elementy wymagające testu jako „do sprawdzenia”. Zdjęcia służą ilustracjom i późniejszej weryfikacji egzemplarza. Katalog 17 filmów „In a Snap” nie zastępuje analizy filmów lub transkrypcji. Kolejność 14 lekcji nadal wymaga akceptacji; dzisiejsze doprecyzowanie nie jest poleceniem automatycznego napisania pozostałych lekcji.

## D-23 — Sprawdzone źródła i kolejność tworzenia lekcji (18.09.2026)

**Status: zatwierdzone przez użytkownika.** Przed napisaniem lekcji sprawdzamy źródła, następnie układamy zrozumiałe wyjaśnienie i ćwiczenie, a na końcu kontrolujemy zgodność z aparatem Ani. Wiedza techniczna pochodzi wyłącznie ze sprawdzonych materiałów; język, porównania i ćwiczenia są autorskie. Konkretne źródła i zakres weryfikacji trafiają do karty redakcyjnej. Nieprzeczytane artykuły i nieprzeanalizowane filmy nie są potwierdzeniem informacji. Braki dotyczące egzemplarza oznaczamy „do sprawdzenia”.

Uzasadnienie: kurs ma być rzetelnym, godnym zaufania prezentem. Wpływ: utrwalenie procesu w dokumencie 03, bez automatycznej zgody na napisanie wszystkich lekcji lub zmianę aplikacji.

## D-24 — Własne i wcześniejsze zdjęcia we współpracy z AI (18.09.2026)

**Status: zatwierdzone doprecyzowanie docelowego modułu, niewdrożone.** Ania może dodawać nowe zdjęcia z EOS RP oraz swoje wcześniejsze zdjęcia, także z innego aparatu lub telefonu, niezależnie od lekcji i obecności EXIF. Nauczyciel AI omawia to, co wyszło dobrze, oraz najwyżej jedną lub dwie rzeczy do poprawy; uwzględnia zamiar Ani, odpowiada na pytania i pomaga przy kolejnych próbach. To współpraca, bez punktacji i zgadywania sprzętu, parametrów lub przyczyn.

Uzasadnienie: nauka ma obejmować własne fotografie Ani, nie tylko zadania kursowe. Wpływ: doprecyzowanie D-08–D-10 oraz dokumentu 06 i przyszłych prób akceptacyjnych. Interfejs rozmowy, retencja, model i budżet pozostają do ustalenia. Ten wpis nie uruchamia integracji, płatnych usług ani wysyłania zdjęć.
