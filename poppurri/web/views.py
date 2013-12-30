#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.views.generic.base import TemplateView

from mixture.models import Mixture, Category


class IndexView(TemplateView):
    """
    TODO
    """
    template_name = u"index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['top_mixtures'] = Mixture.objects.top_rates()
        context['top_categories'] = Category.objects.top_content()
        return context

# vim: ai ts=4 sts=4 et sw=4 ft=python
