#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf.urls import patterns, url

from .views import CategoryListView, CategoryDetailView


urlpatterns = patterns('',
    url(r'^$', CategoryListView.as_view(), name='category_list'),
    url(r'^(?P<pk>\d+)/(?P<slug>[-\w]+)/$', CategoryDetailView.as_view(),
        name='category_detail'),
)

# vim: ai ts=4 sts=4 et sw=4 ft=python
