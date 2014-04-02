rm dbname.sqlite
python manage.py syncdb --noinput --migrate
python manage.py loaddata larevolta.json