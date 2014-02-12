#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


import os
from uuid import uuid4

from django.db import models


class ImageModel(models.Model):
    """
    TODO
    """
    @property
    def image(self):
        """
        TODO
        """
        msg = u"%r must implement an ImageField named 'image'" % \
            (self.__class__, )
        raise NotImplementedError(msg)

    @staticmethod
    def normalize_filename(path):
        """
        TODO
        Source: http://stackoverflow.com/questions/15140942/django-imagefield-change-file-name-on-upload
        """
        def wrapper(instance, filename):
            """
            TODO
            """
            ext = filename.split('.')[-1]
            filename = '{}.{}'.format(
                instance.pk if instance.pk else uuid4().hex,
                ext)
            # return the whole path to the file
            return os.path.join(path, filename)

        return wrapper

    class Meta:
        abstract = True


class Searchable(object):
    """
    TODO
    """
    def search(self, q):
        """
        TODO
        """
        raise NotImplementedError("Must implement the 'search' method.")


# vim: ai ts=4 sts=4 et sw=4 ft=python
