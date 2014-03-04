#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf.urls import patterns, url

from .views import MixtureDetailView, MixtureListView


urlpatterns = patterns('',
    url(r'^$', MixtureListView.as_view(), name='mixture_list'),
    url(r'^(?P<pk>\d+)/(?P<slug>[-\w]+)/$', MixtureDetailView.as_view(),
        name='mixture_detail'),
)

# vim: ai ts=4 sts=4 et sw=4 ft=python
