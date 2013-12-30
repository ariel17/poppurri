#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.views.generic.detail import DetailView

from .models import Mixture, Category


class MixtureDetailView(DetailView):
    """
    TODO
    """
    template_name = u"mixture_detail.html"
    model = Mixture

    def get_context_data(self, **kwargs):
        context = super(MixtureDetailView, self).get_context_data(**kwargs)
        context["category_tree"] = Category.tree(context["object"].category)
        return context

# vim: ai ts=4 sts=4 et sw=4 ft=python
