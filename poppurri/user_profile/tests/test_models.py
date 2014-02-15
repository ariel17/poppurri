#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Test unit cases for 'user_profile' application.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase

from user_profile.models import UserProfile


User = get_user_model()


class UserProfileTestCase(TestCase):
    """
    Tests functionallity defined on :model:`user_profile.UserProfile`.
    """
    def setUp(self):
        super(UserProfileTestCase, self).setUp()
        self.u = User.objects.create(
            username='testusername',
            password='password',
            first_name='Test User',
            last_name='LastName',
        )
        self.up = UserProfile.objects.create(user=self.u, show_name=True)

    def test_get_user_full_name_ok(self):
        """
        Verifies that fetched user full name is the user's first and last name
        composition, when user allows to show it.
        """
        full_name = u"%s %s" % (self.u.first_name, self.u.last_name, )
        self.assertEquals(full_name, self.up.get_user_full_name())

    def test_get_user_full_name_not_allow_showing_name(self):
        """
        Verifies that fetched user full name is the user's username value, when
        user does not allow to show it.
        """
        self.up.show_name = False
        self.assertEquals(self.u.username, self.up.get_user_full_name())

    def test_get_user_full_name_allow_showing_name(self):
        """
        Verifies that fetched user full name is the user's username value, when
        user does not allow to show it.
        """
        full_name = u"%s %s" % (self.u.first_name, self.u.last_name, )
        self.assertEquals(full_name, self.up.get_user_full_name())

    def test_get_user_full_incomplete_profile(self):
        """
        Verifies that fetched user full name is the user's username value, when
        user allows to show it but profile is incomplete.
        """
        self.u.first_name = self.u.last_name = u''
        self.assertEquals(self.u.username, self.up.get_user_full_name())


# vim: ai ts=4 sts=4 et sw=4 ft=python
