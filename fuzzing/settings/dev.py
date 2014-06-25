from .common import *

DEBUG = True

gettext = lambda s: s
LANGUAGES = (
    ('en', gettext('EN')),
    ('ca', gettext('CAT')),
    ('es', gettext('CAST')),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'es'

LOCALE_PATHS = (
    '/Users/javi/dev/fuzzing/locale',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'larevolta',
        'USER': 'larevolta',
    }
}
