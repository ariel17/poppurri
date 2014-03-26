#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Test cases for djmercadopago application models.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from mock import Mock, patch

from django.test import TestCase

from .models import PaymentPreferenceManager, PaymentPreference


class PaymentPreferenceManagerTestCase(TestCase):
    """
    Tests the behaviour of class
    :model:`djmercadopago.PaymentPreferenceManager`.
    """
    def setUp(self):
        super(PaymentPreferenceManagerTestCase, self).setUp()
        self._manager = PaymentPreferenceManager()

    def tearDown(self):
        super(PaymentPreferenceManagerTestCase, self).tearDown()

    @patch('djmercadopago.models._CLIENT')
    def test_create(self, mp_mock):
        print mp_mock
        self._manager.create({})
