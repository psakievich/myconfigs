from spack.package import *
import spack.util.executable
from spack.pkg.psakievich.vimpackage import config_link, neovim
import llnl.util.tty as tty
import os


class Psakievich(BundlePackage):
    """Maseter package to install all my configurations"""

    homepage = "https://psakievich.github.io"
    url      = "pjstack"


    version('main')

    depends_on('the-silver-searcher')
    depends_on('neovim')
    depends_on('git')
    depends_on('cmake')

    phases = ['install']

    def install(self, spec, prefix):

        mkdirp(os.path.expanduser('~/.config/nvim'))
        mkdirp(os.path.expanduser('~/.config/nvim/lua'))
        mkdirp(os.path.expanduser('~/.vim/backup'))

        # non-vim stuff
        config_link(os.path.expanduser('~/soft/myconfigs/tmux.conf'),
                    os.path.expanduser('~/.tmux.conf'))
        config_link(os.path.expanduser('~/soft/myconfigs/my_bash.sh'),
                    os.path.expanduser('~/.my_bash'))

        # link init and vimrc
        config_link(os.path.expanduser('~/soft/myconfigs/init.vim'),
                   os.path.expanduser('~/.config/nvim/init.vim'))
        config_link(os.path.expanduser('~/soft/myconfigs/vimrc.vim'),
                   os.path.expanduser( '~/.vimrc'))
        config_link(os.path.expanduser('~/soft/myconfigs/lua'),
                   os.path.expanduser( '~/.config/nvim/lua'))

        # install tree-sitter languages I want
        languages = ['cpp', 'python', 'lua', 'markdown', 'yaml', 'cmake',
                'latex', 'bibtex', 'make', 'bash']
        install_string = 'TSInstall {lan}'
        provider = neovim()
        provider("'autocmd User PackerComplete quitall' -c 'PackerSync'")
        tty.debug('Attempting to install langeuages')
        provider(['TSUninstall all'])
        for l in languages:
            tty.debug('Installing lang {lang}'.format(lang=l))
            provider([install_string.format(lan=l)])

