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
)

LANGUAGES = (
    ('en', gettext(u'English')),
    ('es', gettext(u'Castellano')),
)

SITE_THEME = 'taller'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'taller.db'
    }
}
