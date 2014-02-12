#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Test cases defined for model/manager classes for application
             mixture.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase

from mixture.models import Mixture
from category.models import Category


class MixtureManagerTestCase(TestCase):
    """
    Tests functionallity defined on :model:`mixture.MixtureManager`.
    """
    def setUp(self):
        """
        Sets up the environment.
        """
        super(MixtureManagerTestCase, self).setUp()

        User = get_user_model()
        user = User(first_name='test', last_name='test')
        user.save()

        cat = Category.objects.create(
            name_es='electronics',
            name_en='electronics',
            slug_en='electronics',
            slug_es='electronics',
        )

        settings.MIXTURE_MAX_RATE = 5

        for i, score in enumerate((1, 5, 5)):
            mixture = Mixture.objects.create(
                author=user,
                name_en='name-%s' % i,
                name_es='name-%s' % i,
                short_description_en='short description %s' % i,
                short_description_es='short description %s' % i,
                long_description_en='long description %s' % i,
                long_description_es='long description %s' % i,
                category=cat,
                is_published=True,
            )
            mixture.rating.add(score=score, user=user, ip_address='127.0.0.1')

    def test_top_rates(self):
        """
        Verifies that the number of top rated mixtures matches the instances
        created.
        """
        self.assertEquals(2, Mixture.published.top_rates().count())

    def test_search(self):
        """
        Verifies that search method matches correctly.
        """
        self.assertEquals(1, Mixture.published.search(q="name-1").count())
        self.assertEquals(
            3, Mixture.published.search(q="short description").count()
        )
        self.assertEquals(0, Mixture.published.search(q=None).count())


# vim: ai ts=4 sts=4 et sw=4 ft=python
