#!/usr/bin/env bash
set -e

python3 manage.py flush --no-input
python3 manage.py migrate

exec "$@"