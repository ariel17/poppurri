#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Mixture


class MixtureDetailView(DetailView):
    """
    TODO
    """
    template_name = u"mixture/detail.html"
    model = Mixture

    # def get_context_data(self, **kwargs):
    #     context = super(MixtureView, self).get_context_data(**kwargs)
    #     return context

# vim: ai ts=4 sts=4 et sw=4 ft=python
