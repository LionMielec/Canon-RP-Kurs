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
