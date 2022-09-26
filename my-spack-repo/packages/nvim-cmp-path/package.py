from spack.package import *
from spack.pkg.psakievich.vimpackage import Vimpackage

class NvimCmpPath(Vimpackage):
    """nvim-cmp source for path"""

    git = "https://github.com/hrsh7th/cmp-path.git"
    homepage = git
    url = git

    version("main", branch = "main")
