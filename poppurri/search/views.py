#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.views.generic.base import TemplateView


class SearchView(TemplateView):
    """
    TODO
    """
    template_name = u"search/result.html"

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        return context

# vim: ai ts=4 sts=4 et sw=4 ft=python
