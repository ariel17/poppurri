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
from fabric.operations import open_shell, prompt


DATETIME_FORMAT = '%Y%m%d%H%y%S'

REMOTE_ENV = path.join('~', 'envs')
REMOTE_ENV_CURRENT = path.join(REMOTE_ENV, 'current')
REMOTE_ENV_CURRENT_ACTIVATE = path.join(REMOTE_ENV_CURRENT, 'bin', 'activate')
REMOTE_ENV_CURRENT_DEACTIVATE = path.join(REMOTE_ENV_CURRENT, 'bin',
                                          'deactivate')

REMOTE_RELEASE = path.join('~', 'releases')
REMOTE_RELEASE_CURRENT = path.join(REMOTE_RELEASE, 'current')

REMOTE_SOURCE = path.join('~', 'source')
REMOTE_SOURCE_CLONE = path.join(REMOTE_SOURCE, 'poppurri')

REMOTE_REQUIREMENTS_PRODUCTION = path.join(
    REMOTE_SOURCE_CLONE, 'requirements', 'production.txt')

REMOTE_REQUIREMENTS_DEVELOPMENT = path.join(
    REMOTE_SOURCE_CLONE, 'requirements', 'development.txt')

GIT_REPOSITORY_URL = 'git@github.com:ariel17/poppurri.git'
GIT_BRANCH_PRODUCTION = 'master'
GIT_BRANCH_DEVELOPMENT = 'develop'


def prepare_source(branch):
    """
    Performs repository operations to obtain a copy on remote server.
    """
    if not exists(REMOTE_SOURCE_CLONE):
        run('mkdir -p %s' % REMOTE_SOURCE)
        with cd(REMOTE_SOURCE):
            run('git clone %s' % GIT_REPOSITORY_URL)

    with cd(REMOTE_SOURCE_CLONE):
        with settings(warn_only=True):
            run('git checkout -b %s origin/%s' % (branch, branch))
            run('git pull --rebase')


def create_secret_key():
    """
    Creates a secret alphanumeric key to be used by Django as seed for hashing.
    """
    import random
    return ''.join([
        random.choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')
        for i in range(50)
    ])


@task
def development():
    """
    Configures development environment.
    """
    env.use_ssh_config = True
    env.hosts = ['poppurri-web', ]
    env.git_branch = GIT_BRANCH_DEVELOPMENT
    env.requirements = REMOTE_REQUIREMENTS_DEVELOPMENT
    env.settings = 'poppurri.settings.development'


@task
def production():
    """
    Configures production environment.
    """
    env.use_ssh_config = True
    env.hosts = ['poppurri-web-production']
    env.git_branch = GIT_BRANCH_PRODUCTION
    env.requirements = REMOTE_REQUIREMENTS_PRODUCTION
    env.settings = 'poppurri.settings.production'


@task
def set_env_vars():
    """
    Configures needed environment variables.
    """
    export_secret_key = 'declare -x SECRET_KEY="%s"' % create_secret_key()
    declarations = [export_secret_key]

    EMAIL_VARS = (
        ('', 'HOST'),
        ('', 'PORT'),
        ('HOST', 'USER'),
        ('HOST', 'PASSWORD'),
    )

    for (vprefix, var) in EMAIL_VARS:
        value = prompt('Enter email %s (blank to skip):' % var.lower())
        if value.strip():
            export = 'declare -x EMAIL_%s="%s"' % (
                '%s_%s' % (vprefix, var) if vprefix else var,
                value)
            declarations.append(export)

    for export in declarations:
        run(export)
        run("echo '%s' >> %s" % (export, REMOTE_ENV_CURRENT_ACTIVATE))


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
        run('pip install -r %s --download-cache=~/.pip/cache' %
            env.requirements)

    with settings(warn_only=True):
        run('rm %s' % REMOTE_ENV_CURRENT)
    run('ln -s %s %s' % (env_dir, REMOTE_ENV_CURRENT))

    set_env_vars()


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

    tmp_sources = path.join(tmp_dir, 'poppurri', '*')
    run('cp -r %s %s' % (tmp_sources, release_dir))

    if exists(REMOTE_RELEASE_CURRENT):
        run('rm %s' % REMOTE_RELEASE_CURRENT)

    run('ln -s %s %s' % (release_dir, REMOTE_RELEASE_CURRENT))

    release_env_dir = path.join(release_dir, 'env')
    run('ln -s %s %s' % (REMOTE_ENV_CURRENT, release_env_dir))


@task
def shell():
    """
    Opens the project's python interactive shell.
    """
    env_activate_path = path.join(REMOTE_RELEASE_CURRENT, 'env', 'bin',
                                  'activate')
    manage_path = path.join(REMOTE_RELEASE_CURRENT, 'manage.py')
    open_shell('source %s; %s shell --settings=%s; exit;' %
               (env_activate_path, manage_path, env.settings))
