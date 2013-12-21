#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: The mixture application. A mixture represents a hand manufactured
work to expose.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from djangoratings.fields import RatingField

from common.models import ImageModel


class MixtureManager(models.Manager):
    """
    A custom manager to add functionallity related to table level of
    :model:`mixture.Mixture`.
    """

    def top_rates(self, max_rate=settings.MIXTURE_MAX_RATE):
        return self.filter(rating_score__gte=max_rate)


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
    description = models.TextField(
        _(u"Description"),
        help_text=_(u"The long description about the product.")
    )
    expose = models.BooleanField(default=True)
    rating = RatingField(
        range=settings.MIXTURE_MAX_RATE,
        can_change_vote=True,
        allow_delete=True
    )

    objects = MixtureManager()

    def __unicode__(self):
        return unicode(self.name)


class MixtureImage(ImageModel):
    """
    A mixture image that describes the object/service.
    """
    mixture = models.ForeignKey(u"Mixture")
    image = models.ImageField(
        _(u"Mixture image"),
        upload_to=ImageModel.normalize_filename(settings.MIXTURES_IMAGES_PATH),
        default=settings.IMAGES_DEFAULT,
    )

# vim: ai ts=4 sts=4 et sw=4 ft=python
