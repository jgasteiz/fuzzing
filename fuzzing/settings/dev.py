# coding=utf-8
from .common import *

SITE_URL = "http://localhost:8000"

gettext = lambda s: s

MODELTRANSLATION_DEFAULT_LANGUAGE = 'es'
MODELTRANSLATION_TRANSLATION_FILES = (
    'fuzzing.core.translation',
)

LOCALE_PATHS = (
    '/Users/javi/dev/fuzzing/locale',
)

DISPLAY_LANGUAGES = (
    'en',
    'es',
    'eu',
    'fr',
)

INSTALLED_APPS += (
    'debug_toolbar',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'taller',
        'USER': 'taller',
    }
}
