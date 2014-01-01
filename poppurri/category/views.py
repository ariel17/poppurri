#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.views.generic.detail import DetailView
from django.views.generic import TemplateView

from .models import Category


class CategoryDetailView(DetailView):
    """
    TODO
    """
    template_name = u"category_detail.html"
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        return context


class CategoryListView(TemplateView):
    """
    TODO
    """
    template_name = u"category_list.html"
    model = Category
    context_object_name = u"category_list"

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context[u"category_list"] = [
            Category.tree(c) for c in Category.objects.filter(is_final=True)
        ]
        return context


# vim: ai ts=4 sts=4 et sw=4 ft=python
