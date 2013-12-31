#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: The mixture application. A mixture represents a hand anufactured
work to expose.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf import settings
from django.db import models
from django.db.models import Count
from django.utils.translation import ugettext_lazy as _

from djangoratings.fields import RatingField

from common.models import ImageModel


class MixtureManager(models.Manager):
    """
    A custom manager to add functionallity related to table level of
    :model:`mixture.Mixture`.
    """
    def top_rates(self, max_rate=settings.MIXTURE_MAX_RATE,
                  limit_to=settings.WEB_CAROUSEL_MIXTURE_COUNT):
        return self.filter(rating_score__gte=max_rate)[:limit_to]


class Mixture(models.Model):
    """
    Represents a hand-made object or service.
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(
        _(u"Name"),
        max_length=100,
        help_text=_(u"A mixture short name that describes what it is.")
    )
    slug = models.SlugField(_("Slug name"), blank=True, null=True)
    short_description = models.CharField(
        _(u"Short description"),
        max_length=255,
        help_text=_(u"Short description about the product.")
    )
    long_description = models.TextField(
        _(u"Long description"),
        help_text=_(u"Long description about the product.")
    )
    expose = models.BooleanField(default=True)
    rating = RatingField(
        range=settings.MIXTURE_MAX_RATE,
        can_change_vote=True,
        allow_delete=True
    )
    category = models.ForeignKey(
        'Category',
        null=True,
        related_name='mixtures'
    )

    objects = MixtureManager()

    def __unicode__(self):
        return unicode(self.name)


class MixtureImageManager(models.Manager):
    """
    TODO
    """
    use_for_related_field = True

    def random_outstanding_image(self, *args, **kwargs):
        """
        TODO
        """
        outstandings = self.filter(outstanding=True).order_by('?')
        if len(outstandings):
            return outstandings[0]
        return None


class MixtureImage(ImageModel):
    """
    A mixture image that describes the object/service.
    """
    mixture = models.ForeignKey(u"Mixture", related_name=u"images")
    image = models.ImageField(
        _(u"Mixture image"),
        upload_to=ImageModel.normalize_filename(settings.MIXTURES_IMAGES_PATH),
        default=settings.IMAGES_DEFAULT,
    )
    alt = models.CharField(
        _(u"Alt text for the image."),
        max_length=50,
        blank=True,
        null=True,
    )
    outstanding = models.BooleanField(
        _(u"Is outstanding"),
        help_text=u"The image is outstanding between others.",
        default=False,
    )

    objects = MixtureImageManager()


class Recipe(models.Model):
    """
    TODO
    """
    mixture = models.ForeignKey(u"Mixture", related_name=u"recipes")
    item = models.CharField(_(u"Item name"), max_length=100)
    amount = models.CharField(
        _(u"Item amout"),
        max_length=50,
        blank=True,
        null=True
    )


class CategoryManager(models.Manager):
    """
    TODO
    """
    use_for_related_field = True

    def top_content(self, limit_to=settings.WEB_CATEGORIES_COUNT):
        """
        TODO
        """
        return self.annotate(num_mixtures=Count('mixtures')).\
            order_by('-num_mixtures').filter(num_mixtures__gt=0)[:limit_to]


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

    objects = CategoryManager()

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
