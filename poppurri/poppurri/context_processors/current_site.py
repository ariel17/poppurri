#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: A context processor that adds the current site instance to request
information.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib.sites.models import Site


def current_site(request):
    """
    A context processor to add the "current site" to the current Context
    """
    try:
        current_site = Site.objects.get_current()
        return {
            'current_site': current_site,
        }
    except Site.DoesNotExist:
        return {
            'current_site': ''
        }
