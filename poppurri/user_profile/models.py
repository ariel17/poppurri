#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: User profile application containing model definition.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.models import ImageModel, Searchable


class UserProfileManager(models.Manager, Searchable):
    """
    A custom manager to add functionallity related to table level of
    :model:`user_profile.UserProfile`.
    """
    def get_query_set(self):
        return super(UserProfileManager, self).get_query_set().filter(
            user__is_active=True
        )


class UserProfile(ImageModel):
    """
    Stores only profile related information about the platform user.
    """
    user = models.OneToOneField(get_user_model(), related_name='profile')
    show_name = models.BooleanField(
        _(u'Show name on site'),
        help_text=u'Indicates if full username must be shown or not.',
        default=True,
    )
    picture = models.ImageField(
        _(u'User picture'),
        upload_to=ImageModel.normalize_filename(settings.AUTHOR_IMAGES_PATH),
        default=settings.USER_PROFILE_DEFAULT_IMAGE_URL,
        blank=True,
        null=True
    )
    notify_by_email = models.BooleanField(
        _('Mail notification enabled'),
        default=True
    )
    biography = models.TextField(_(u'User biography'), blank=True, null=True)
    personal_page_url = models.URLField(
        _(u'Pesonal page URL'),
        blank=True,
        null=True
    )

    objects = models.Manager()
    actives = UserProfileManager()

    def get_user_full_name(self):
        """
        Returns the full human name or the username, based on flag 'show_name'.
        """
        if self.show_name:
            full_name = (
                u"%s %s" % (self.user.first_name, self.user.last_name)
            ).strip()
            if full_name:
                return full_name

        return self.user.username


# vim: ai ts=4 sts=4 et sw=4 ft=python
