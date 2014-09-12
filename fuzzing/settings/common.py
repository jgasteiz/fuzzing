# coding=utf-8
"""
Django settings for fuzzing-cms project.
"""
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return os.environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)

SITE_URL = "http://localhost:8000"

# SECRET_KEY = get_env_setting("SECRET_KEY")
SECRET_KEY = 'sr+$itn8!+a#i-=!uz--$f5g8gb)gf@4$frvoi4&2o8_+2u@7r'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
)

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '188.226.146.75', '188.226.222.173']


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
    'localeurl',
    'reversion',
    'tinymce',
    'south',
    'gunicorn',
    'modeltranslation',
    'crispy_forms',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'localeurl.middleware.LocaleURLMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    "fuzzing.cms.context_processors.i18n_extended",
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

gettext = lambda s: s
LANGUAGES = (
    ('en', gettext(u'English')),
    ('eu', gettext(u'Euskara')),
    ('es', gettext(u'Castellano')),
    ('ca', gettext(u'Castellano')),
    ('fr', gettext(u'Français')),
)


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'fuzzing/../templates')
)

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'fuzzing/../static'),
)

STATIC_URL = '/static/'
UPLOADS_ROOT = 'uploads'

LOGIN_REDIRECT_URL = '/cms/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = '/cms/login/'
LOGOUT_URL = '/cms/logout/'

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}

DEBUG_TOOLBAR_PATCH_SETTINGS = False

SITE_THEME = 'taller'
DISPLAY_LANGUAGES = ()
