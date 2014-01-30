#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Fabric file for remote deployment.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from datetime import datetime
from os import path

from fabric.api import env, settings, abort, local, run, prefix, task, cd
from fabric.contrib.console import confirm
from fabric.contrib.files import exists


DATETIME_FORMAT = '%Y%m%d%H%y'

REMOTE_ENV = path.join('~', 'envs')
REMOTE_ENV_CURRENT = path.join(REMOTE_ENV, 'current')

REMOTE_RELEASE = path.join('~', 'releases')
REMOTE_RELEASE_CURRENT = path.join(REMOTE_RELEASE, 'current')

REMOTE_REQUIREMENTS = path.join(REMOTE_RELEASE_CURRENT, 'requirements.txt')

REMOTE_SOURCE = path.join('~', 'source')

GIT_REPOSITORY_URL = 'git@github.com:ariel17/poppurri.git'
GIT_BRANCH_PRODUCTION = 'master'
GIT_BRANCH_DEVELOPMENT = 'develop'


def prepare_source(branch):
    """
    Performs repository operations to obtain a copy on remote server.
    """
    if exists(REMOTE_SOURCE):
        run('rm -rf %s' % REMOTE_SOURCE)

    run('mkdir %s' % REMOTE_SOURCE)
    with cd(REMOTE_SOURCE):
        run('git clone %s' % GIT_REPOSITORY_URL)
        with cd('poppurri'):
            run('git checkout -b %s origin/%s' % (branch, branch))


@task
def development():
    """
    Configures development environment.
    """
    env.use_ssh_config = True
    env.hosts = ['poppurri-web', ]
    prepare_source(GIT_BRANCH_DEVELOPMENT)


@task
def production():
    """
    Configures production environment.
    """
    env.use_ssh_config = True
    env.hosts = ['poppurri-web-production']
    env.user = 'poppurri'
    prepare_source(GIT_BRANCH_PRODUCTION)


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
