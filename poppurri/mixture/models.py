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

from common.models import ImageModel


class Mixture(models.Model):
    """
    TODO
    """
    author = models.ForeignKey(u"auth.User")
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
    valoration = models.PositiveIntegerField(_("Valoration"), default=0)
    # requeriments
    # steps
    # designs


class MixtureImage(ImageModel):
    """
    TODO
    """
    mixture = models.ForeignKey(u"Mixture")
    image = models.ImageField(
        _(u"Mixture image"),
        upload_to=ImageModel.normalize_filename(settings.MIXTURES_IMAGES_PATH),
        default=settings.IMAGES_DEFAULT,
    )

# vim: ai ts=4 sts=4 et sw=4 ft=python
