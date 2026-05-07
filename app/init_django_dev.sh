#!/bin/bash
python3 manage.py makemigrations
python3 manage.py makemigrations base
python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput
python3 manage.py loaddata fixtures/admin.json