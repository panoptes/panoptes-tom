#!/bin/sh


# echo "Starting nginx reverse-proxy"
# sudo nginx -c nginx.conf

python manage.py flush --no-input
python manage.py migrate

exec "$@"