#!/usr/bin/env bash
# Jednorazowa konfiguracja serwera hermes-vps pod kurs Canon RP.
# Uruchamia właściciel na serwerze: sudo bash setup-canonkurs.sh
# Opis i cofanie zmian: README.md w tym folderze.
set -euo pipefail

readonly DEPLOY_USER="canonkurs"
readonly DEPLOY_HOME="/home/${DEPLOY_USER}"
readonly SITE_DIR="/srv/canon-rp-kurs"
readonly DEPLOY_KEY="ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIavyKHOmsdVycdpFgng20c5nBDOb04pM/1s9YNg5vPo canon-rp-kurs deploy (Mac)"

fail() {
  echo "BŁĄD: $*" >&2
  exit 1
}

# Sprawdzenia przed jakąkolwiek zmianą.
[[ "${EUID}" -eq 0 ]] || fail "uruchom skrypt przez: sudo bash $0"
command -v tailscale >/dev/null 2>&1 || fail "brak polecenia tailscale."
if id "${DEPLOY_USER}" >/dev/null 2>&1; then
  fail "konto ${DEPLOY_USER} już istnieje. Niczego nie zmieniłem."
fi
if [[ -e "${SITE_DIR}" ]]; then
  fail "${SITE_DIR} już istnieje. Niczego nie zmieniłem."
fi

# a) Konto bez hasła, tylko do wgrywania kursu.
useradd --create-home --shell /bin/bash "${DEPLOY_USER}"

# b) Klucz wdrożeniowy z Maca, z ograniczeniami „restrict”.
install -d -m 700 -o "${DEPLOY_USER}" -g "${DEPLOY_USER}" "${DEPLOY_HOME}/.ssh"
printf 'restrict %s\n' "${DEPLOY_KEY}" > "${DEPLOY_HOME}/.ssh/authorized_keys"
chown "${DEPLOY_USER}:${DEPLOY_USER}" "${DEPLOY_HOME}/.ssh/authorized_keys"
chmod 600 "${DEPLOY_HOME}/.ssh/authorized_keys"

# c) Folder na pliki kursu.
install -d -m 755 -o "${DEPLOY_USER}" -g "${DEPLOY_USER}" "${SITE_DIR}"

# d) Udostępnienie folderu tylko w prywatnej sieci Tailscale.
tailscale serve --bg --https=443 "${SITE_DIR}"

# e) Stan i podsumowanie.
echo
echo "== tailscale serve status =="
tailscale serve status
echo
echo "== Podsumowanie =="
echo "- Utworzono konto ${DEPLOY_USER} (bez hasła, logowanie tylko kluczem z Maca)."
echo "- Klucz wpisano do ${DEPLOY_HOME}/.ssh/authorized_keys."
echo "- Utworzono folder ${SITE_DIR} (właściciel: ${DEPLOY_USER})."
echo "- Folder jest udostępniony przez Tailscale na porcie 443, tylko w prywatnej sieci."
echo "Folder jest na razie pusty. Kurs trzeba jeszcze wgrać z Maca."
