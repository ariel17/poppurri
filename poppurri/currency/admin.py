#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Administration console configuration for Currency model.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib import admin

from .models import Currency


class CurrencyAdmin(admin.ModelAdmin):
    """
    Administration class configuring console disposition for model
    :model:`currency.Currency`.
    """
    list_display = ('code', 'name', 'symbol', 'value', )
    search_fields = ('name', 'code', )


admin.site.register(Currency, CurrencyAdmin)
