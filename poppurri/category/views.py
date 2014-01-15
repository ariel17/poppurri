#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.db.models import Q
from django.views.generic import TemplateView

from .models import Category
from mixture.models import Mixture


class CategoryListView(TemplateView):
    """
    TODO
    """
    template_name = 'category_list.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['view'] = 'category'
        context['category_list'] = [
            Category.tree(c) for c in Category.objects.filter(is_final=True)
        ]
        return context


class CategoryDetailView(TemplateView):
    """
    TODO
    """
    template_name = u"category_detail.html"
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)

        category = Category.final.get(
            Q(slug_en=self.kwargs['slug']) | Q(slug_es=self.kwargs['slug'])
        )
        context['category'] = category
        context['mixture_list'] = Mixture.published.filter(category=category)
        return context


# vim: ai ts=4 sts=4 et sw=4 ft=python
