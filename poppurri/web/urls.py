#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf.urls import patterns, url

from .views import IndexView


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
)

# vim: ai ts=4 sts=4 et sw=4 ft=python
