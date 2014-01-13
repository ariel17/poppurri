#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf import settings
from django.views.generic.base import TemplateView

from mixture.models import Mixture
from category.models import Category


class SearchView(TemplateView):
    """
    TODO
    """
    template_name = u"search_result.html"

    def get(self, *args, **kwargs):
        self._q = self.request.GET.get(settings.SEARCH_QUERY_PARAM, None)
        return super(SearchView, self).get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context[u"q"] = self._q
        context[u"mixture_result"] = Mixture.published.search(q=self._q)
        context[u"category_result"] = Category.final.search(q=self._q)
        return context


# vim: ai ts=4 sts=4 et sw=4 ft=python
