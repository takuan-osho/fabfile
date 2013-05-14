# -*- coding:utf-8 -*-

from fabric.api import task
from fabric.api import local

from fabtools.vagrant import vagrant
from fabtools.vagrant import vagrant_settings

from . import deb
from . import rpm
from . import myconfig
from . import python
from . import nodejs
from . import nginx
from . import oracle_jdk


@task
def setup_deb():
    local('vagrant up')

    with vagrant_settings():

        deb.update_index(quiet=False)
        deb.upgrade()
        deb.setup_devtools()

        myconfig.setup_dotfiles()

        python.setup_package_manager()
        python.install_useful_packages()

        nodejs.installed_from_source()

    local('vagrant sandbox on')


@task
def setup_rpm():
    local('vagrant up')
    with vagrant_settings():

        rpm.update()
        rpm.upgrade()
        rpm.setup_devtools()

        myconfig.setup_dotfiles()

        python.setup_package_manager()
        python.install_useful_packages()

        nodejs.installed_from_source()

    local('vagrant sandbox on')
