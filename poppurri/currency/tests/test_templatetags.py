#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Templatetags test units.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from decimal import Decimal

from django.conf import settings
from django.test import TestCase

from currency.models import Currency
from currency.templatetags.to_currency import to_currency


class ToCurrencyTestCase(TestCase):
    """
    Test unit for ```to_currency``` template tag.
    """
    def setUp(self):
        super(ToCurrencyTestCase, self).setUp()

    def tearDown(self):
        super(ToCurrencyTestCase, self).tearDown()

    def test_to_currency(self):
        """
        Tests a successful currency convertion, when the scale exists in model.
        """
        currency = Currency.objects.get(code='ARS')
        self.assertEquals(Decimal('13'),
                          to_currency(Decimal('1.55'), currency))

        currency = Currency.objects.get(code='USD')
        self.assertEquals(Decimal('2.0'),
                          to_currency(Decimal('1.55'), currency))
