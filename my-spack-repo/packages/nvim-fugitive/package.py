from spack.package import *
from spack.pkg.psakievich.vimpackage import Vimpackage


class NvimFugitive(Vimpackage):
    """A git wrapper so good it should be illegal"""

    git = "https://github.com/tpope/vim-fugitive.git"
    homepage = git
    url      = git
    version('master', branch = 'master')

