from spack.package import *
from spack.pkg.psakievich.vimpackage import Vimpackage


class NvimCmp(Vimpackage):
    """A completion plugin for neovim coded in Lua."""

    git = "https://github.com/hrsh7th/nvim-cmp.git"
    homepage = git
    url      = git

    version('0.0.1', tag = 'v0.0.1')
    version('main', branch = 'main')
