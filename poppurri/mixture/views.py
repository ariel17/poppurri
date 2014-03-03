#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from contact_form.forms import ContactForm

from .models import Mixture
from category.models import Category
from currency.models import Currency


class FilterMixin(object):
    """
    TODO
    """
    def get_queryset(self):
        page = self.request.GET.get('page', 1)
        self.paginator = Paginator(Mixture.published.all(),
                                   settings.MIXTURE_LIST_MAX_ITEMS)
        try:
            return self.paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            return self.paginator.page(1)
        except EmptyPage:
            # If page is out of range, deliver last page.
            return self.paginator.page(self.paginator.num_pages)


class MixtureListView(FilterMixin, ListView):
    """
    TODO
    """
    template_name = u'mixture_list.html'
    model = Mixture

    def get_context_data(self, **kwargs):
        context = super(MixtureListView, self).get_context_data(**kwargs)
        context['view'] = 'mixture'
        context['page_numbers'] = [
            (i, i + 1) for i in range(self.paginator.num_pages)
        ]
        return context


class MixtureDetailView(TemplateView):
    """
    TODO
    """
    template_name = u'mixture_detail.html'
    model = Mixture

    def get_context_data(self, **kwargs):
        context = super(MixtureDetailView, self).get_context_data(**kwargs)

        mixture = Mixture.published.get(
            Q(slug_en=self.kwargs['slug']) | Q(slug_es=self.kwargs['slug'])
        )
        context['object'] = mixture

        currency_code = self.request.GET.get(
            'c', settings.CURRENCY_DEFAULT_CODE).upper()

        try:
            currency = Currency.objects.get(code=currency_code)
        except Currency.DoesNotExist:
            currency = Currency.objects.get(
                code=settings.CURRENCY_DEFAULT_CODE)

        context['currency'] = currency

        context['category_tree'] = Category.tree(mixture.category)
        context['form'] = ContactForm(request=self.request)
        return context

# vim: ai ts=4 sts=4 et sw=4 ft=python
