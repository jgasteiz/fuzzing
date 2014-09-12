# coding=utf-8
import os
from .common import *

DEBUG = False

SITE_URL = "http://eltallerdeasier.com"

MODELTRANSLATION_DEFAULT_LANGUAGE = 'es'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale')
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
