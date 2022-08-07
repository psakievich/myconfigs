from spack.package import *
from spack.pkg.psakievich.vimpackage import Vimpackage

class NvimTreesitter(Vimpackage):
    """Neovim plugin telescope"""

    homepage = "https://github.com/nvim-treesitter/nvim-treesitter.git"
    url      = homepage
    git      = homepage

    version('master', branch='master')
    depends_on('neovim')

