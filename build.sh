#!/usr/bin/env bash

set -Eeuo pipefail

installer="$(mktemp)"
trap 'rm -f "$installer"' EXIT

curl \
  --proto '=https' \
  --proto-redir '=https' \
  --tlsv1.2 \
  --location \
  --fail \
  --silent \
  --show-error \
  --output "$installer" \
  https://astral.sh/uv/install.sh

sh "$installer"

source "$HOME/.local/bin/env"

make install

psql \
  -v ON_ERROR_STOP=1 \
  -a \
  -d "$DATABASE_URL" \
  -f database.sql
