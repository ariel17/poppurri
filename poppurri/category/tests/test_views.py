#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Test cases for Category views.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.core.urlresolvers import reverse
from django.test import TestCase, Client


class CategoryDetailViewTestCase(TestCase):

    def setUp(self):
        super(CategoryDetailViewTestCase, self).setUp()
        self._c = Client()

    def tearDown(self):
        super(CategoryDetailViewTestCase, self).tearDown()

    def test_404(self):
        response = self._c.get(
            reverse('category_detail', args=(999, 'ignored-slug'))
        )
        self.assertEquals(200, response.status_code)  # custom 404

    def test_404_slug(self):
        response = self._c.get(
            reverse('category_detail_slug', args=('bad-slug',))
        )
        self.assertEquals(200, response.status_code)  # custom 404

    def test_404_id(self):
        response = self._c.get(
            reverse('category_detail_id', args=(999,))
        )
        self.assertEquals(200, response.status_code)  # custom 404
