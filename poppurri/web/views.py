#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.views.generic.base import TemplateView

from mixture.models import Mixture
from category.models import Category


class HomeView(TemplateView):
    """
    TODO
    """
    template_name = u"home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['view'] = 'home'
        context['top_mixtures'] = Mixture.published.top_rates()
        context['top_categories'] = Category.final.top_content()
        return context


class NotFoundView(TemplateView):
    template_name = '404.html'


class ServerErrorView(TemplateView):
    template_name = '500.html'


# vim: ai ts=4 sts=4 et sw=4 ft=python
