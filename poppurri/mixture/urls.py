#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf.urls import patterns, url

from .views import MixtureDetailView


urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/', MixtureDetailView.as_view(), name='mixture_id'),
    url(r'^(?P<slug>\s+)/', MixtureDetailView.as_view(), name='mixture_slug'),
)

# vim: ai ts=4 sts=4 et sw=4 ft=python
