#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Changes decimal value representing a price into an scale dictated
by a currency.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from decimal import Decimal, ROUND_CEILING

from django.template import Library


register = Library()


@register.filter
def to_currency(value, currency):
    """
    Expects a decimal value that must be changed into a currency value.
    """
    return (value * currency.value).to_integral_exact(rounding=ROUND_CEILING)
