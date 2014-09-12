# -*- coding: utf-8 -*-
"Development isolated configuration"
from __future__ import absolute_import
from os import environ

from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = get_env_setting("SECRET_KEY")

INTERNAL_IPS = ('127.0.0.1',)
TIME_ZONE = 'Europe/Madrid'

SITE_URL = "http://localhost.com:8000"

INSTALLED_APPS += (
    # 'debug_toolbar',
)


EMAIL_SENDER = ''
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_PORT = environ.get('EMAIL_PORT', 587)
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'info@example.com')
EMAIL_HOST_PASSWORD = get_env_setting('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True


#SQLITE3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#Metrics
ANALYTICS_TRACKING_ID = 'UA-XXXXXXX-XX'

DEBUG_TOOLBAR_PATCH_SETTINGS = False

try:
    from local_settings import *
except ImportError:
    pass
