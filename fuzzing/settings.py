import os
from django.utils.translation import ugettext_lazy as _


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


SECRET_KEY = 'sr+$itn8!+a#i-=!uz--$f5g8gb)gf@4$frvoi4&2o8_+2u@7r'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_URL = "http://eltallerdeasier.com"

ALLOWED_HOSTS = []

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'fuzzing/templates')
)

# Application definition


DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    'fuzzing.core',
    'fuzzing.cms',
    'fuzzing.website',
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS

INSTALLED_APPS += (
    'reversion',
    'tinymce',
    'south',
    'crispy_forms',
    'gunicorn',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'fuzzing.urls'

WSGI_APPLICATION = 'fuzzing.wsgi.application'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


LANGUAGE_CODE = 'en-us'
LANGUAGES = (
    ('es', _('Spanish')),
    ('en', _('English')),
    ('eu', _('Euskara'))
)


# MODELTRANSLATION_FALLBACK_LANGUAGES = ('es', )
# MODELTRANSLATION_AUTO_POPULATE = False
# MODELTRANSLATION_LOADDATA_RETAIN_LOCALE = True

# MODELTRANSLATION_TRANSLATION_FILES = (
#     'fuzzing.core.translation',
# )


LANGUAGES_DICT = dict(LANGUAGES)
LANGUAGE_COOKIE_NAME = 'user_language'

TIME_ZONE = 'UTC'

### Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'fuzzing/static'),
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
UPLOADS_ROOT = 'uploads'

LOGIN_REDIRECT_URL = '/cms/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = '/cms/login/'
LOGOUT_URL = '/cms/logout/'



THEME_CHOICES = (
    ('larevolta', 'La Revolta'),
    ('taller', 'Taller de Asier'),
)

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}

DEBUG_TOOLBAR_PATCH_SETTINGS = False

try:
    from local_settings import *
except ImportError:
    pass
