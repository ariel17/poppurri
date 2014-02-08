#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: URL mapping configuration for application 'user_profile'.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf.urls import patterns, url

from .views import UserProfileListView, UserProfileDetailView


urlpatterns = patterns('',
    url(r'^$', UserProfileListView.as_view(), name='user_profile_list'),
    url(r'^(?P<username>[-\w]+)/$', UserProfileDetailView.as_view(),
        name='user_profile_detail'),
)

# vim: ai ts=4 sts=4 et sw=4 ft=python
