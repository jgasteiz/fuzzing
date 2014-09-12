# -*- coding: utf-8 -*-
"""Production settings and globals."""
from __future__ import absolute_import
from os import environ

from .base import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG

SITE_URL = "http://example-site.com"

ALLOWED_HOSTS = ['www.example-site.com',]
INTERNAL_IPS = ('127.0.0.1',)

INSTALLED_APPS += (
    # 'debug_toolbar',
)

SECRET_KEY = get_env_setting("SECRET_KEY")

EMAIL_SENDER = ''
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_PORT = environ.get('EMAIL_PORT', 587)
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'info@example.com')
EMAIL_HOST_PASSWORD = get_env_setting('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
# EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# # See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = 'admin@example.com' # emails for errors

# # See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
# CACHES = {}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fuzzing_db',
        'USER': 'admin',
        'PASSWORD': get_env_setting('DB_ADMIN_PASS'),
        'HOST': 'localhost',
        'PORT': '',
    }
}

# https://docs.djangoproject.com/en/1.6/topics/http/sessions/#module-django.contrib.sessions
# SESSION_ENGINE = ''
