#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Production settings and globals.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


import os
from os import environ

from base import *


########## HOST CONFIGURATION
# See: https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = ['*']
########## END HOST CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'poppurri',
        'USER': 'poppurri',
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
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_env_setting('SECRET_KEY')
########## END SECRET CONFIGURATION


########## INSTALLED APPS
# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS += ('gunicorn',)
########## END INSTALLED APPS


########## MIXTURE CONFIGURATION
MIXTURE_MAX_RATE = 0
########## END MIXTURE CONFIGURATION


########## WEB CONFIGURATION
WEB_CAROUSEL_MIXTURE_COUNT = 10
WEB_CATEGORIES_COUNT = 3
########## END WEB CONFIGURATION


########## sorl-thumbnail CONFIGURATION
THUMBNAIL_DEBUG = DEBUG
THUMBNAIL_KVSTORE = u"sorl.thumbnail.kvstores.redis_kvstore.KVStore"
THUMBNAIL_REDIS_DB = u"poppurri"
########## END sorl-thumbnail CONFIGURATION


########## GOOGLE ANALYTICS CONFIGURATION
USE_GOOGLE_ANALYTICS = False
########## END GOOGLE ANALYTICS CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = 'localhost'

EMAIL_PORT = 25

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = 'root@poppurri.com.ar'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#default-from-email
DEFAULT_FROM_EMAIL = 'info@poppurri.com.ar'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#send-broken-link-emails 
SEND_BROKEN_LINK_EMAILS = True
########## END EMAIL CONFIGURATION


# vim: ai ts=4 sts=4 et sw=4 ft=python
