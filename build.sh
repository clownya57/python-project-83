#!/usr/bin/env bash

set -Eeuo pipefail

curl -LsSf https://astral.sh/uv/install.sh | sh
source "$HOME/.local/bin/env"

make install

psql \
  -v ON_ERROR_STOP=1 \
  -a \
  -d "$DATABASE_URL" \
  -f database.sql
