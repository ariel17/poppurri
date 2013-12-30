#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf import settings
from django.db.models import Q
from django.views.generic.base import TemplateView

from mixture.models import Mixture


class SearchView(TemplateView):
    """
    TODO
    """
    template_name = u"search_result.html"

    def _mixture_result(self, q):
        """
        TODO
        """
        query = Q()

        for term in q.split():
            print "term: ", term
            query = query | Q(name__icontains=term) | \
                Q(short_description__icontains=term) | \
                Q(long_description__icontains=term)

        return Mixture.objects.filter(query)

    def get(self, *args, **kwargs):
        self._q = self.request.GET.get(settings.SEARCH_QUERY_PARAM, None)
        return super(SearchView, self).get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context[u"query"] = self._q
        context[u"mixture_result"] = self._mixture_result(self._q) if self._q \
            else {}
        return context


# vim: ai ts=4 sts=4 et sw=4 ft=python
