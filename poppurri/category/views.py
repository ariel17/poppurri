#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.db.models import Q
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from .models import Category
from mixture.models import Mixture


class CategoryListView(ListView):
    """
    TODO
    """
    template_name = 'category_list.html'
    model = Category

    def get_queryset(self):
        return Category.final.all()

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['view'] = 'category'
        return context


class CategoryDetailView(TemplateView):
    """
    TODO
    """
    template_name = u"category_detail.html"
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)

        if 'slug' in self.kwargs:  # This is backward compatibility
            category = Category.final.get(
                Q(slug_en=self.kwargs['slug']) | Q(slug_es=self.kwargs['slug'])
            )
        else:
            # Normal category request
            category = Category.final.get(pk=self.kwargs['pk'])

        context['category'] = category
        context['mixture_list'] = Mixture.published.filter(category=category)
        return context


# vim: ai ts=4 sts=4 et sw=4 ft=python
