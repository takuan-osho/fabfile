# -*- coding:utf-8 -*-

from fabric.api import task

import fabtools
from fabtools import require

update_index = task(fabtools.deb.update_index)
upgrade = task(fabtools.deb.upgrade)

@task
def setup_devtools():
    """
    Install basic tools for developers.
    """
    packages = '''
        ssh curl wget vim git tmux build-essential libsqlite3-dev
        libreadline6-dev libgdbm-dev zlib1g-dev libbz2-dev sqlite3
        tk-dev zip tree jenkins
    '''.split()
    require.deb.packages(packages, update=True)
