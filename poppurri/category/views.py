#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

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


class CategoryListView(ListView):
    """
    TODO
    """
    template_name = u"category_list.html"
    model = Category
    context_object_name = u"category_list"

    def get_queryset(self):
        return Category.objects.filter(is_final=True)


# vim: ai ts=4 sts=4 et sw=4 ft=python
