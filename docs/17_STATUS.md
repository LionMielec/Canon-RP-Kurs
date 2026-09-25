# Canon RP kurs — STATUS

Stan na: 2026-09-25

## Etap projektu
Trwa przygotowanie projektu do implementacji w Codexie oraz porządkowanie materiałów i treści kursu.

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

## Następny krok
Najpierw uporządkować **rdzeń edukacyjny Poziomu 1**: zatwierdzić program, przygotować plan produkcji lekcji, przypisać do każdej lekcji sprawdzone źródła, ćwiczenia i potrzebne materiały z aparatu Ani. Równolegle kontynuować kontrolowany handoff do Codexa i zdefiniować MVP aplikacji tak, aby implementacja obsługiwała zatwierdzoną strukturę kursu. Punkt 9 — Analiza zdjęć przez AI pozostaje zatwierdzonym modułem wspierającym, ale nie jest nadrzędnym priorytetem wobec treści edukacyjnej.

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

## L1-02 — stan roboczy 24.09.2026
- wykonano research techniczny obsługi odtwarzania i powiększania zdjęć na Canon EOS RP,
- główna ścieżka obsługi: przycisk odtwarzania → wybór zdjęcia → przycisk z lupą → główne pokrętło do powiększenia → wybierak do przesuwania widoku,
- sprawdzenie ostrości opiera się na porównaniu tego samego konkretnego szczegółu na trzech zdjęciach,
- lekcja celowo nie diagnozuje jeszcze pełnych przyczyn nieostrości i nie wprowadza ustawień AF,
- przygotowano `/Canon-RP-kurs/docs/L1-02_LESSON.md`,
- przygotowano `/Canon-RP-kurs/docs/L1-02_VISUAL_PRODUCTION.md`,
- do `ASSET_MANIFEST.md` dopisano V01–V05 dla L1-02,
- istniejące zdjęcia Ani wystarczają do V01 i V03; nowe materiały są potrzebne tylko dla realnego ekranu odtwarzania/powiększenia oraz kontrolowanego porównania detalu,
- L1-02 nie jest jeszcze zatwierdzona; następny krok to wspólny przegląd treści i zakresu.



## Korekta L1-02 — gotowy kurs
- materiały dydaktyczne pokazujące ostrość są częścią gotowej aplikacji i powstają przed przekazaniem kursu Ani,
- zdjęcia Ani są wykorzystywane dopiero w ćwiczeniu po demonstracji, nie jako źródło materiałów do nauczenia nowego pojęcia,
- dla L1-02 znaleziono otwarte źródła CC0 do warstwy dydaktycznej: zestaw Bautsch `Correct.Focus` / `Front.Focus` / `Back.Focus` oraz kandydat wysokorozdzielczy `Chive flower close-up`,
- rzeczywiste zdjęcia EOS RP Ani służą do wskazywania fizycznych przycisków i pokręteł,
- po korekcie nie wymagamy zdjęć ekranu odtwarzania EOS RP ani osobnej produkcji zdjęć referencyjnych przez Anię lub właściciela projektu,
- L1-02 została zatwierdzona 25.09.2026. Przyjęto uproszczenie wzorca V01 do dwóch przykładów, korektę opisu małego podglądu, porównywanie tego samego konkretnego szczegółu oraz obowiązek zapisania dokładnych źródeł V04 przed produkcją.
- Następny krok: wspólny przegląd L1-03 „Układam zdjęcie bez zmiany ustawień”.

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
