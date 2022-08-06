from spack.package import *
from spack.pkg.psakievich.vimpackage import Vimpackage


class NvimNeogit(Vimpackage):
    """A work-in-progress Magit clone for Neovim that is geared toward the Vim philosophy."""

    git = "https://github.com/TimUntersberger/neogit.git"
    homepage = git
    url      = git
    version('master', branch = 'master')
    depends_on('nvim-plenary')

