# coding=utf-8
from .common import *

DEBUG = False

MODELTRANSLATION_DEFAULT_LANGUAGE = 'es'

LOCALE_PATHS = (
    '/Users/javi/dev/fuzzing/locale',
)

DISPLAY_LANGUAGES = (
    'en',
    'es',
    'eu',
    'fr',
)

SITE_THEME = 'taller'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'taller',
        'USER': 'taller',
        # 'PASSWORD': get_env_setting("DB_ADMIN_PASS"),
        'PASSWORD': 'taller',
    }
}
