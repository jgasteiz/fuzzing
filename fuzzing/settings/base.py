import os

from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext_lazy as _

def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return os.environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TIME_ZONE = 'Europe/Madrid'

SECRET_KEY = get_env_setting("SECRET_KEY")

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

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
    'modeltranslation',
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


### Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'))

LANGUAGE_CODE = 'es'
LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
    ('eu', _('Euskara'))
)

MODELTRANSLATION_FALLBACK_LANGUAGES = ('es', )
MODELTRANSLATION_AUTO_POPULATE = False
MODELTRANSLATION_LOADDATA_RETAIN_LOCALE = True

MODELTRANSLATION_TRANSLATION_FILES = (
    'fuzzing.core.translation',
)

LANGUAGES_DICT = dict(LANGUAGES)
LANGUAGE_COOKIE_NAME = 'user_language'



STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates/'),
)

STATIC_ROOT = os.path.join(BASE_DIR)
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

CRISPY_TEMPLATE_PACK = 'bootstrap3'

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}

