#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib import admin

from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'is_final')
    prepopulated_fields = {
        'slug_en': ('name_en', ),
        'slug_es': ('name_es', ),
    }


admin.site.register(Category, CategoryAdmin)


# vim: ai ts=4 sts=4 et sw=4 ft=python
