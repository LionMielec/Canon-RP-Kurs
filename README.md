# Canon RP — Kurs

Pierwsza wersja aplikacji internetowej do prywatnych testów. Zatwierdzony zakres: ikona ekranu początkowego iPhone’a, ekran startowy, dwie lekcje, jeden krok naraz, lawenda/fiolet/róż i animowane zbliżenie z możliwością zatrzymania.

Statyczne pliki w `dist/` są zarówno źródłem, jak i publikowaną aplikacją. Bez frameworka, instalacji zależności i zewnętrznych skryptów. Manifest określa uruchamianie w osobnym oknie. Aplikacja wymaga internetu; nie ma trybu offline, serwera AI ani synchronizacji postępów.

## Materiały i treść

`dist/lessons.js` zawiera treść dla Ani z L1-01 (zaakceptowany wzorzec) i L1-02 w dokumentacji `/Users/pawelsiedleczka/Documents/ChatGPT/Canon-RP-Kurs/docs/`. Karty redakcyjne nie są częścią interfejsu. Pomoc pozostaje dostępna przy krokach i ćwiczeniu. Układ dzieli treść na przygotowanie, sześć kroków, wyjaśnienie, ćwiczenie i podsumowanie.

`dist/camera-top.jpeg` to własne zdjęcie udostępnione przez użytkownika (oryginał 780DC05E-6E96-4ADA-B67E-219B670E3C0A.jpeg). Ruch jest animowanym zbliżeniem na zdjęcie, nie filmem pokazującym fizyczne przestawienie przełącznika. Zdjęcie pozostaje niezmienione; oznaczenia są nakładane w interfejsie. Animacja uruchamia się na żądanie, ma pauzę i powtórzenie oraz respektuje ograniczenie ruchu.

Ikona jest prostym własnym znakiem obiektywu z literami RP. Nie używa logo producenta jako znaku aplikacji.

## Urządzenia i dostęp

Docelowe urządzenie Ani: iPhone 17 Pro Max. Telefon do pierwszych prób: iPhone 15 Pro Max. Rzeczywiste działanie dodawania ikony i otwierania prywatnej aplikacji wymaga testu na telefonie. Publikacja Sites jest prywatna dla właściciela; udostępnienie Ani wymaga osobnego ustalenia dostępu. Nie zmieniać publiczności na publiczną.

Instalowanie na iPhonie: otworzyć adres w Safari, wybrać udostępnianie i dodanie do ekranu początkowego, pozostawić otwieranie jako aplikacja internetowa, jeśli taka opcja jest widoczna. Źródło: https://support.apple.com/guide/iphone/open-as-web-app-iphea86e5236/ios

## Przegląd lokalny

Z katalogu projektu: `python3 -m http.server 8766 --bind 127.0.0.1 --directory dist`.

Treści i polskie oznaczenia menu nadal wymagają testów na aparacie Ani. Ta wersja nie zatwierdza finalnej palety ani animacji pozostałych lekcji.
