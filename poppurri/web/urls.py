#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf.urls import patterns, include, url

from .views import HomeListView


urlpatterns = patterns('',
    url(r'^$', HomeListView.as_view(), name='article-list'),
)

# vim: ai ts=4 sts=4 et sw=4 ft=python
