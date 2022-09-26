from spack.package import *
from spack.pkg.psakievich.vimpackage import Vimpackage

class NvimVimVsnipInteg(Vimpackage):
    """vim-vsnip integrations to other plugins"""

    git = "https://github.com/hrsh7th/vim-vsnip-integ.git"
    homepage = git
    url = git

    version("master", branch = "master")
