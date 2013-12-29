#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Mixture, MixtureImage, Category


class MixtureAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'expose', 'rating_score', )
    search_fields = (
        'name',
        'short_description',
        'long_description',
        'autor__first_name',
        'author__last_name',
        'author__email',
    )
    list_filter = ('expose',)


class MixtureImageAdmin(admin.ModelAdmin):
    list_display = ('mixture', 'link_image', 'outstanding')
    search_fields = ('mixture',)

    def link_image(self, obj):
        return u"<a href='{0}'>{0}</a>".format(obj.image.url)

    link_image.allow_tags = True
    link_image.short_description = _(u'Image')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Mixture, MixtureAdmin)
admin.site.register(MixtureImage, MixtureImageAdmin)
admin.site.register(Category, CategoryAdmin)

# vim: ai ts=4 sts=4 et sw=4 ft=python
