from spack.package import *
from spack.pkg.psakievich.vimpackage import Vimpackage

class NvimCmpCmdline(Vimpackage):
    """nvim-cmp source for vim's cmdline"""

    git = "https://github.com/hrsh7th/cmp-cmdline.git"
    homepage = git
    url = git

    version("main", branch = "main")
