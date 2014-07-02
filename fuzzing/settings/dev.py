# coding=utf-8
from .common import *

gettext = lambda s: s

MODELTRANSLATION_DEFAULT_LANGUAGE = 'es'

LOCALE_PATHS = (
    '/Users/javi/dev/fuzzing/locale',
)

DISPLAY_LANGUAGES = [
    'en',
    'es',
    'eu',
    'fr',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'taller',
        'USER': 'taller',
    }
}