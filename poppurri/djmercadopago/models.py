#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Payment models for MercadoPago API.
See: https://developers.mercadopago.com/
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from decimal import Decimal
import logging
import uuid

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.utils.translation import ugettext_lazy as _

import mercadopago


REQUIRED_SETTINGS = [
    'MERCADOPAGO_CLIENT_ID',
    'MERCADOPAGO_CLIENT_SECRET',
]

for key in REQUIRED_SETTINGS:
    if not hasattr(settings, key):
        raise ImproperlyConfigured('Missing required setting: %s' % key)

CLIENT_ID = settings.MERCADOPAGO_CLIENT_ID

CLIENT_SECRET = settings.MERCADOPAGO_CLIENT_SECRET

ACCESS_TOKEN = getattr(settings, 'MERCADOPAGO_ACCESS_TOKEN', None)

USE_SANDBOX = getattr(settings, 'MERCADOPAGO_USE_SANDBOX', False)

_CLIENT = mercadopago.MP(CLIENT_ID, CLIENT_SECRET)

LOGGER = logging.getLogger(__name__)


class PaymentType(models.Model):
    """
    Payment type or category.
    """
    mercadopago_id = models.CharField(
        _('MercadoPago id'),
        primary_key=True,
        max_length=50,
    )
    name = models.CharField(
        _('Name'),
        max_length=200,
        blank=True,
        null=True
    )


class PaymentMethod(models.Model):
    """
    The payment description.
    """
    mercadopago_id = models.CharField(
        _('MercadoPago id'),
        primary_key=True,
        max_length=50,
    )
    name = models.CharField(_('Name'), max_length=200)
    payment_type = models.ForeignKey(PaymentType)
    thumbnail = models.URLField(_('Thumbnail URL'), )
    secure_thumbnail = models.URLField(_('Secure thumbnail URL'), )


class PaymentItem(models.Model):
    """
    The item content description.
    """
    title = models.CharField(
        _('Title'),
        max_length=200,
        help_text=_('Mandatory; it will be shown on payment process.'),
    )
    quantity = models.PositiveIntegerField(
        _('Quantity'),
        help_text=_('Mandatory.'),
    )
    unit_price = models.DecimalField(
        _('Unit price'),
        max_digits=10,
        decimal_places=2,
        help_text=_('Mandatory.'),
    )
    currency_id = models.CharField(
        _('Currency type'),
        max_length=3,
        help_text=_(
            'mandatory. Argentina (argentinian peso): ARS, Brazil (Real): '
            'brl, Mexico (mexican peso): MXN, Venezuela (Strong Bolivar): '
            'vef, Colombia (colombian peso): COP'
        ),
    )
    picture_url = models.URLField(
        _('Image URL'),
        blank=True,
        null=True,
        default=None,
        help_text=_('Optional.'),
    )
    mercadopago_id = models.CharField(
        _('MercadoPago ID (aka code)'),
        max_length=200,
        blank=True,
        null=True,
        default=None,
        help_text=_('Optional.'),
    )
    description = models.CharField(
        _('description'),
        max_length=200,
        blank=True,
        null=True,
        default=None,
        help_text=_('Optional.'),
    )


class PaymentPayer(models.Model):
    """
    Payer user information.
    """
    name = models.CharField(
        _('Buyer name'),
        max_length=100,
        blank=True,
        null=True,
        default=None,
        help_text=_('Optional.'),
    )
    surename = models.CharField(
        _('Buyer surename'),
        max_length=100,
        blank=True,
        null=True,
        default=None,
        help_text=_('Optional.'),
    )
    email = models.EmailField(
        _('Buyer email'),
        blank=True,
        null=True,
        default=None,
        help_text=_('Optional.'),
    )


class PaymentBackURL(models.Model):
    """
    The URL locations to return on MercadoPago responses, based on the
    operation's success result.
    """
    success = models.URLField(
        _('Success payment URL'),
        blank=True,
        null=True,
        default=None,
        help_text=_('Optional.'),
    )
    failure = models.URLField(
        _('Failed payment URL'),
        blank=True,
        null=True,
        default=None,
        help_text=_('Optional.'),
    )
    pending = models.URLField(
        _('Pending payment URL'),
        blank=True,
        null=True,
        default=None,
        help_text=_('Optional.'),
    )


