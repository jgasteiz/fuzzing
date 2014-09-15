from .common import *

DEBUG = False

MODELTRANSLATION_DEFAULT_LANGUAGE = 'es'

LOCALE_PATHS = (
    '/opt/larevolta/fuzzing/locale',
)

DISPLAY_LANGUAGES = (
    'en',
    'es',
    'ca',
)

SITE_THEME = 'larevolta'

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
