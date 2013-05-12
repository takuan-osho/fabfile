# -*- coding:utf-8 -*-

from fabric.api import task

from fabtools import require


@task
def server():
    require.nginx.server()
