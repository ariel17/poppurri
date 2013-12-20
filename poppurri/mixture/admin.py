#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib import admin

from .models import Mixture, MixtureImage


class MixtureAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'expose')
    search_fields = (
        'name',
        'description',
        'autor__first_name',
        'author__last_name',
        'author__email',
    )
    list_filter = ('expose',)


class MixtureImageAdmin(admin.ModelAdmin):
    list_display = ('mixture', 'image')
    search_fields = ('mixture',)


admin.site.register(Mixture, MixtureAdmin)
admin.site.register(MixtureImage, MixtureImageAdmin)

# vim: ai ts=4 sts=4 et sw=4 ft=python
