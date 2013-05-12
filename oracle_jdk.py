# -*- coding:utf-8 -*-

from fabric.api import task

from fabtools import require

installed = task(require.oracle_jdk.installed)
