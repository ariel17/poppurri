#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Fabric file for remote deployment.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from datetime import datetime
from os import path

from fabric.api import env, settings, abort, local, run, prefix, task, cd, sudo
from fabric.contrib.console import confirm
from fabric.contrib.files import exists
from fabric.operations import open_shell


APPLICATION = 'poppurri'

DATETIME_FORMAT = '%Y%m%d%H%y%S'

REMOTE_ENV = path.join('$HOME', 'envs')
REMOTE_ENV_CURRENT = path.join(REMOTE_ENV, 'current')
REMOTE_ENV_CURRENT_ACTIVATE = path.join(REMOTE_ENV_CURRENT, 'bin', 'activate')
REMOTE_ENV_CURRENT_DEACTIVATE = path.join(REMOTE_ENV_CURRENT, 'bin',
                                          'deactivate')

REMOTE_STORAGE = path.join('$HOME', 'storage')
REMOTE_STORAGE_MEDIA = path.join(REMOTE_STORAGE, 'media')
REMOTE_STORAGE_STATIC = path.join(REMOTE_STORAGE, 'assets')

REMOTE_RELEASE = path.join('$HOME', 'releases')
REMOTE_RELEASE_CURRENT = path.join(REMOTE_RELEASE, 'current')
REMOTE_RELEASE_CURRENT_MANAGE = path.join(REMOTE_RELEASE_CURRENT, 'manage.py')

REMOTE_SOURCE = path.join('$HOME', 'source')
REMOTE_SOURCE_TMP = path.join(REMOTE_SOURCE, 'tmp')
REMOTE_SOURCE_CLONE = path.join(REMOTE_SOURCE, APPLICATION)

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


def clean():
    """
    Removes deploy artifacts.
    """
    with settings(warn_only=True):
        run('rm -rf %s' % REMOTE_SOURCE_TMP)


@task
def development():
    """
    Configures development environment.
    """
    env.use_ssh_config = True
    env.forward_agent = True
    env.hosts = ['poppurri-web-development', ]
    env.git_branch = GIT_BRANCH_DEVELOPMENT
    env.requirements = REMOTE_REQUIREMENTS_DEVELOPMENT
    env.settings = '%s.settings.development' % APPLICATION
    env.application = '%s-dev' % APPLICATION


@task
def production():
    """
    Configures production environment.
    """
    env.use_ssh_config = True
    env.forward_agent = True
    env.hosts = ['poppurri-web-production']
    env.git_branch = GIT_BRANCH_PRODUCTION
    env.requirements = REMOTE_REQUIREMENTS_PRODUCTION
    env.settings = '%s.settings.production' % APPLICATION
    env.application = APPLICATION


@task
def set_env_vars():
    """
    Configures needed environment variables.
    """
    export_secret_key = 'declare -x SECRET_KEY="%s"' % create_secret_key()
    declarations = [export_secret_key]

    for export in declarations:
        run(export)
        run("echo '%s' >> %s" % (export, REMOTE_ENV_CURRENT_ACTIVATE))


@task
def test():
    """
    Executes tests on project.
    """
    with settings(warn_only=True):
        result = local('./%s/manage.py test' % env.application, capture=True)
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
        run('pip install -r %s --download-cache=$HOME/.pip/cache' %
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

    run('mkdir -p %s' % REMOTE_SOURCE_TMP)

    with cd(REMOTE_SOURCE_CLONE):
        run('git archive %s | tar -x -C %s' % (env.git_branch,
                                               REMOTE_SOURCE_TMP))
        with settings(warn_only=True):
            for d in ['media', 'assets']:
                tmp_dir = path.join(REMOTE_SOURCE_TMP, env.application, d)
                run('rm -rf %s' % tmp_dir)

    now = datetime.now().strftime(DATETIME_FORMAT)
    release_dir = path.join(REMOTE_RELEASE, now)
    run('mkdir -p %s' % release_dir)

    tmp_bin = path.join(REMOTE_SOURCE_TMP, 'bin')
    tmp_sources = path.join(REMOTE_SOURCE_CLONE, APPLICATION, '*')
    run('cp -r %s %s %s' % (tmp_sources, tmp_bin, release_dir))

    release_env_dir = path.join(release_dir, 'env')
    run('ln -s %s %s' % (REMOTE_ENV_CURRENT, release_env_dir))

    with settings(warn_only=True):
        release_media_dir = path.join(release_dir, 'media')
        run('mkdir -p %s' % REMOTE_STORAGE_MEDIA)

        release_static_dir = path.join(release_dir, 'assets')
        run('mkdir -p %s' % REMOTE_STORAGE_STATIC)

    run('ln -s %s %s' % (REMOTE_STORAGE_MEDIA, release_media_dir))
    run('ln -s %s %s' % (REMOTE_STORAGE_STATIC, release_static_dir))

    with prefix('source %s' % REMOTE_ENV_CURRENT_ACTIVATE):
        release_dir_manage = path.join(release_dir, 'manage.py')
        run('%s syncdb --settings=%s' %
            (release_dir_manage, env.settings))
        run('%s migrate --settings=%s' %
            (release_dir_manage, env.settings))
        run('%s collectstatic --settings=%s --noinput' %
            (release_dir_manage, env.settings))
        run('%s compilemessages --settings=%s' %
            (release_dir_manage, env.settings))

    if exists(REMOTE_RELEASE_CURRENT):
        run('rm %s' % REMOTE_RELEASE_CURRENT)

    run('ln -s %s %s' % (release_dir, REMOTE_RELEASE_CURRENT))
    clean()


@task
def shell():
    """
    Opens the project's python interactive shell.
    """
    open_shell('source %s; %s shell --settings=%s; exit;' %
               (REMOTE_ENV_CURRENT_ACTIVATE, REMOTE_RELEASE_CURRENT_MANAGE,
                env.settings))


@task
def restart():
    """
    Restart supervisord configuration.
    """
    sudo('supervisorctl restart %s' % env.application, shell=False)
