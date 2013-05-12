# -*- coding:utf-8 -*-

from fabric.api import task
from fabric.api import local

from fabtools.vagrant import vagrant
from fabtools.vagrant import vagrant_settings

from cuisine import package_update
from cuisine import package_upgrade

from . import deb
from . import nginx
from . import python
from . import nodejs
from . import oracle_jdk
from . import myconfig

package_update = task(package_update)
package_upgrade = task(package_upgrade)


@task
def setup_deb():
    local('vagrant up')
    with vagrant_settings():
        package_update()
        package_upgrade()

        deb.setup_devtools()

        python.setup_package_manager()
        python.install_useful_packages()
