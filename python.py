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
def install_useful_packages():
    pip_pkg_list = '''
        Sphinx mercurial virtualenv virtualenvwrapper pytest nose
        monitoring see ipython bpython
    '''.split()
    require.python.packages(pip_pkg_list, use_sudo=True)

    distribute_pkg_list = '''
    '''.split()
    distribute_pkg_list = [pkg for pkg in distribute_pkg_list
                           if not python.is_installed(pkg)]
    if distribute_pkg_list:
        python_distribute.install(distribute_pkg_list, use_sudo=True)
