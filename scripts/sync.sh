#!/bin/bash
set -e

find . -name '*.pyc' -delete
rm -fr media/*
ls pycon/*/migrations | grep -v __init__.py | xargs rm -rf
rm -f dev_db.sqlite3

python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py createsuperuser --username=test --email=test@example.com
