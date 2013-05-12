# -*- coding:utf-8 -*-

from fabric.api import task

from fabtools import require


@task
def setup_devtools():
    """
    Install basic tools for developpers.
    """
    packages = '''
        ssh curl wget vim git tmux build-essential libsqlite3-dev libreadline6-dev libgdbm-dev
        zlib1g-dev libbz2-dev sqlite3 tk-dev zip tree
    '''.split()
    require.deb.packages(packages, update=True)
