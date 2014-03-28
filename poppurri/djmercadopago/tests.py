#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Test cases for djmercadopago application models.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


import uuid
from mock import Mock, patch

from django.test import TestCase
from django.test.utils import override_settings

from .models import PaymentPreferenceManager, PaymentPreference


class PaymentPreferenceManagerTestCase(TestCase):
    """
    Tests the behaviour of class
    :model:`djmercadopago.PaymentPreferenceManager`.
    """
    def setUp(self):
        super(PaymentPreferenceManagerTestCase, self).setUp()
        self._manager = PaymentPreference.objects

        self._preference_return = {
            'response': {
                'items': [{
                    'title': 'Test title',
                    'quantity': 1,
                    'unit_price': '6.75',
                    'currency_id': 'ARS',
                    'id': '234',
                    'description': 'Test item description',
                    'picture_url': 'http://localhost/404.gif',
                }],
                'payer': {
                    'name': 'John',
                    'surename': 'Doe',
                    'email': 'john.doe@example.com',
                },
                'back_urls': {
                    'success': 'http://localhost/success/',
                    'failure': 'http://localhost/failure/',
                    'pending': 'http://localhost/pending/',
                },
                'id': '23',
                'init_point': 'http://localhost/init_point/',
                'sandbox_init_point': 'http://localhost/sandbox_init_point/',
                'external_reference': str(uuid.uuid4()).replace('-', ''),
                'date_created': '2011-08-16T21:28:42.606-04:00',
            }
        }

    def tearDown(self):
        super(PaymentPreferenceManagerTestCase, self).tearDown()

    @patch('djmercadopago.models._CLIENT')
    def test_create(self, mp_mock):

        mp_mock.create_preference.return_value = self._preference_return
        pp = self._manager.create({
            'items': [{
                'title': 'Test title payment',
                'quantity': '1',
                'currency_id': 'ARS',
                'unit_price': '0',
            }]
        })

        print pp
