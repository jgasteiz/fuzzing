"""
Django settings for fuzzing-cms project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sr+$itn8!+a#i-=!uz--$f5g8gb)gf@4$frvoi4&2o8_+2u@7r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'fuzzing/templates')
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'reversion',
    'tinymce',
    'south',
    'crispy_forms',
    'debug_toolbar',
    'fuzzing.core',
    'fuzzing.cms',
    'fuzzing.website',
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

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

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
