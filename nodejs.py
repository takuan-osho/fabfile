# -*- coding:utf-8 -*-

from fabric.api import task

from fabtools import require

installed = task(require.nodejs.installed_from_source)
