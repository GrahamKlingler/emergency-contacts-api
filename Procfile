release: python manage.py makemigrations emergency-contacts
python manage.py migrate
web: gunicorn api_test.wsgi:application --log-file -