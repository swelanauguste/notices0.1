#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py makemigrations
python manage.py migrate
#python manage.py makemigtrations
#python manage.py migrate
# python manage.py flush --no-input
python manage.py createsuperuser --username kingship --email kingship.lc@gmail.com --no-input
python manage.py add_category_list
python manage.py add_statuses
python manage.py collectstatic --no-input

exec "$@"
