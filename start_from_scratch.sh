rm -rf postgres/db-data
# change settings
cd django_project

python manage.py makemigrations works
python manage.py migrate

export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_EMAIL=admin@example.com
export DJANGO_SUPERUSER_PASSWORD=123321
python manage.py createsuperuser --noinput

# django manage.py runserver 8080
