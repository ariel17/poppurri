#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: A currency equivalence model.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.db import models
from django.utils.translation import ugettext_lazy as _

from transmeta import TransMeta


class Currency(models.Model):
    """
    A currency equivalence model. Store how much from a currency is equals to
    another.
    """
    __metaclass__ = TransMeta

    name = models.CharField(
        _(u'Currency name'),
        max_length=50,
        blank=True,
        null=True,
        default=None,
    )
    code = models.CharField(
        _(u'Representation code'),
        max_length=3,
        unique=True,
    )
    symbol = models.CharField(_(u'Representation symbol'), max_length=3)
    value = models.DecimalField(
        _(u'Currency scale'),
        max_digits=10,
        decimal_places=2,
        help_text=_(u'The currency value that equals to USD$ 1.'),
    )

    def __unicode__(self):
        return unicode(self.code)

    class Meta:
        verbose_name_plural = "Currencies"
        translate = ('name', )
