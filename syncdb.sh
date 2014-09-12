rm fuzzing/db.sqlite3
python manage.py syncdb --noinput --migrate
python manage.py createsuperuser

# python manage.py loaddata data.json
