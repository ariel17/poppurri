#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "poppurri.settings.local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

# vim: ai ts=4 sts=4 et sw=4 ft=python
