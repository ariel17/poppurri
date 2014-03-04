#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Requests to "The Free Currency Converter API" for new values on
currency equivalences and updates the values stored in model.

API URL: http://www.freecurrencyconverterapi.com/
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"

from decimal import Decimal
import logging
import requests

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.management.base import BaseCommand

from currency.models import Currency


LOGGER = logging.getLogger(__name__)

API_URL = 'http://www.freecurrencyconverterapi.com/api/convert?compact=y&q={0}'

key = 'CURRENCY_FROM'
if not hasattr(settings, key):
    raise ImproperlyConfigured('Missing required configuration: %r' % (key, ))


class Command(BaseCommand):
    args = '<code1 code2 ...>'
    help = 'Collects currency equivalences to update the values stored in '\
           'model. It can be called with specific codes to update; if none '\
           'is indicated then all currencies will be updated.'
    with_errors = False

    def handle(self, *args, **options):
        self.stdout.write('> Updating currencies...')

        args = list(args)
        if settings.CURRENCY_DEFAULT and settings.CURRENCY_DEFAULT not in args:
            args.append(settings.CURRENCY_DEFAULT)

        for code in args:
            code = code.upper()
            key = '%s-%s' % (settings.CURRENCY_FROM, code.upper())
            LOGGER.debug("Key to use: %r" % (key, ))

            url = API_URL.format(key)
            LOGGER.info("Request for Currency API updates: %r" % url)

            try:
                response = requests.get(url)
                response.raise_for_status()
                value = response.json()[key]['val']
            except:
                self.with_errors = True
                LOGGER.exception('Failed requesting Currency API updates:')
                continue

            currency, created = Currency.objects.get_or_create(code=code)
            currency.value = Decimal(value)
            currency.save()

            LOGGER.info("%s -> %d" % (code, currency.value))

        if self.with_errors:
            self.stdout.write('** ERROR: Check logs for details. **')

        self.stdout.write('> Done.')
