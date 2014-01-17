#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Production settings and globals.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from base import *

import dj_database_url


########## HOST CONFIGURATION
# See: https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = ['*']
########## END HOST CONFIGURATION


########## DATABASE CONFIGURATION
DATABASES = {
    'default': dj_database_url.config(),
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

# vim: ai ts=4 sts=4 et sw=4 ft=python
