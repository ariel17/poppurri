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
from fabric.operations import open_shell


DATETIME_FORMAT = '%Y%m%d%H%y'

REMOTE_ENV = path.join('~', 'envs')
REMOTE_ENV_CURRENT = path.join(REMOTE_ENV, 'current')
REMOTE_ENV_CURRENT_ACTIVATE = path.join(REMOTE_ENV_CURRENT, 'bin', 'activate')
REMOTE_ENV_CURRENT_DEACTIVATE = path.join(REMOTE_ENV_CURRENT, 'bin',
                                          'deactivate')

REMOTE_RELEASE = path.join('~', 'releases')
REMOTE_RELEASE_CURRENT = path.join(REMOTE_RELEASE, 'current')

REMOTE_REQUIREMENTS = path.join(REMOTE_RELEASE_CURRENT, 'requirements.txt')

REMOTE_SOURCE = path.join('~', 'source')
REMOTE_SOURCE_CLONE = path.join(REMOTE_SOURCE, 'poppurri')

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
        with cd(REMOTE_SOURCE_CLONE):
            with settings(warn_only=True):
                run('git checkout -b %s origin/%s' % (branch, branch))


@task
def development():
    """
    Configures development environment.
    """
    env.use_ssh_config = True
    env.hosts = ['poppurri-web', ]
    env.git_branch = GIT_BRANCH_DEVELOPMENT


@task
def production():
    """
    Configures production environment.
    """
    env.use_ssh_config = True
    env.hosts = ['poppurri-web-production']
    env.git_branch = GIT_BRANCH_PRODUCTION


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
    prepare_source(env.git_branch)

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
    prepare_source(env.git_branch)

    tmp_dir = path.join(REMOTE_SOURCE, 'tmp')
    run('mkdir -p %s' % tmp_dir)

    with cd(REMOTE_SOURCE_CLONE):
        run('git archive %s | tar -x -C %s' % (env.git_branch, tmp_dir))

    now = datetime.now().strftime(DATETIME_FORMAT)
    release_dir = path.join(REMOTE_RELEASE, now)
    run('mkdir -p %s' % release_dir)

    tmp_source_dir = path.join(tmp_dir, 'poppurri')
    run('cp -r %s %s' % (tmp_source_dir, release_dir))

    if exists(REMOTE_RELEASE_CURRENT):
        run('rm %s' % REMOTE_RELEASE_CURRENT)

    run('ln -s %s %s' % (release_dir, REMOTE_RELEASE_CURRENT))


@task
def shell():
    """
    Opens the project's python interactive shell.
    """
    with cd(REMOTE_RELEASE_CURRENT):
        with prefix('source %s' % REMOTE_ENV_CURRENT_ACTIVATE):
            open_shell('./manage.py shell')
