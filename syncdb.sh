# dropdb 'larevolta'
# createdb 'larevolta'
rm dbname.sqlite
python manage.py syncdb --noinput --migrate