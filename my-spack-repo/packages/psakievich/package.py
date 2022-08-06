from spack.package import *
import spack.util.executable
from spack.pkg.psakievich.vimpackage import config_link, neovim
import os


class Psakievich(BundlePackage):
    """Maseter package to install all my configurations"""

    homepage = "https://psakievich.github.io"
    url      = "pjstack"


    version('main')

    depends_on('nvim-telescope')
    depends_on('neovim')
    depends_on('nvim-lspconfig')
    depends_on('nvim-dracula')
    depends_on('nvim-gruvbox')

    phases = ['install']

    def install(self, spec, prefix):

        mkdirp(os.path.expanduser('~/.config/nvim'))
        mkdirp(os.path.expanduser('~/.config/nvim/lua'))
        mkdirp(os.path.expanduser('~/.vim'))

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
        for l in languages:
            provider([install_string.format(lan=l)])
            
