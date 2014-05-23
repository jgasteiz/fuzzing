# Fuzzing CMS

## How to run the thing
- Clone the repo `git@github.com:jgasteiz/fuzzing-cms.git`
- Create virtualenv and install requirements: `mkvirtualenv fuzzing && pip install -r requirements.txt`
- Run `./syncdb.sh`
- Run `./serve.sh`

## Optional - Create a postgresql database for local development

- `psql postgres`
- `CREATE USER username;`
- `CREATE DATABASE dbname;`
- `GRANT ALL PRIVILEGES ON DATABASE dbname to username;`

## Optional - Restore postgres database from sql backup

- `dropdb dbname`
- `createdb dbname`
- `psql dbname < filename.sql`