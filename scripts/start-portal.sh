#!/usr/bin/env bash
set -e

# Handle any DB migrations.
echo "Performing migrations"
# Uncomment below to flush db before starting.
#python manage.py flush --no-input

echo "Looking for ${SQL_DATABASE}."
python manage.py migrate

# Start the web server.
echo "Starting PANOPTES Tom"
python manage.py runserver 0.0.0.0:8080
