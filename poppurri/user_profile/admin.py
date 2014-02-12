#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Administration console configuration for 'user_profile'
             application models.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib import admin

from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'has_picture', 'notify_by_email', 'has_biography',
                    'has_personal_page_url', 'is_complete', )
    list_filter = ('notify_by_email', )
    search_fields = ('user', 'is_complete')

    def has_picture(self, obj):
        """
        Returns ``True`` or ``False`` based on empty or filled picture image
        field.
        """
        return bool(obj.picture)

    def has_biography(self, obj):
        """
        Returns ``True`` or ``False`` based on empty or filled biography field.
        """
        return bool(obj.biography)

    def has_personal_page_url(self, obj):
        """
        Returns ``True`` or ``False`` based on empty or filled
        personal_page_url field.
        """
        return bool(obj.personal_page_url)

    def is_complete(self, obj):
        """
        Returns ``True`` or ``False`` based on filled or empty profile.
        """
        return self.has_picture(obj) and obj.notify_by_email and \
            self.has_biography(obj) and self.has_personal_page_url(obj)

    has_picture.boolean = True
    is_complete.boolean = True
    has_biography.boolean = True
    has_personal_page_url.boolean = True


admin.site.register(UserProfile, UserProfileAdmin)


# vim: ai ts=4 sts=4 et sw=4 ft=python
