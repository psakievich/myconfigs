from spack.package import *
from spack.pkg.psakievich.vimpackage import Vimpackage

class NvimCmpBuffer(Vimpackage):
    """nvim-cmp source for buffer words"""

    git = "https://github.com/hrsh7th/cmp-buffer.git"
    homepage = git
    url = git

    version("main", branch = "main")
