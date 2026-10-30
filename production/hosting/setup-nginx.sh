#!/usr/bin/env bash
# Przełączenie kursu Canon RP na nginx oraz aktualizacje serwera hermes-vps (D-088).
# Uruchamia właściciel na serwerze, z konta hermesadmin: sudo bash setup-nginx.sh
# Plik canon-rp-kurs.conf musi leżeć w tym samym folderze co skrypt.
# Opis i cofanie zmian: README.md w tym folderze.
set -euo pipefail

readonly SITE_DIR="/srv/canon-rp-kurs"
readonly LISTEN="127.0.0.1:8081"
readonly LOCAL_URL="http://${LISTEN}"
readonly CONF_NAME="canon-rp-kurs"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
readonly SCRIPT_DIR
readonly CONF_SRC="${SCRIPT_DIR}/${CONF_NAME}.conf"
readonly CONF_DST="/etc/nginx/sites-available/${CONF_NAME}"
readonly CONF_LINK="/etc/nginx/sites-enabled/${CONF_NAME}"
readonly DEFAULT_LINK="/etc/nginx/sites-enabled/default"
readonly POLICY="/usr/sbin/policy-rc.d"
readonly POLICY_MARK="# canon-rp-kurs setup-nginx.sh (D-088)"

# Aktualizacje bez pytań. Przy pytaniu o plik ustawień zostaje obecna wersja.
# needrestart tylko wypisuje usługi do restartu (bez tego sam restartowałby np. Hermesa).
export DEBIAN_FRONTEND=noninteractive
export NEEDRESTART_MODE=l
readonly APT_OPTS=(-y -o Dpkg::Options::=--force-confdef -o Dpkg::Options::=--force-confold)

fail() {
  echo "BŁĄD: $*" >&2
  exit 1
}

step() {
  echo
  echo "== $*"
}

# Stan tailscale serve: "folder" (jak po setup-canonkurs.sh), "nginx" (już przełączony) albo "inny".
serve_state() {
  local json
  json="$(tailscale serve status --json)"
  if grep -Fq "\"Proxy\": \"${LOCAL_URL}\"" <<<"${json}"; then
    echo "nginx"
  elif grep -Fq "\"Path\": \"${SITE_DIR}\"" <<<"${json}"; then
    echo "folder"
  else
    echo "inny"
  fi
}

# Adresy, na których słucha nginx (puste, gdy nie działa).
nginx_addresses() {
  ss -tlnpH | awk '/"nginx"/ {print $4}' | sort -u
}

# ---------------------------------------------------------------------------
step "0/6 Sprawdzam, czy można zaczynać"

[[ "${EUID}" -eq 0 ]] || fail "uruchom skrypt przez: sudo bash $0"
command -v tailscale >/dev/null 2>&1 || fail "brak polecenia tailscale."
[[ -f "${CONF_SRC}" ]] || fail "brak pliku ${CONF_SRC}. Skopiuj go obok skryptu."
[[ -d "${SITE_DIR}" ]] || fail "brak folderu kursu ${SITE_DIR}."

if [[ -e "${POLICY}" ]] && ! grep -Fq "${POLICY_MARK}" "${POLICY}"; then
  fail "istnieje obcy plik ${POLICY}. Niczego nie zmieniłem."
fi

state="$(serve_state)"
[[ "${state}" != "inny" ]] || fail "tailscale serve ma nieznane ustawienia. Niczego nie zmieniłem."
echo "tailscale serve: ${state}."

if ! systemctl is-active --quiet nginx && ss -tlnH | awk '{print $4}' | grep -Fxq "${LISTEN}"; then
  fail "port ${LISTEN} jest zajęty przez inny program. Niczego nie zmieniłem."
fi
echo "Można zaczynać."

# ---------------------------------------------------------------------------
step "1/6 Aktualizuję pakiety (aktualizacja Tailscale chwilowo przerwie połączenia przez Tailscale)"

apt-get update
apt-get "${APT_OPTS[@]}" upgrade

if [[ -f /var/run/reboot-required ]]; then
  echo
  echo "STOP: po aktualizacjach serwer wymaga restartu. Skrypt NIE restartuje serwera."
  echo "Pakiety, które tego wymagają:"
  cat /var/run/reboot-required.pkgs 2>/dev/null || echo "(brak listy)"
  echo "Zrestartuj serwer, a potem uruchom ten skrypt jeszcze raz."
  exit 2
fi
echo "Aktualizacje gotowe. Restart nie jest potrzebny."

# ---------------------------------------------------------------------------
step "2/6 Instaluję nginx (bez uruchamiania)"

if dpkg-query -W -f='${Status}' nginx 2>/dev/null | grep -q "install ok installed"; then
  echo "nginx jest już zainstalowany."
else
  # policy-rc.d (mechanizm Debiana): kod 101 zabrania instalatorowi uruchomić nginx.
  # Domyślna strona nginx słuchałaby na porcie 80 na wszystkich adresach.
  # Inne usługi uruchamiają się normalnie. Plik znika zaraz po instalacji.
  cat >"${POLICY}" <<EOF
#!/bin/sh
${POLICY_MARK}
# Blokuje tylko uruchomienie nginx w trakcie instalacji.
while [ \$# -gt 0 ]; do
  case "\$1" in
    --*) shift ;;
    *) break ;;
  esac
done
case "\$1" in
  nginx|nginx.service) exit 101 ;;
esac
exit 0
EOF
  chmod 755 "${POLICY}"
  trap 'rm -f "${POLICY}"' EXIT

  apt-get "${APT_OPTS[@]}" install nginx

  rm -f "${POLICY}"
  trap - EXIT
  echo "nginx zainstalowany."
