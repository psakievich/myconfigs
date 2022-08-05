from spack.package import *
import spack.util.executable
import os


class Pjstack(BundlePackage):
    """Maseter package to install all my configurations"""

    homepage = "https://psakievich.github.io"
    url      = "pjstack"


    version('main')

    depends_on('nvim-telescope')
    depends_on('neovim')
    phases = ['install']

    def install(self, spec, prefix):

        mkdirp(os.path.expanduser('~/.config/nvim'))
        mkdirp(os.path.expanduser('~/.vim'))

        # link init and vimrc
        os.symlink(os.path.expanduser('~/soft/myconfigs/init.vim'),
                   os.path.expanduser('~/.config/nvim/init.vim'))
        os.symlink(os.path.expanduser('~/soft/myconfigs/vimrc.vim'),
                   os.path.expanduser( '~/.vimrc'))

        # build help tags
        nvim = spack.util.executable.which('nvim')

