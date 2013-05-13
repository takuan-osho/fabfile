# -*- coding:utf-8 -*-

from fabric.api import task

from fabtools import require


@task
def setup_devtools():
    """
    Install basic tools for developpers.
    """
    packages = '''
        build_essentioal ssh curl wget vim git tmux zip tree mysql 
    '''.split()
    require.rpm.packages(packages, yes='yes')
