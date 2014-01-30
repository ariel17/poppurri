#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Fabric file for remote deployment.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from datetime import datetime
from os import environ, path

from fabric.api import env, settings, abort, local, run, prefix, task
from fabric.contrib.console import confirm


DATETIME_FORMAT = '%Y%m%d%H%y'

REMOTE_ENV = path.join('~', 'envs')
REMOTE_ENV_CURRENT = path.join(REMOTE_ENV, 'current')

REMOTE_RELEASE = path.join('~', 'releases')
REMOTE_RELEASE_CURRENT = path.join(REMOTE_RELEASE, 'current')

REMOTE_REQUIREMENTS = path.join(REMOTE_RELEASE_CURRENT, 'requirements.txt')

env.use_ssh_config = True


@task
def development():
    """
    Configures development environment.
    """
    env.hosts = ['poppurri-web-development', ]


@task
def production():
    """
    Configures production environment.
    """
    env.hosts = ['poppurri-web-production', ]


@task
def test():
    """
    Executes tests on project.
    """
    with settings(warn_only=True):
        result = local('./poppurri/manage.py test', capture=True)
    if result.failed and not confirm('Tests failed. Continue anyway?'):
        abort('Aborting at user request.')


@task
def create_env():
    """
    Creates a new environment and installs required dependencies.
    """
    run('mkdir -p %s' % REMOTE_ENV)

    now = datetime.now().strftime(DATETIME_FORMAT)
    env_dir = path.join(REMOTE_ENV, now)
    run('virtualenv %s' % env_dir)

    activate_path = path.join(env_dir, 'bin', 'activate')
    with prefix('source %s' % activate_path):
        run('pip install -r %s' % REMOTE_REQUIREMENTS)

    run('rm %s' % REMOTE_ENV_CURRENT)
    run('ln -s %s %s' % (env_dir, REMOTE_ENV_CURRENT))


@task
def deploy():
    """
    Puts the project on environment remote hosts.
    """
    pass
