#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Test cases for djmercadopago application models.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


import uuid
from mock import patch

from django.test import TestCase

from .models import PaymentPreference, PaymentType, PaymentMethod


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
                'payment_methods': {
                    'excluded_payment_methods': [{
                        'id': 'amex',
                    }],
                    'excluded_payment_types': [{
                        'id': 'ticket',
                    }],
                    'installments': 12,
                },
                'id': '23',
                'init_point': 'http://localhost/init_point/',
                'sandbox_init_point': 'http://localhost/sandbox_init_point/',
                'external_reference': str(uuid.uuid4()).replace('-', ''),
                'date_created': '2011-08-16T21:28:42.606-04:00',
            }
        }

        pt_card = PaymentType.objects.create(
            mercadopago_id='credit_card',
            name='Credit Card',
        )

        PaymentType.objects.create(
            mercadopago_id='ticket',
            name='Ticket',
        )

        PaymentMethod.objects.create(
            mercadopago_id='amex',
            name='American Express',
            payment_type=pt_card,
            thumbnail='http://localhost/404.gif',
            secure_thumbnail='https://localhost/404.gif'
        )

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

        # self.assertEquals(pp.items)
        # slf.assertEquals(pp.payer)
        # self.assertEquals(pp.back_urls)

        excluded_methods = pp.excluded_payment_methods.all().values_list(
            'mercadopago_id', flat=True
        )
        self.assertEquals(
            len(self._preference_return['response']['payment_methods']['excluded_payment_methods']),
            pp.excluded_payment_methods.all().count()
        )
        for method in self._preference_return['response']['payment_methods']['excluded_payment_methods']:
            self.assertTrue(method['id'] in excluded_methods)

        excluded_types = pp.excluded_payment_types.all().values_list(
            'mercadopago_id', flat=True
        )
        self.assertEquals(
            len(self._preference_return['response']['payment_methods']['excluded_payment_types']),
            pp.excluded_payment_types.all().count()
        )
        for p_type in self._preference_return['response']['payment_methods']['excluded_payment_types']:
            self.assertTrue(p_type['id'] in excluded_types)

        self.assertEquals(
            self._preference_return['response']['payment_methods']['installments'],
            pp.installments
        )
        # self.assertEquals(pp.external_reference)
        # self.assertEquals(pp.collector_id)
        # self.assertEquals(pp.init_point)
        # self.assertEquals(pp.sandbox_init_point)
        # self.assertEquals(pp.date_created)
