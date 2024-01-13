#!/bin/bash

# Realizar las migraciones de Django
echo "Run migrations auto"
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

# Recopilar archivos estáticos
python3 manage.py collectstatic --clear
python3 manage.py collectstatic --noinput

# Iniciar Gunicorn con la opción --static-map para servir archivos estáticos
echo "Init server"
gunicorn billing.wsgi:application --bind 0:8000
exec "$@"
