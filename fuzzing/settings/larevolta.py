from .common import *

DEBUG = False

MODELTRANSLATION_DEFAULT_LANGUAGE = 'es'

LOCALE_PATHS = (
    '/Users/javi/dev/fuzzing/locale',
)

DISPLAY_LANGUAGES = (
    'en',
    'es',
    'ca',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'larevolta',
        'USER': 'larevolta',
    }
}
