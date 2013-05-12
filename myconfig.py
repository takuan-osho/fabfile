# -*- coding:utf-8 -*-

from fabric.api import task
from fabric.api import run
from fabric.api import cd

import fabtools
from fabtools.require import git

import cuisine


@task
def install_dotfiles():
    git.working_copy('https://github.com/takuan-osho/dotfiles.git',
                     path='$HOME/dotfiles')


@task
def setup_dotfiles():
    if fabtools.files.is_dir('$HOME/dotfiles'):
        run('mv $HOME/dotfiles/ $HOME/.dotfiles')
    with cd('.dotfiles'):
        run('bash bash_setup.sh')
    git.working_copy('https://github.com/Shougo/neobundle.vim.git',
                     path='$HOME/.dotfiles/.vim/bundle/neobundle.vim')
