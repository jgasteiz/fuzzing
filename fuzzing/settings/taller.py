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

LANGUAGES = (
    ('en', gettext(u'English')),
    ('es', gettext(u'Castellano')),
    ('eu', gettext(u'Euskara')),
    ('fr', gettext(u'Français')),
)

SITE_THEME = 'taller'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'taller',
        'USER': 'taller',
        'PASSWORD': 'taller',
    }
}
