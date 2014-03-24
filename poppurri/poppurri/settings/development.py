#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Development settings and globals.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from os.path import join, normpath

from base import *


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'poppurri_dev',
        'USER': 'poppurri_dev',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        'LOCATION': 'localhost:11211',
        'KEY_PREFIX': 'development-',
    }
}
########## END CACHE CONFIGURATION


########## TOOLBAR CONFIGURATION
# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INSTALLED_APPS += (
    'debug_toolbar',
)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INTERNAL_IPS = ('127.0.0.1',)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)


# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TEMPLATE_CONTEXT': True,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
}
########## END TOOLBAR CONFIGURATION


MEDIA_URL = 'https://development.poppurri.com.ar/media/'
STATIC_URL = 'https://development.poppurri.com.ar/static/'


########## MIXTURE CONFIGURATION
MIXTURE_MAX_RATE = 0
########## END MIXTURE CONFIGURATION


########## WEB CONFIGURATION
WEB_CAROUSEL_MIXTURE_COUNT = 10
WEB_CATEGORIES_COUNT = 3
########## END WEB CONFIGURATION


########## sorl-thumbnail CONFIGURATION
THUMBNAIL_DEBUG = DEBUG
########## END sorl-thumbnail CONFIGURATION


########## GOOGLE ANALYTICS CONFIGURATION
USE_GOOGLE_ANALYTICS = False
########## END GOOGLE ANALYTICS CONFIGURATION


########## SENTRY CONFIGURATION
RAVEN_CONFIG = {
    'dsn': 'http://d259cd5e06994dcf838b58193002df1d:eda1d02a4b15401984bcac1209af9203@sentry.ariel17.com.ar/6',
}
########## END SENTRY CONFIGURATION


for logger in LOGGING['loggers'].keys():
    LOGGING['loggers'][logger]['level'] = 'DEBUG'
    LOGGING['loggers'][logger]['handlers'] = ['sentry', 'console']


# vim: ai ts=4 sts=4 et sw=4 ft=python