class PaymentPreferenceManager(models.Manager):
    """
    Overwrites the create method in order to use the MercadoPago API client.
    """
    use_for_related_fields = True

    def create(self, preference, *args, **kwargs):
        """
        Creates a :model:`djmercadopago.PaymentPreference` instance using the
        MercadoPago API client and stores the response infomation.
        """
        _uuid = uuid.uuid4()

        LOGGER.debug('[%s] Requesting creation of payment preferences: %r '
                     '...' % (_uuid, preference, ))

        response = _CLIENT.create_preference(preference)['response']
        LOGGER.debug('[%s] Done. Response: %r' % (_uuid, response))

        params = {}
        for field in PaymentPayer._meta.fields:
            LOGGER.debug('Payer field: %s' % field)
            if field not in response['payer']:
                continue
            params[field] = response['payer'][field]
        payer, _ = PaymentPayer.objects.get_or_create(**params)

        params = {}
        for field in PaymentBackURL._meta.fields:
            if field not in response['back_urls']:
                continue
            params[field] = response['back_urls'][field]
        back_urls, _ = PaymentBackURL.objects.get_or_create(**params)

        params = {}
        for field in PaymentPreference._meta.fields:
            if field in ['items', 'payer', 'back_urls'] or \
                    field not in response:
                continue
            params[field] = response[field]

        params.update({
            'payer': payer,
            'back_urls': back_urls,
        })
        pp = super(PaymentPreferenceManager, self).create(*args, **params)

        for item in response['items']:
            params = {}
            for field in PaymentItem._meta.fields:
                if field not in item:
                    continue
                if 'price' in field:
                    params[field] = Decimal(item[field])
                else:
                    params[field] = item[field]
            obj, _ = PaymentItem.objects.get_or_create(**params)
            pp.items.add(obj)

        # if 'payment_methods' in response:
        #     for method_id in response['payment_methods'].\
        #             get('excluded_payment_methods', []):
        #         payment_method, _ = PaymentMethod.objects.get(
        #             mercadopago_id=method_id
        #         )
        #         pp.payment_methods_excluded_payment_methods.add(payment_method)

        #     for type_id in response['payment_methods'].\
        #             get('excluded_payment_type', []):
        #         payment_type, _ = PaymentType.objects.get_or_create(
        #             mercadopago_id=type_id
        #         )
        #         pp.payment_methods_excluded_payment_types.add(payment_type)

        #     pp.payment_methods_installments = response['payment_methods'].\
        #         get('installments', None)

        #     pp.save()

        return pp


class PaymentPreference(models.Model):
    """
    Customizes the payment preferences to use.
    See: http://developers.mercadopago.com/documentacion/api/preferences
    """
    items = models.ManyToManyField(PaymentItem)

    payer = models.ForeignKey(PaymentPayer)

    back_urls = models.ForeignKey(PaymentBackURL)

    payment_methods_excluded_payment_methods = models.ManyToManyField(
        PaymentMethod,
        null=True,
        default=None,
    )
    payment_methods_excluded_payment_types = models.ManyToManyField(
        PaymentType,
        null=True,
        default=None,
    )
    payment_methods_installments = models.PositiveIntegerField(
        _('Maximum installments'),
        null=True,
        default=None,
        help_text=_('Optional. Maximum number of installments you will to '
                    'accept with credit card.'),
    )

    external_reference = models.CharField(
        _('External reference'),
        max_length=200,
        blank=True,
        null=True,
        help_text=_('Optional. Your system ID to link it to the payment.'),
    )
    collector_id = models.CharField(
        _('Collector ID'),
        max_length=200,
        help_text=_('Your identification ID as seller.'),
    )
    init_point = models.URLField(
        _('Init point'),
        help_text=_('Checkout access point.'),
    )
    sandbox_init_point = models.URLField(
        _('Sandbox init point'),
        help_text=_('Checkout access point on sandbox environment.'),
    )
    date_created = models.DateTimeField(
        _('Date created'),
    )

    objects = PaymentPreferenceManager()


# vim: ai ts=4 sts=4 et sw=4 ft=python
