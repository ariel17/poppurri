#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Project configuration for testing.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from base import *


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = 'smtp.gmail.com'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = 'password'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = 'info@poppurri.com.ar'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = 587

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER

# See: https://docs.djangoproject.com/en/dev/ref/settings/#default-from-email 
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# See: https://docs.djangoproject.com/en/dev/ref/settings/#send-broken-link-emails 
SEND_BROKEN_LINK_EMAILS = True
########## END EMAIL CONFIGURATION


########## IN-MEMORY TEST DATABASE CONFIGURATION
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}
########## END IN-MEMORY TEST DATABASE CONFIGURATION

########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
########## END CACHE CONFIGURATION


########## TOOLBAR CONFIGURATION
INSTALLED_APPS += (
    'coverage',
)


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


for logger in LOGGING['loggers'].keys():
    LOGGING['loggers'][logger]['level'] = 'DEBUG'
    LOGGING['loggers'][logger]['handlers'] = ['sentry', 'console']


SOUTH_TESTS_MIGRATE = False  # To disable migrations and use syncdb instead
SKIP_SOUTH_TESTS = True  # To disable South's own unit tests

# vim: ai ts=4 sts=4 et sw=4 ft=python
