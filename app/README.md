# Canon RP — Kurs

Lokalna wersja aplikacji internetowej do prywatnych testów. Zakres: ikona ekranu początkowego iPhone’a, ekran startowy, dwie lekcje, jeden krok naraz oraz zachowana kolorystyka lawendy, fioletu i różu.

Statyczne pliki w `dist/` są zarówno źródłem, jak i publikowaną aplikacją. Bez frameworka, instalacji zależności i zewnętrznych skryptów. Manifest określa uruchamianie w osobnym oknie. Aplikacja wymaga internetu; nie ma trybu offline, serwera AI ani synchronizacji postępów.

## Materiały i treść

`dist/lessons.js` zawiera dosłowną treść dla Ani z zatwierdzonych dokumentów L1-01 i L1-02 w `/Users/pawelsiedleczka/Documents/ChatGPT/Canon-RP-Kurs/docs/`. Dane rozdzielają cel, kroki, ćwiczenie, pomoc, podsumowanie i materiały powiązane identyfikatorami z krokami. `dist/app.js` renderuje ten sam układ dla obu lekcji. Spis na stronie głównej prowadzi do początku każdej lekcji i bezpośrednio do ćwiczenia.

L1-01-V01 i V02 korzystają wyłącznie z mastera `fbe2fd62-e8ab-465b-b340-b6d0b4458622.jpg` (`libfile_167abe23e1488191ba89b2d851b2155c`, SHA-256 `8aae829f911c1d3d950e66d616d8a1a51d22fac4882532d969a13d30f7f7603f`). Kadry robocze wycięto odpowiednio z pikseli `(150, 775, 790, 1255)` i `(900, 755, 1540, 1235)`; delikatne oznaczenia są nakładane w CSS. L1-02-V03 pochodzi z `57652b89-ae48-4cd1-b998-e883aee8aa1f.jpg`, kadr `(1020, 370, 1520, 870)`. Te trzy kadry wymagają zatwierdzenia. Pozostałe materiały V03–V06 w L1-01 oraz V01, V02, V04, V05 w L1-02 mają jawne placeholdery produkcyjne. Materiały produkcyjne nie są przedstawiane jako zatwierdzone przykłady dydaktyczne.

Surowe zdjęcia pozostają w lokalnym pakiecie `/Users/pawelsiedleczka/Documents/ChatGPT/Canon-RP-Kurs/materials/camera-source-pack-2026-09-24/`; do aplikacji trafiły tylko wskazane kadry.

### Lokalne korekty K-01–K-04 — 27.09.2026

Lekcja 1 ma osobne domknięcie teorii przed ćwiczeniem i przycisk „Przejdź do ćwiczenia”. Identyfikatory, statusy oraz notatki produkcyjne pozostają w danych, ale nie są renderowane Ani. Niegotowe materiały nadal mają jawne, naturalnie opisane placeholdery.

Powyższy opis trzech kadrów dotyczy wcześniejszej wersji. Materiał odtwarzania w Lekcji 2 ma teraz dwa ujęcia (odtwarzanie i wybierak), a powiększenie — trzy (lupa, główne pokrętło, wybierak). Wszystkie są wyświetlane przed tekstem używającym tych elementów. Nowe kadry pochodzą wyłącznie ze wskazanych masterów:

- `l1-02-selector.jpg`: tył aparatu, crop `(1170, 550, 1430, 810)`; używany przy przeglądaniu i przesuwaniu zdjęcia.
- `l1-02-magnify-button.jpg`: tył aparatu, crop `(1280, 350, 1500, 560)`.
- `l1-02-main-dial.jpg`: góra aparatu, crop `(1360, 430, 1810, 800)`; ten sam kadr pokazuje też spust migawki w Lekcji 1, z osobnym oznaczeniem. Nie zastępuje brakującego pokazu dwóch etapów naciskania.

Kadry są robocze, do zatwierdzenia; oznaczenia nakłada CSS. Pozostałe wcześniejsze braki (m.in. wzorce ostrości i pokaz trzymania aparatu) nie zostały uzupełnione w tej rundzie. Lokalna weryfikacja Chrome objęła wszystkie 23 widoki przy szerokościach 320, 390, 430, 768 i 1440 px, przejście teoria → ćwiczenie oraz Wstecz, obecność i kolejność zdjęć, brak identyfikatorów, błędów JS/HTTP i poziomego przewijania. Rozmiar 430 × 932 px odpowiada widokowi iPhone 15 Pro Max; nie jest testem fizycznego telefonu ani Safari. Nie wykonano commit/push/publikacji.

