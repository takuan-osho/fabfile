# -*- coding:utf-8 -*-

from fabric.api import task

from fabtools import require

server = task(require.nginx.server)
