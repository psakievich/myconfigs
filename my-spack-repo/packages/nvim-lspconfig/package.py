from spack.package import *
from spack.pkg.psakievich.vimpackage import Vimpackage

class NvimLspconfig(Vimpackage):
    """Neovim plugin lspconfig"""

    homepage = "https://github.com/neovim/nvim-lspconfig.git"
    url      = homepage
    git      = homepage

    version('master', branch='master')

