# Hosting kursu na hermes-vps (Tailscale)

Decyzja właściciela z 17.10.2026: kurs jest dostępny tylko w prywatnej sieci Tailscale.
Do wgrywania plików służy osobne konto `canonkurs`.

## Co robi `setup-canonkurs.sh`

Skrypt uruchamia się raz, na serwerze. Najpierw sprawdza, czy:
- działa z uprawnieniami administratora (`sudo`),
- na serwerze jest Tailscale,
- konto `canonkurs` jeszcze nie istnieje,
- folder `/srv/canon-rp-kurs` jeszcze nie istnieje.

Jeśli którykolwiek warunek nie jest spełniony, skrypt kończy się komunikatem i niczego nie zmienia.

Potem:
1. Tworzy konto `canonkurs` bez hasła.
2. Wpisuje temu kontu klucz z Maca (`~/.ssh/canonkurs_deploy_ed25519`) z opcją `restrict`.
   Ta opcja blokuje m.in. przekierowania portów i dodatkowe kanały połączenia.
3. Tworzy pusty folder `/srv/canon-rp-kurs` należący do konta `canonkurs`.
4. Udostępnia ten folder przez Tailscale pod adresem `https://hermes-vps-1.<nazwa-sieci>.ts.net/`
   — tylko dla urządzeń w prywatnej sieci Tailscale, nie w otwartym internecie.
5. Wypisuje stan udostępniania i krótkie podsumowanie.

Skrypt niczego nie instaluje i nie zmienia ustawień SSH, zapory, Hermesa, `/srv/dyknote` ani `/home/hermesadmin`.

## Jak uruchomić

1. Skopiuj skrypt z Maca na serwer:

   ```bash
   scp production/hosting/setup-canonkurs.sh hermes-vps:~/
   ```

2. Zaloguj się na serwer i uruchom skrypt (poprosi o hasło do `sudo`):

   ```bash
   ssh hermes-vps
   ```

   ```bash
   sudo bash ~/setup-canonkurs.sh
   ```

3. Sprawdź z Maca, czy logowanie nowym kontem działa:

   ```bash
   ssh canonkurs-vps true
   ```

## Wgrywanie nowej wersji

Na Macu, w folderze projektu, uruchom jedną komendę:

```bash
bash production/hosting/deploy.sh
```

Skrypt:
- zatrzymuje się, jeśli w `app/` są niezapisane zmiany albo `app/` różni się od wersji w `main` na GitHubie,
- wysyła cały folder `app/dist/` na serwer, razem z rysunkami Canon,
- usuwa z serwera pliki, których nie ma już na Macu (pomija pliki `.DS_Store`),
- na końcu pisze, ile plików jest na serwerze i ile z nich to rysunki Canon.

Kurs jest potem pod adresem `https://hermes-vps-1.taila20cd6.ts.net/` (tylko w sieci Tailscale).

## Jak cofnąć

Każdy punkt można cofnąć osobno. Komendy uruchamia się na serwerze, przez `sudo`.

Wyłączenie udostępniania przez Tailscale (punkt 4):

```bash
sudo tailscale serve --https=443 off
```

Usunięcie folderu kursu razem z wgranymi plikami (punkt 3):

```bash
sudo rm -rf /srv/canon-rp-kurs
```

Usunięcie samego klucza, bez usuwania konta (punkt 2):

```bash
sudo rm /home/canonkurs/.ssh/authorized_keys
```

Usunięcie konta razem z jego folderem domowym i kluczem (punkty 1 i 2):

```bash
sudo userdel --remove canonkurs
```

### Na Macu

Usunięcie klucza wdrożeniowego:

```bash
rm ~/.ssh/canonkurs_deploy_ed25519 ~/.ssh/canonkurs_deploy_ed25519.pub
```

Przywrócenie `~/.ssh/config` sprzed dopisania wpisu `canonkurs-vps`:

```bash
cp ~/.ssh/config.backup-2026-10-17 ~/.ssh/config
```

## Serwer stron nginx (D-088)

Od D-088 kurs nie jest już udostępniany przez Tailscale bezpośrednio z folderu.
Pliki wysyła nginx, który słucha tylko na `127.0.0.1:8081` (wyłącznie wewnątrz serwera).
Tailscale serve przekazuje do niego ruch z portu 443, nadal tylko w prywatnej sieci Tailscale.

Dlaczego: przy udostępnianiu folderu Tailscale nie wysyła nagłówka `Cache-Control` ani `ETag`,
więc ikona na iPhonie pokazywała starą wersję kursu (D-087). nginx wysyła każdy plik
z `Cache-Control: no-cache` i `ETag` — telefon zawsze sprawdza, czy jest nowsza wersja.
Plik `manifest.webmanifest` idzie jako `application/manifest+json`. nginx nie podaje swojej wersji.

