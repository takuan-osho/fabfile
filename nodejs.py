# -*- coding:utf-8 -*-

from fabric.api import task

from fabtools import require

installed_from_source = task(require.nodejs.installed_from_source)
