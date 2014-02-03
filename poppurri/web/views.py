#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.shortcuts import render_to_response
from django.template import RequestContext
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


def not_found(request):
    """
    Handles 404 pages.
    """
    return render_to_response('404.html', {},
                              context_instance=RequestContext(request))


def server_error(request):
    """
    Handles 500 pages.
    """
    return render_to_response('500.html', {},
                              context_instance=RequestContext(request))


# vim: ai ts=4 sts=4 et sw=4 ft=python
