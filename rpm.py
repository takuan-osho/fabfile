# -*- coding:utf-8 -*-

from fabric.api import task

import fabtools
from fabtools import require

update = task(fabtools.rpm.update)
upgrade = task(fabtools.rpm.upgrade)


@task
def setup_devtools():
    """
    Install basic tools for developpers.
    """
    packages = '''
        build_essentioal ssh curl wget vim git tmux zip tree mysql
    '''.split()
    require.rpm.packages(packages, yes='yes')
