# -*- coding:utf-8 -*-

from fabric.api import local
from fabric.api import task
from fabric.api import cd

from fabtools.vagrant import vagrant

from cuisine import package_update
from cuisine import package_upgrade

from . import deb
from . import nginx
from . import python
from . import nodejs
from . import oracle_jdk

package_update = task(package_update)
package_upgrade = task(package_upgrade)


@task
def install_dotfiles():
    fabtools.git.clone('https://github.com/takuan-osho/dotfiles.git')


@task
def setup_dotfiles():
    run('mv $HOME/dotfiles/ $HOME/.dotfiles')
    with cd('.dotfiles'):
        run('bash bash_setup.sh')
    run('git clone https://github.com/Shougo/neobundle.vim.git ~/.dotfiles/.vim/bundle/neobundle.vim')
