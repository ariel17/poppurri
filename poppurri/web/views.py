#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.views.generic.list import ListView

from mixture.models import Mixture


class HomeListView(ListView):
    """
    TODO
    """
    model = Mixture
    template_name = u"web/index.html"

    # def get_queryset(self):
    #     """
    #     TODO
    #     """
    #     pass

# vim: ai ts=4 sts=4 et sw=4 ft=python
