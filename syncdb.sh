dropdb 'larevolta'
createdb 'larevolta'
python manage.py syncdb --noinput --migrate
# python manage.py loaddata data.json
