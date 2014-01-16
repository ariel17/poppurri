#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: The mixture application. A mixture represents a hand anufactured
work to expose.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from transmeta import TransMeta
from djangoratings.fields import RatingField

from common.models import ImageModel, Searchable


class MixtureManager(models.Manager, Searchable):
    """
    A custom manager to add functionallity related to table level of
    :model:`mixture.Mixture`.
    """
    def get_query_set(self):
        return super(MixtureManager, self).get_query_set().filter(
            is_published=True
        )

    def top_rates(self, max_rate=settings.MIXTURE_MAX_RATE,
                  limit_to=settings.WEB_CAROUSEL_MIXTURE_COUNT):
        """
        TODO
        """
        return self.get_query_set().filter(
            rating_score__gte=max_rate,
        )[:limit_to]

    def search(self, q):
        """
        TODO
        """
        query = models.Q(name__icontains=q) | \
            models.Q(short_description__icontains=q) | \
            models.Q(long_description__icontains=q)

        return self.get_query_set().filter(query)


class Mixture(models.Model):
    """
    Represents a hand-made object or service.
    """
    __metaclass__ = TransMeta

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(
        _(u"Name"),
        max_length=100,
        help_text=_(u"A mixture short name that describes what it is."),
    )
    slug = models.SlugField(_("Slug name"), blank=True, null=True)
    short_description = models.CharField(
        _(u"Short description"),
        max_length=255,
        help_text=_(u"Short description about the product."),
    )
    long_description = models.TextField(
        _(u"Long description"),
        help_text=_(u"Long description about the product."),
    )
    is_published = models.BooleanField(
        _(u"Is Published"),
        default=True,
        help_text=_(u"Publish the mixture on site."),
    )
    rating = RatingField(
        range=settings.MIXTURE_MAX_RATE,
        can_change_vote=True,
        allow_delete=True,
    )
    category = models.ForeignKey(
        'category.Category',
        null=True,
        related_name='mixtures',
        help_text=_(u"The mixture clasification in category."),
    )

    objects = models.Manager()
    published = MixtureManager()

    class Meta:
        translate = ('name', 'short_description', 'long_description', 'slug')

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
    __metaclass__ = TransMeta

    mixture = models.ForeignKey(u"Mixture", related_name=u"recipes")
    item = models.CharField(_(u"Item name"), max_length=100)
    amount = models.CharField(
        _(u"Item amout"),
        max_length=50,
        blank=True,
        null=True
    )

    class Meta:
        translate = ('item', )

# vim: ai ts=4 sts=4 et sw=4 ft=python
