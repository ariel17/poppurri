#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.db.models import Q
from django.views.generic import TemplateView

from .models import Mixture
from category.models import Category


class MixtureDetailView(TemplateView):
    """
    TODO
    """
    template_name = u"mixture_detail.html"
    model = Mixture

    def get_context_data(self, **kwargs):
        context = super(MixtureDetailView, self).get_context_data(**kwargs)

        mixture = Mixture.published.get(
            Q(slug_en=self.kwargs['slug']) | Q(slug_es=self.kwargs['slug'])
        )
        context["category_tree"] = Category.tree(mixture.category)
        context['object'] = mixture
        return context

# vim: ai ts=4 sts=4 et sw=4 ft=python
