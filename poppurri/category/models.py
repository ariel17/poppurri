#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf import settings
from django.db import models
from django.db.models import Count
from django.utils.translation import ugettext_lazy as _

from common.models import Searchable


class CategoryManager(models.Manager, Searchable):
    """
    TODO
    """
    use_for_related_field = True

    def get_query_set(self):
        """
        TODO
        """
        return super(CategoryManager, self).get_query_set().filter(
            is_final=True
        )

    def top_content(self, limit_to=settings.WEB_CATEGORIES_COUNT):
        """
        TODO
        """
        return self.annotate(num_mixtures=Count('mixtures')).\
            order_by('-num_mixtures').filter(num_mixtures__gt=0)[:limit_to]

    def search(self, q):
        """
        TODO
        """
        query = models.Q(name__icontains=q) | \
            models.Q(description__icontains=q)

        return self.get_query_set().filter(query)


class Category(models.Model):
    """
    TODO
    """
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        default=None,
        related_name='children',
    )
    name = models.CharField(_(u"Category name"), max_length=100, unique=True)
    description = models.CharField(
        _(u"Description"),
        max_length=255,
        blank=True,
        null=True
    )
    slug = models.SlugField(max_length=100)
    is_final = models.BooleanField(_(u"Is a final category"), default=False)

    objects = models.Manager()
    final = CategoryManager()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return unicode(self.name)

    def top_mixture(self):
        """
        TODO
        """
        mixtures = self.mixtures.all()
        if not len(mixtures):
            return None

        return mixtures.order_by('-rating_score')[0]

    @classmethod
    def tree(cls, child_category):
        """
        TODO
        """

        if not child_category:
            return None

        node = child_category
        tree = [node]

        while node.parent:
            tree.append(node.parent)
            node = node.parent

        tree.reverse()
        return tree


# vim: ai ts=4 sts=4 et sw=4 ft=python
