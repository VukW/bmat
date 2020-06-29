#!/bin/bash
sleep 10
python3.7 manage.py makemigrations works
python3.7 manage.py migrate
python3.7 manage.py createsuperuser --noinput
python3.7 manage.py runserver 0.0.0.0:8000
