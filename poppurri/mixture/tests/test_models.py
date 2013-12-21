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

from mixture.models import Mixture, Category


class MixtureManagerTestCase(TestCase):
    """
    Tests functionallity defined pn :model:`mixture.MixtureManager`.
    """
    def setUp(self):
        """
        Sets up the environment.
        """
        super(MixtureManagerTestCase, self).setUp()

        User = get_user_model()
        user = User(first_name='test', last_name='test')
        user.save()

        cat = Category.objects.create(name='electronics', slug='electronics')

        for score in (1, 5, 5):
            mixture = Mixture.objects.create(
                author=user,
                name='name',
                description='description',
                category=cat,
            )
            mixture.rating.add(score=score, user=user, ip_address='127.0.0.1')

    def test_top_rates(self):
        """
        Verifies that the number of top rated mixtures matches the instances
        created.
        """
        self.assertEquals(2, Mixture.objects.top_rates().count())


class CategoryManager(TestCase):
    """
    """
    def setUp(self):
        """
        TODO
        """
        super(CategoryManager, self).setUp()

        User = get_user_model()
        user = User(first_name='test', last_name='test')
        user.save()

        self.cat = Category.objects.create(name='electronics', slug='electronics')

        for score in (1, 5, 5):
            mixture = Mixture.objects.create(
                author=user,
                name='name',
                description='description',
                category=self.cat,
            )
            mixture.rating.add(score=score, user=user, ip_address='127.0.0.1')

    def test_top_content(self):
        """
        TODO
        """
        top_content = Category.objects.top_content()
        self.assertTrue(len(top_content) <= settings.WEB_CATEGORIES_COUNT)

# vim: ai ts=4 sts=4 et sw=4 ft=python
