# coding=utf-8
from .common import *

gettext = lambda s: s

MODELTRANSLATION_DEFAULT_LANGUAGE = 'es'

LOCALE_PATHS = (
    '/Users/javi/dev/fuzzing/locale',
)

DISPLAY_LANGUAGES = (
    'en',
    'es',
    'ca',
)

LANGUAGES = (
    ('en', gettext(u'English')),
    ('es', gettext(u'Castellano')),
    ('ca', gettext(u'Català')),
)

SITE_THEME = 'larevolta'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'larevolta',
        'USER': 'test',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '',
    }
}