Pliki:
- `nginx/canon-rp-kurs.conf` — ustawienia nginx dla kursu,
- `setup-nginx.sh` — jednorazowa instalacja.

### Co robi `setup-nginx.sh`

Najpierw sprawdza, czy działa z `sudo`, czy obok leży `canon-rp-kurs.conf`, czy istnieje folder kursu
i czy tailscale serve udostępnia folder kursu albo już przekazuje ruch do nginx.
Przy czymkolwiek innym kończy się i niczego nie zmienia. Potem:

1. Aktualizuje pakiety (`apt-get upgrade`). Przy pytaniu o plik ustawień zostawia obecną wersję.
   Usług nie restartuje — na końcu tylko wypisuje, które warto zrestartować.
   Jeśli serwer wymaga restartu, skrypt kończy się komunikatem i **nie** restartuje serwera.
2. Instaluje nginx z pakietów Ubuntu **bez uruchamiania go**. Domyślna strona nginx
   słuchałaby na porcie 80 na wszystkich adresach. Na czas instalacji skrypt tworzy
   `/usr/sbin/policy-rc.d` (mechanizm Debiana), który zabrania uruchomienia tylko nginx;
   zaraz po instalacji plik usuwa.
3. Wpisuje `canon-rp-kurs.conf` do `/etc/nginx/sites-available/` i wyłącza domyślną stronę nginx.
4. Sprawdza ustawienia (`nginx -t`), uruchamia nginx i sprawdza, że słucha tylko na `127.0.0.1:8081`.
5. Przełącza tailscale serve z folderu na `http://127.0.0.1:8081`.
6. Sprawdza nagłówki strony głównej, `app.js` i `manifest.webmanifest`, adresy nginx,
   stan tailscale serve i to, że Hermes (`hermes-gateway`) działa.

Skrypt można bezpiecznie uruchomić drugi raz — kroki już zrobione pomija albo powtarza bez skutków ubocznych.

### Jak uruchomić

Aktualizacja Tailscale chwilowo przerywa połączenia przez Tailscale. Łącz się więc
skrótem `hermes-vps` (adres publiczny serwera), nie przez Tailscale.

1. Skopiuj oba pliki z Maca na serwer:

   ```bash
   scp production/hosting/setup-nginx.sh production/hosting/nginx/canon-rp-kurs.conf hermes-vps:~/
   ```

2. Zaloguj się i uruchom skrypt (poprosi o hasło do `sudo`):

   ```bash
   ssh hermes-vps
   ```

   ```bash
   sudo bash ~/setup-nginx.sh
   ```

3. Z Maca sprawdź nagłówki (tylko w sieci Tailscale):

   ```bash
   curl -sI https://hermes-vps-1.taila20cd6.ts.net/manifest.webmanifest
   ```

### `deploy.sh` działa bez zmian

`deploy.sh` nadal wgrywa pliki do `/srv/canon-rp-kurs` kontem `canonkurs`, a nginx czyta z tego samego folderu.
Sprawdzone 30.10.2026: wszystkie pliki w `app/dist/` na Macu i w `/srv/canon-rp-kurs` na serwerze
są czytelne dla innych kont (nginx działa jako `www-data`), a folder ma prawa `755`.
`ETag` zależy od daty zmiany i rozmiaru pliku; `deploy.sh` przenosi datę zmiany z Maca (`rsync -t`),
więc nowa wersja pliku dostaje nowy `ETag`. Nowe pliki dostają prawa z Maca z maską serwera `022`.

### Jak cofnąć nginx

Komendy uruchamia się na serwerze, przez `sudo`, w tej kolejności.

1. Tailscale serve z powrotem na folder kursu — najpierw wyłączenie przekazywania do nginx,
   potem udostępnienie folderu tą samą komendą co w `setup-canonkurs.sh`.
   Kolejność ma znaczenie: dokumentacja Tailscale nie mówi, czy nowe ustawienie zastępuje stare pod tym samym adresem,
   więc stare wyłączamy jawnie.

   ```bash
   sudo tailscale serve --https=443 http://127.0.0.1:8081 off
   ```

   ```bash
   sudo tailscale serve --bg --https=443 /srv/canon-rp-kurs
   ```

2. Zatrzymanie nginx i wyłączenie jego startu przy uruchomieniu serwera.
   Robimy to dopiero po kroku 1, żeby kurs nie przestał działać w międzyczasie.

   ```bash
   sudo systemctl disable --now nginx
   ```

3. (Opcjonalnie) Usunięcie nginx razem z jego ustawieniami. Po kroku 2 nginx nie działa,
   więc ten krok nie jest potrzebny do przywrócenia kursu.

   ```bash
   sudo apt-get purge nginx nginx-common
   ```

Aktualizacji pakietów z kroku 1 skryptu nie cofamy — to zwykłe poprawki Ubuntu i Tailscale.
