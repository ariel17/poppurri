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

from ..models import Category
from mixture.models import Mixture


class CategorySetUpMixin(object):
    """
    TODO
    """
    def setUp(self):
        """
        TODO
        """
        super(CategorySetUpMixin, self).setUp()

        User = get_user_model()
        user = User(first_name='test', last_name='test')
        user.save()

        for cat_name in ('electronics', 'house', 'garden'):
            cat = Category.objects.create(
                name_en=cat_name,
                name_es=cat_name,
                slug_en=cat_name,
                slug_es=cat_name,
                is_final=True,
            )

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
                mixture.rating.add(
                    score=score,
                    user=user,
                    ip_address='127.0.0.1'
                )

        self.cat1 = Category.objects.create(
            name_en=str(1),
            name_es=str(1),
            slug_en=str(1),
            slug_es=str(1),
            is_final=False,
        )

        self.cat2 = Category.objects.create(
            name_en=str(2),
            name_es=str(2),
            slug_en=str(2),
            slug_es=str(2),
            is_final=False,
        )

        self.cat3 = Category.objects.create(
            name_en=str(3),
            name_es=str(3),
            slug_en=str(3),
            slug_es=str(3),
            is_final=True,
        )

        self.cat3.parent = self.cat2
        self.cat2.parent = self.cat1


class CategoryManagerTestcase(CategorySetUpMixin, TestCase):
    """
    TODO
    """
    def test_top_content_ok(self):
        """
        TODO
        """
        top_content = Category.final.top_content()
        self.assertTrue(len(top_content) <= settings.WEB_CATEGORIES_COUNT)


class CategoryTestCase(CategorySetUpMixin, TestCase):
    """
    TODO
    """
    def test_top_mixture_published(self):
        """
        TODO
        """
        cat = Category.final.all()[1]
        top_mixture = cat.top_mixture()

        self.assertIsNotNone(top_mixture)

        for mixture in cat.mixtures.all():
            self.assertTrue(top_mixture.rating.score >= mixture.rating.score)

    def test_top_mixture_unpublished(self):
        """
        Verifies that if a category has all unpublished mixtures, then it does
        not show any.
        """
        cat = Category.objects.all()[0]
        mixtures = Mixture.objects.filter(category=cat)

        for m in mixtures:
            m.is_published = False
            m.save()

        self.assertIsNone(cat.top_mixture())

    def test_tree(self):
        """
        TODO
        """
        tree = Category.tree(self.cat3)
        self.assertEquals(self.cat1, tree[0])
        self.assertEquals(self.cat2, tree[1])
        self.assertEquals(self.cat3, tree[2])

    def test_search(self):
        """
        Verifies that search method matches text fields on category model.
        """
        self.assertEquals(1, Category.final.search(q="house").count())
        self.assertEquals(
            3, Category.final.search(q="e").count()
        )
        self.assertEquals(0, Category.final.search(q=None).count())




# vim: ai ts=4 sts=4 et sw=4 ft=python
