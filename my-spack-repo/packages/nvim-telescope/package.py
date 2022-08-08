from spack.package import *
from spack.pkg.psakievich.vimpackage import Vimpackage

class NvimTelescope(Vimpackage):
    """Neovim plugin telescope"""

    homepage = "https://github.com/nvim-telescope/telescope.nvim"
    url      = homepage
    git      = homepage

    version('0.1.0', tag='0.1.0')
    variant('ripgrep', default=True, description='use ripgrep for grepping')

    depends_on('nvim-plenary')
    depends_on('nvim-treesitter')
    depends_on('nvim-ripgrep', when='+ripgrep')
