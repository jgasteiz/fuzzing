from .common import *

DEBUG = False

gettext = lambda s: s
LANGUAGES = (
    ('en', gettext('EN')),
    ('ca', gettext('CAT')),
    ('es', gettext('CAST')),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'es'

LOCALE_PATHS = (
    '/opt/larevolta/fuzzing/locale',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'larevolta',
        'USER': 'larevolta',
        'PASSWORD': 'Girasol13',
        'HOST': 'localhost',
        'PORT': '',
    }
}
