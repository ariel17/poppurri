#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.core import urlresolvers
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from .models import Mixture, MixtureImage, Category, Recipe


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
    prepopulated_fields = {
        'slug': ('name', ),
    }


class MixtureImageAdmin(admin.ModelAdmin):
    list_display = ('mixture', 'link_image', 'outstanding')
    search_fields = ('mixture',)

    def link_image(self, obj):
        return u"<a href='{0}'>{0}</a>".format(obj.image.url)

    link_image.allow_tags = True
    link_image.short_description = _(u'Image')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'is_final')
    prepopulated_fields = {
        'slug': ('name', ),
    }


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('item', 'amount', 'link_mixture', )

    def link_mixture(self, obj):
        content_type = ContentType.objects.get_for_model(Mixture)
        url = reverse(u"admin:%s_%s_change" % (
            content_type.app_label, content_type.model),
            args=(obj.mixture.pk,))
        return u"<a href='{0}'>{1}</a>".format(url, obj.mixture.name)

    link_mixture.allow_tags = True
    link_mixture.short_description = _(u'Mixture')


admin.site.register(Mixture, MixtureAdmin)
admin.site.register(MixtureImage, MixtureImageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)


# vim: ai ts=4 sts=4 et sw=4 ft=python
