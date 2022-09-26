from spack.package import *
from spack.pkg.psakievich.vimpackage import Vimpackage

class NvimCmpVsnip(Vimpackage):
    """nvim-cmp source for vim-vsnip"""

    git = "https://github.com/hrsh7th/cmp-vsnip.git"
    homepage = git
    url = git

    version("main", branch = "main")
