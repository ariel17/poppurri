#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__user__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.db.models import Q
from django.contrib.auth import get_user_model
from django.conf import settings
from django.views.generic import TemplateView
from django.views.generic.list import ListView


User = get_user_model()


class UserProfileListView(ListView):
    """
    TODO
    """
    template_name = u'user_profile_list.html'
    model = User

    def get_queryset(self):
        return User.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super(UserProfileListView, self).get_context_data(**kwargs)
        context['view'] = 'user'
        return context


class UserProfileDetailView(TemplateView):
    """
    TODO
    """
    template_name = u'user_profile_detail.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super(UserProfileDetailView, self).get_context_data(**kwargs)
        user = User.objects.get(Q(username=self.kwargs['username']))
        context['user_object'] = user
        context['view'] = 'user'
        return context


class UserProfileMixtureListView(ListView):
    """
    TODO
    """
    pass

# vim: ai ts=4 sts=4 et sw=4 ft=python
