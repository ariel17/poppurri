#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Common settings and globals.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.utils.translation import ugettext_lazy as _
from os import environ
from os.path import abspath, basename, dirname, join, normpath
from sys import path

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)


########## PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)
########## END PATH CONFIGURATION


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Ariel Gerardo Rios', 'ariel.gerardo.rios@gmail.com'),
    ('Telma Soledad Euler', 'telmoke@hotmail.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION

########## GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'UTC'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'es-ar'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
########## END GENERAL CONFIGURATION


########## MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
########## END STATIC FILE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key should only be used for development and testing.
SECRET_KEY = r"$n#(&3z8531p0@7&30w0x3*m66vb-l=ej4x-+f5hyi6*8adl1s"
########## END SECRET CONFIGURATION


########## SITE CONFIGURATION
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []
########## END SITE CONFIGURATION


########## FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    normpath(join(SITE_ROOT, 'fixtures')),
)
########## END FIXTURE CONFIGURATION


########## TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'poppurri.context_processors.current_site.current_site',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'settings_context_processor.context_processors.settings',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    normpath(join(SITE_ROOT, 'templates')),
)
########## END TEMPLATE CONFIGURATION


########## MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
    # Default Django middleware.
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # Adds some attributes missing in the request object from Django 1.6.
    'poppurri.middlewares.BodyMiddleware',
)
########## END MIDDLEWARE CONFIGURATION


########## URL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = '%s.urls' % SITE_NAME
########## END URL CONFIGURATION


########## APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    # 'django.contrib.humanize',

    # Admin panel and documentation:
    'django.contrib.admin',
    'django.contrib.admindocs',
)

THIRD_PARTY_APPS = (
    # Database migration helpers:
    'south',
    # Rating implementation
    'djangoratings',
    # thumbnails generator
    'sorl.thumbnail',
    # Add settings configuration to context processor for templates
    'settings_context_processor',
    # Translation
    'rosetta',
    # Sentry error notification
    'raven.contrib.django.raven_compat',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    'category',
    'common',
    'currency',
    'mixture',
    'search',
    'user_profile',
    'web',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION


########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['sentry'],
            'level': 'ERROR',
            'propagate': True,
        },
        'contact_form': {
            'handlers': ['sentry'],
            'level': 'ERROR',
            'propagate': True,
        },
        'mixture': {
            'handlers': ['sentry'],
            'level': 'ERROR',
            'propagate': True,
        },
        'category': {
            'handlers': ['sentry'],
            'level': 'ERROR',
            'propagate': True,
        },
        'web': {
            'handlers': ['sentry'],
            'level': 'ERROR',
            'propagate': True,
        },
        'currency': {
            'handlers': ['sentry'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
########## END LOGGING CONFIGURATION


########## WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME
########## END WSGI CONFIGURATION


########## COMMON CONFIGURATION
IMAGES_ROOT = "img"
IMAGES_DEFAULT = join(IMAGES_ROOT, 'no-img.png')
########## END COMMON CONFIGURATION


########## MIXTURE CONFIGURATION
MIXTURES_IMAGES_PATH = join(IMAGES_ROOT, 'mixtures')
MIXTURES_MIN_RATE = 0
MIXTURE_LIST_MAX_ITEMS = 10
########## END MIXTURE CONFIGURATION


########## WEB CONFIGURATION
WEB_CAROUSEL_MIXTURE_COUNT = 10
WEB_CATEGORIES_COUNT = 3
########## END WEB CONFIGURATION


########## SEARCH CONFIGURATION
SEARCH_QUERY_PARAM = "q"
########## END SEARCH CONFIGURATION


########## AUTHOR CONFIGURATION
AUTHOR_IMAGES_PATH = join(IMAGES_ROOT, 'mixtures')
########## END AUTHOR CONFIGURATION


########## USER PROFILE CONFIGURATION
USER_PROFILE_DEFAULT_IMAGE_URL = join('img', 'generic-user.png')
########## END USER PROFILE CONFIGURATION


########## SETTINGS CONTEXT PROCESSOR CONFIGURATION
TEMPLATE_VISIBLE_SETTINGS = (
    'SEARCH_QUERY_PARAM',
    'USE_GOOGLE_ANALYTICS',
    'USER_PROFILE_DEFAULT_IMAGE_URL',
)
########## END SETTINGS CONTEXT PROCESSOR CONFIGURATION


LOCALE_PATHS = (
    join(SITE_ROOT, 'locale'),
)

LANGUAGES = (
    ('es', _('Spanish')),
    ('en', _('English')),
)


######### CURRENCY CONFIGURATION
CURRENCY_DEFAULT = 'ARS'
CURRENCY_FROM = 'USD'
######### CURRENCY CONFIGURATION


# vim: ai ts=4 sts=4 et sw=4 ft=python
