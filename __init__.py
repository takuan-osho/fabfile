# -*- coding:utf-8 -*-

from fabric.api import task

from fabtools.vagrant import vagrant

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
