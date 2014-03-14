rm db.sqlite3
python manage.py syncdb --noinput --migrate
# python manage.py loaddata data.json