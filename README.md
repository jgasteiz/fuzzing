# Fuzzing CMS

## How to run the thing
- Clone the repo `git@github.com:jgasteiz/fuzzing-cms.git`
- Create virtualenv and install requirements: `mkvirtualenv fuzzing && pip install -r requirements.txt`
- Run `./syncdb.sh`
- Run `./serve.sh`

## Restore postgres database from sql backup

dropdb larevolta
createdb larevolta
psql dbname < filename.sql