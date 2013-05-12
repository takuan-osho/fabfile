# -*- coding:utf-8 -*-

from fabric.api import task

from fabtools import require


@task
def installed():
    require.nodejs.installed_from_source()