fi
# Usuwa także plik policy-rc.d pozostały po przerwanym wcześniej uruchomieniu skryptu.
rm -f "${POLICY}"

# Zabezpieczenie: gdyby nginx mimo wszystko działał na innych adresach — zatrzymaj go.
if systemctl is-active --quiet nginx && [[ "$(nginx_addresses)" != "${LISTEN}" ]]; then
  systemctl stop nginx
  fail "nginx słuchał na innych adresach niż ${LISTEN}. Zatrzymałem go."
fi

# ---------------------------------------------------------------------------
step "3/6 Wpisuję ustawienia kursu i wyłączam domyślną stronę nginx"

install -m 644 -o root -g root "${CONF_SRC}" "${CONF_DST}"
ln -sfn "${CONF_DST}" "${CONF_LINK}"

if [[ -L "${DEFAULT_LINK}" ]]; then
  rm -f "${DEFAULT_LINK}"
  echo "Wyłączyłem domyślną stronę nginx."
elif [[ -e "${DEFAULT_LINK}" ]]; then
  fail "${DEFAULT_LINK} jest zwykłym plikiem, a nie skrótem. Niczego więcej nie zmieniłem."
fi
echo "Ustawienia kursu: ${CONF_DST}."

# ---------------------------------------------------------------------------
step "4/6 Sprawdzam ustawienia (nginx -t) i uruchamiam nginx"

nginx -t

systemctl enable --quiet nginx
if systemctl is-active --quiet nginx; then
  systemctl reload nginx
else
  systemctl start nginx
fi

for _ in $(seq 1 10); do
  [[ "$(nginx_addresses)" == "${LISTEN}" ]] && break
  sleep 1
done
if [[ "$(nginx_addresses)" != "${LISTEN}" ]]; then
  systemctl stop nginx
  fail "nginx nie słucha wyłącznie na ${LISTEN}. Zatrzymałem go. tailscale serve bez zmian."
fi
curl -fsS -o /dev/null "${LOCAL_URL}/" || fail "nginx nie zwraca strony głównej kursu. tailscale serve bez zmian."
echo "nginx działa i słucha tylko na ${LISTEN}."

# ---------------------------------------------------------------------------
step "5/6 Przełączam tailscale serve z folderu na nginx"

# Po aktualizacji Tailscale może potrzebować chwili na ponowne połączenie.
for _ in $(seq 1 30); do
  tailscale status >/dev/null 2>&1 && break
  sleep 1
done
tailscale status >/dev/null 2>&1 || fail "Tailscale nie odpowiada. tailscale serve bez zmian."

state="$(serve_state)"
case "${state}" in
  nginx)
    echo "tailscale serve już przekazuje ruch do nginx."
    ;;
  folder)
    tailscale serve --https=443 "${SITE_DIR}" off
    tailscale serve --bg --https=443 "${LOCAL_URL}"
    [[ "$(serve_state)" == "nginx" ]] || fail "przełączenie tailscale serve się nie udało. Stan: tailscale serve status"
    echo "Przełączone."
    ;;
  *)
    fail "tailscale serve ma nieznane ustawienia. Niczego nie przełączyłem."
    ;;
esac

# ---------------------------------------------------------------------------
step "6/6 Sprawdzenie"

check_headers() {
  local path="$1" want_type="$2" headers
  headers="$(curl -fsSI "${LOCAL_URL}${path}")"
  echo "-- ${path}"
  echo "${headers}"
  grep -qi '^cache-control: no-cache' <<<"${headers}" || fail "${path}: brak Cache-Control: no-cache."
  grep -qi '^etag:' <<<"${headers}" || fail "${path}: brak ETag."
  grep -Eqi "^content-type: ${want_type}" <<<"${headers}" || fail "${path}: zły typ pliku."
  if grep -qi '^server: nginx/' <<<"${headers}"; then
    fail "${path}: nginx ujawnia numer wersji."
  fi
}

check_headers "/" "text/html"
# Typ plików .js zależy od wersji listy typów nginx; oba są poprawne.
check_headers "/app.js" "(application|text)/javascript"
check_headers "/manifest.webmanifest" "application/manifest\+json"

echo
echo "-- Adresy, na których słucha nginx:"
nginx_addresses
[[ "$(nginx_addresses)" == "${LISTEN}" ]] || fail "nginx słucha nie tylko na ${LISTEN}."
if ss -tlnH | awk '{print $4}' | grep -Eq ':80$'; then
  fail "coś słucha na porcie 80."
fi

echo
echo "-- tailscale serve status:"
tailscale serve status

echo
echo "-- hermes-gateway:"
systemctl is-active hermes-gateway || fail "hermes-gateway nie działa."

echo
echo "-- Usługi do ponownego uruchomienia po aktualizacjach (tylko lista, nic nie restartowałem):"
needrestart -b || echo "(needrestart nie zwrócił listy)"

echo
echo "== Podsumowanie"
echo "- Pakiety zaktualizowane, restart serwera nie był potrzebny."
echo "- nginx słucha tylko na ${LISTEN} i wysyła pliki kursu z Cache-Control: no-cache i ETag."
echo "- tailscale serve przekazuje ruch z portu 443 do nginx (tylko w sieci Tailscale)."
echo "- Hermes działa. deploy.sh wgrywa pliki do ${SITE_DIR} jak dotąd."
echo "Teraz: sprawdź nagłówki z Maca i kurs na iPhonie."
