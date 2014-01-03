#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from .models import Mixture, MixtureImage, Recipe
from category.models import Category


class MixtureImageAdmin(admin.ModelAdmin):
    list_display = ('mixture', 'link_image', 'outstanding')
    search_fields = ('mixture',)

    def link_image(self, obj):
        return u"<a href='{0}'>{0}</a>".format(obj.image.url)

    link_image.allow_tags = True
    link_image.short_description = _(u'Image')


class MixtureImageInline(admin.StackedInline):
    model = MixtureImage
    extra = 1


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


class RecipeInline(admin.StackedInline):
    model = Recipe
    extra = 1


class MixtureAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'author',
        'is_published',
        'rating_score',
        'link_category',
    )
    search_fields = (
        'name',
        'short_description',
        'long_description',
        'autor__first_name',
        'author__last_name',
        'author__email',
    )
    list_filter = ('is_published',)
    prepopulated_fields = {
        'slug': ('name', ),
    }
    inlines = [MixtureImageInline, RecipeInline, ]

    def link_category(self, obj):
        content_type = ContentType.objects.get_for_model(Category)
        url = reverse(u"admin:%s_%s_change" % (
            content_type.app_label, content_type.model),
            args=(obj.category.pk,))
        return u"<a href='{0}'>{1}</a>".format(url, obj.category.name)

    link_category.allow_tags = True
    link_category.short_description = _(u'Category')


admin.site.register(Mixture, MixtureAdmin)
admin.site.register(MixtureImage, MixtureImageAdmin)
admin.site.register(Recipe, RecipeAdmin)


# vim: ai ts=4 sts=4 et sw=4 ft=python
