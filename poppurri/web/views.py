#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf import settings
from django.views.generic.base import TemplateView

from mixture.models import Mixture


class IndexView(TemplateView):
    """
    TODO
    """
    template_name = u"web/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['top_rates'] = Mixture.objects.\
            top_rates()[:settings.WEB_CAROUSEL_MIXTURE_COUNT]

        return context

# vim: ai ts=4 sts=4 et sw=4 ft=python
