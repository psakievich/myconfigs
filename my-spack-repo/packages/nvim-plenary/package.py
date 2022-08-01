from spack.package import *
from VimPackage import VimPackage

class NvimPlenary(VimPackage):
    """Collection of functions used for many neovim plugins"""

    url      = 'https://github.com/nvim-lua/plenary.nvim'
    homepage = url
    git = url

    version('master', branch='master')
