# -*- coding:utf-8 -*-

from fabric.api import task

from fabtools import python
from fabtools import python_distribute
from fabtools import require


@task
def setup_package_manager():
    require.python.distribute()
    require.python.pip()


@task
def useful_packages():
    pkg_list = '''
        Sphinx mercurial virtualenv virtualenvwrapper pytest nose
        monitoring see
    '''.split()
    pkg_list = [pkg for pkg in pkg_list if not python.is_installed(pkg)]
    if pkg_list:
        python_distribute.install(pkg_list, use_sudo=True)
