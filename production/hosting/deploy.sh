#!/usr/bin/env bash
# Wysyła aplikację kursu (app/dist/) na serwer hermes-vps, konto canonkurs.
# Uruchamiaj z Maca, z dowolnego miejsca w repozytorium:
#   bash production/hosting/deploy.sh
set -euo pipefail

REMOTE="canonkurs-vps"
REMOTE_DIR="/srv/canon-rp-kurs/"

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

SRC_DIR="app/dist/"

# 1. app/ musi być zapisane w Git i takie samo jak origin/main.
if [[ -n "$(git status --porcelain --untracked-files=no -- app/)" ]]; then
  echo "STOP: w app/ są niezapisane zmiany (git status). Najpierw je zapisz albo cofnij." >&2
  git status --short --untracked-files=no -- app/ >&2
  exit 1
fi

git fetch --quiet origin main
if ! git diff --quiet origin/main -- app/; then
  echo "STOP: app/ różni się od origin/main. Wgrywamy tylko wersję z main." >&2
  git diff --stat origin/main -- app/ >&2
  exit 1
fi

# 2. Wysyłka. --delete usuwa z serwera pliki, których nie ma już na Macu.
rsync -rlt --delete --exclude='.DS_Store' "$SRC_DIR" "$REMOTE:$REMOTE_DIR"

# 3. Podsumowanie.
total="$(find "$SRC_DIR" -type f ! -name '.DS_Store' | wc -l | tr -d ' ')"
canon="$(find "$SRC_DIR" -type f -name '*-canon.*' | wc -l | tr -d ' ')"
echo "Gotowe: wgrano aplikację na serwer."
echo "Plików na serwerze: $total, w tym rysunków Canon: $canon."
