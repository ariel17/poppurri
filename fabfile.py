#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Fabric file for remote deployment.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from os import environ, path

from fabric.api import env, settings, abort, local
from fabric.contrib.console import confirm


PROJECT_ROOT = path.dirname(path.realpath(__file__))
APP_DIRECTORY = path.join(PROJECT_ROOT, 'poppurri')

COMMANDS = {
    'test': path.join(APP_DIRECTORY, 'manage.py test'),
}


def _get_env_setting(setting):
    """
    Get the environment setting or raise exception.
    """
    try:
        return environ[setting]
    except KeyError:
        raise EnvironmentError("Set the %s env variable" % setting)


def development():
    """
    Configures development environment.
    """
    env.hosts = _get_env_setting('POPPURRI_DEVELOPMENT_HOSTS')


def production():
    """
    Configures production environment.
    """
    env.hosts = _get_env_setting('POPPURRI_PRODUCTION_HOSTS')


def test():
    """
    Executes tests on project.
    """
    with settings(warn_only=True):
        result = local(COMMANDS['test'], capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")


def create_env():
    """
    Creates a new environment and installs required dependencies.
    """
    pass


def deploy():
    """
    Puts the project on environment remote hosts.
    """
    pass
