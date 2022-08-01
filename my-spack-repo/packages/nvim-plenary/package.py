from spack.package import *
from spack.pkg.psakievich.vimpackage import Vimpackage

class NvimPlenary(Vimpackage):
    """Collection of functions used for many neovim plugins"""

    url      = 'https://github.com/nvim-lua/plenary.nvim'
    homepage = url
    git = url

    version('master', branch='master')
    depends_on('neovim')