`dist/camera-top.jpeg` pozostał w katalogu po wersji 1, ale aplikacja go nie wyświetla i nie używa jako źródła V01/V02.

Ikona jest prostym własnym znakiem obiektywu z literami RP. Nie używa logo producenta jako znaku aplikacji.

## Urządzenia i dostęp

Docelowe urządzenie Ani: iPhone 17 Pro Max. Telefon do pierwszych prób: iPhone 15 Pro Max. Rzeczywiste działanie dodawania ikony i otwierania prywatnej aplikacji wymaga testu na telefonie. Publikacja Sites jest prywatna dla właściciela; udostępnienie Ani wymaga osobnego ustalenia dostępu. Nie zmieniać publiczności na publiczną.

Instalowanie na iPhonie: otworzyć adres w Safari, wybrać udostępnianie i dodanie do ekranu początkowego, pozostawić otwieranie jako aplikacja internetowa, jeśli taka opcja jest widoczna. Źródło: https://support.apple.com/guide/iphone/open-as-web-app-iphea86e5236/ios

## Przegląd lokalny

Z katalogu projektu: `python3 -m http.server 8766 --bind 127.0.0.1 --directory dist`.

Treści i polskie oznaczenia menu nadal wymagają testów na aparacie Ani. Ta wersja nie zatwierdza finalnej palety ani animacji pozostałych lekcji.

## Wspólny mechanizm instrukcji i podświetleń — lokalnie, 27.09.2026

Krok może zawierać `screens` z własnymi kluczami adresów, a ekran — uporządkowane `blocks`: `{text: '...'}` albo `{asset: 'identyfikator', frame: 0}`. Dzięki temu tekst i właściwe zdjęcie sąsiadują w danych; renderer nie rozpoznaje numerów konkretnych lekcji. Proste istniejące kroki zachowują `body` i `mediaPlacement`. Stary adres kroku prowadzi do jego pierwszego ekranu.

Odtwarzanie: `#lekcja-2/odtwarzanie`; następny ekran: `#lekcja-2/wybierak`. W powiększaniu każda z trzech instrukcji ma własne zdjęcie bezpośrednio poniżej.

Każda ramka zdjęcia ma tablicę `markers`. Wspólna konfiguracja: `x`, `y` (środek), `width`, `height` — procenty rozmiaru zdjęcia. `kind: 'halo'` oznacza miękką poświatę, a `kind: 'direction'` dodaje kierunek z `label`, np. `←`. Ten sam komponent obsługuje włącznik, A+, spust, odtwarzanie, lupę, pokrętło i wybierak. Nie ma klas CSS przypisanych do konkretnych elementów aparatu.

Zdjęcie zachowuje proporcje (`width: 100%; height: auto`), a nakładka ma ten sam układ odniesienia. Gradient z wcześniejszym różem poświaty (#e9a8d8) i stałe rozmycie zmiękczają krawędzie. Środek pozostaje pusty, aby nie zakrywać elementu aparatu. Po wejściu poświata wykonuje dwa spokojne oddechy po 6 s (skala nakładki 1–1,06), następnie pozostaje statyczna. Przezroczystość jest stała (opacity 1); pozycja i rozmiar kontenera markera nie są animowane. `prefers-reduced-motion: reduce` wyłącza pulsowanie i pozostawia widoczną poświatę. Oznaczenia są `aria-hidden`, zdjęcie i podpis nadal opisują czynność. Pliki zdjęć są niezmienione.

Test: `tests/camera-guidance.cjs` wymaga Playwright (można wskazać ścieżkę przez `PLAYWRIGHT_MODULE`), opcjonalnie `CHROME_EXECUTABLE`, działającego lokalnego podglądu (`PREVIEW_URL`, domyślnie port 8766) i `QA_OUTPUT` na zrzuty/wyniki. Testuje wszystkie widoki, brak technicznych ID, ładowanie obrazów, kolejność materiałów, nawigację, tryby ruchu, brak poziomego scrolla i geometrię markerów podczas skalowania. Nie wymaga zmian zależności publikowanej aplikacji.
