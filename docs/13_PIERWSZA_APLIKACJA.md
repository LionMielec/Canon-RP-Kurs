# Pierwsza aplikacja — wersja do prób

Aktualizacja: 18.09.2026. Publikacja zakończona powodzeniem.

[Otwórz Canon RP — Kurs](https://canon-rp-kurs-ani.pawel-s-mielec.chatgpt.site)

## Zakres

Ekran startowy, dwie pełne lekcje, jeden krok naraz, rozwijana pomoc, lawenda/fiolet/róż i fioletowa ikona. Pierwsza lekcja pokazuje animowane zbliżenia prawdziwego zdjęcia aparatu z zaznaczonym elementem. Animacja jest uruchamiana przyciskiem, ma pauzę i powtórzenie, respektuje ograniczenie ruchu. Nie przedstawia fizycznego przestawiania przełączników.

Treści z istniejących L1-01 i L1-02 zostały zachowane, bez kart redakcyjnych. Pomoc przeniesiono pod kroki i ćwiczenie. Przygotowanie, wyjaśnienie i zakończenie mają osobne widoki. Dodano dwa delikatne porównania humorystyczne zgodnie z D-17.

## Na iPhonie

Otwórz adres w Safari i zaloguj się kontem właściciela, jeśli pojawi się ekran dostępu. W menu udostępniania wybierz dodanie do ekranu początkowego. Pozostaw włączone „Otwórz jako aplikację internetową”, jeżeli ta opcja jest widoczna, i zatwierdź dodanie. Otwórz kurs z nowej ikony.

[Instrukcja Apple](https://support.apple.com/guide/iphone/open-as-web-app-iphea86e5236/ios).

Pierwszy test: iPhone 15 Pro Max użytkownika. Docelowo: iPhone 17 Pro Max Ani. Dostęp jest prywatny dla właściciela; udostępnienie Ani wymaga oddzielnego ustalenia. Nie obiecano pełnego trybu offline — aplikacja potrzebuje internetu. Nie ma AI, bazy danych ani synchronizacji postępów.

## Źródła i hosting

Minimalna statyczna aplikacja HTML/CSS/JavaScript. Źródło i publikowane pliki: `dist/`. Manifest z trybem `standalone`; ikony PNG 180, 192 i 512 px oraz SVG. Bez dodatkowego frameworka i zależności uruchomieniowych.

**Właściwy folder kodu Sites:** `/Users/pawelsiedleczka/.codex/.chatgpt-projects/g-p-6aabf9b9dd848191b1f8a77f4f9213d0/canon-rp-app`.

Główny folder `/Users/pawelsiedleczka/Documents/ChatGPT/Canon-RP-Kurs` nadal przechowuje dokumentację. Jego `app/` nie jest aktualnym checkoutem opublikowanej strony. Nie tworzyć drugiego Site ani niezależnej kopii kodu przy kontynuacji; pracować w folderze powyżej i używać istniejącego identyfikatora.

- Site: `appgprj_6aad16a482e48191a0f623f9a51b32a9`.
- Wersja: 1.
- Commit źródła: `c71aebd8f7dabe4da6103bdee1c784817a140dfc`.
- Wersja Sites: `appgprj_6aad16a482e48191a0f623f9a51b32a9~appgver_09c57ada50d481918184f7856f723080`.
- Wdrożenie: `appgdep_6aad1c2b41948191bd519751858b555a`, status `succeeded`.

Kod zapisano i przesłano do osobnego prywatnego repo źródłowego Sites. Repo dokumentacji nie było automatycznie commitowane ani wypychane w tym etapie. W plikach nie zapisano danych dostępu do hostingu.

## Weryfikacja

Sprawdzono 20 widoków obu lekcji przy szerokościach 320, 430, 440 i 1024 px (80 kombinacji), brak poziomego przepełnienia i błędów JavaScript. Przetestowano przejścia, rozwijanie pomocy, animację: start/pauza/wznowienie/powtórzenie, ograniczenie ruchu oraz próbę z tekstem powiększonym do 200%. Sprawdzono dostępność ikon i zasobów, manifest, składnię skryptów oraz obejrzano zrzuty ekranu startowego i obu lekcji. Hosting potwierdził udaną publikację wersji 1.

Pozostaje rzeczywista próba Safari, logowania i ikony na iPhonie. Testy przeglądarkowe wykonano w Chrome z emulacją mobilnego widoku — nie są testem fizycznego iPhone’a ani aparatu Ani. Zgodność obsługi aparatu i firmware pozostaje do sprawdzenia zgodnie z kartami lekcji.

## Następny krok

Ocenić wygląd na telefonie: czytelność, przewijanie, kolory i animowane zbliżenie. Użytkownik decyduje o zmianach. Nie rozbudowywać automatycznie kolejnych lekcji, AI ani infrastruktury.

## Ocena i korekty po publikacji — 18.09.2026

Użytkownik pozytywnie ocenił wygląd aplikacji. Nie potwierdził jednoznacznie uruchomienia z ikony na iPhonie; nie oznaczać tego testu jako zaliczonego. Rozmowa tej sesji nie była widoczna w projekcie ChatGPT na jego telefonie, dlatego dostęp do kursu przekazywać bezpośrednim adresem, niezależnie od widoczności rozmowy.

Docelowa animacja została doprecyzowana w D-19: obrót, zbliżenie, pokazanie działania, start automatyczny bez przycisku „Odtwórz”. Duże kółko zastąpi precyzyjny obrys lub strzałka. Wersja 1 nadal ma dotychczasowy przycisk i powiększenie zdjęcia; nie wdrożono jeszcze korekt.

D-20 dodaje wymaganie klikalnego spisu lekcji i ćwiczeń. Obecne karty dwóch lekcji są punktem wyjścia; spis z bezpośrednimi wejściami do ćwiczeń pozostaje do przygotowania.
