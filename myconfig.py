# -*- coding:utf-8 -*-

from fabric.api import task
from fabric.api import run
from fabric.api import cd

from fabtools import files
from fabtools.require import git

import cuisine


def install_dotfiles():
    git.working_copy('https://github.com/takuan-osho/dotfiles.git',
                     path='$HOME/dotfiles')


@task
def setup_dotfiles():
    if files.is_dir('$HOME/dotfiles') and not files.is_dir('$HOME/.dotfiles'):
        install_dotfiles()
        run('mv $HOME/dotfiles/ $HOME/.dotfiles')
        with cd('$HOME/.dotfiles'):
            run('bash bash_setup.sh')
        with cd('$HOME/.dotfiles/.vim/bundle'):
            run('rm -rf neobundle.vim')
            git.working_copy('https://github.com/Shougo/neobundle.vim.git')
