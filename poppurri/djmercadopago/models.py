#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Payment models for MercadoPago API.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.db import models
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


REQUIRED_SETTINGS = ['MERCADOPAGO_ACCESS_TOKEN',]

for key in REQUIRED_SETTINGS:
    if not getattr(settings, key):
        raise ImproperlyConfigured('Missing required setting: %s' % key)

ACCESS_TOKEN = settings.MERCADOPAGO_ACCESS_TOKEN


class 
