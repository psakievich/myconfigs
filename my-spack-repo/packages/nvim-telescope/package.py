from spack.package import *
from VimPackage import VimPackage


class NvimTelescope(VimPackage):
    """Neovim plugin telescope"""

    homepage = "https://github.com/nvim-telescope/telescope.nvim"
    url      = homepage
    git      = homepage

    version('0.1.0', tag='0.1.0')

    depends_on('nvim-plenary')
