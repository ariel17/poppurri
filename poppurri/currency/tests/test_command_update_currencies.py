#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Test units for manager command ```update_currencies```.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


import json
from mock import patch, Mock
from decimal import Decimal

from django.test import TestCase
from django.test.utils import override_settings

from currency.management.commands import update_currencies
from currency.models import Currency


class UpdateCurrenciesTestCase(TestCase):
    """
    Test case for ```update_currencies``` command.
    """
    def setUp(self):
        super(UpdateCurrenciesTestCase, self).setUp()
        Currency.objects.all().delete()
        self._command = update_currencies.Command()

    def tearDown(self):
        super(UpdateCurrenciesTestCase, self).tearDown()
        Currency.objects.all().delete()

    @override_settings(CURRENCY_DEFAULT='ARS')
    @patch('currency.management.commands.update_currencies.requests')
    def test_handle_ok_with_default(self, mock_requests):
        """
        Requests to API results in a HTTP OK status and updates executed
        successful. Default currency is setted and processed.
        """
        json_response = {
            'USD-PHP': {'val': Decimal('10.00'), },
            'USD-ARS': {'val': Decimal('5.00'), },
        }

        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = json_response

        mock_requests.get.return_value = mock_response
        self._command.execute('php')

        self.assertEquals(2, Currency.objects.all().count())
        self.assertEquals(json_response['USD-PHP']['val'],
                          Currency.objects.get(code='PHP').value)

    @override_settings(CURRENCY_DEFAULT=None)
    @patch('currency.management.commands.update_currencies.requests')
    def test_handle_ok_without_default(self, mock_requests):
        """
        Requests to API results in a HTTP OK status and updates executed
        successful. Default currency is not setted.
        """
        json_response = {
            'USD-PHP': {'val': Decimal('10.00'), },
        }

        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = json_response

        mock_requests.get.return_value = mock_response
        self._command.execute('php')

        self.assertEquals(1, Currency.objects.all().count())
        self.assertEquals(json_response['USD-PHP']['val'],
                          Currency.objects.get(code='PHP').value)

    @override_settings(CURRENCY_DEFAULT=None)
    @patch('currency.management.commands.update_currencies.requests')
    def test_handle_fail_404(self, mock_requests):
        """
        Requests to API results in a HTTP 404 status.
        """
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = \
            Exception('Mocked exception U.U')

        mock_requests.get.return_value = mock_response
        self._command.execute('php')

        self.assertEquals(0, Currency.objects.all().count())

    @override_settings(CURRENCY_DEFAULT=None)
    @patch('currency.management.commands.update_currencies.requests')
    def test_handle_currency_not_found(self, mock_requests):
        """
        Requests to API results in a HTTP 404 status.
        """
        json_response = {}

        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = json_response

        mock_requests.get.return_value = mock_response
        self._command.execute('php')

        self.assertEquals(0, Currency.objects.all().count())
