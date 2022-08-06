from spack.package import *
from spack.pkg.psakievich.vimpackage import Vimpackage


class NvimNerdtree(Vimpackage):
    """A tree explorer plugin for Vim"""

    git = "https://github.com/preservim/nerdtree.git"
    homepage = git
    url      = git
    version('master', branch = 'master')

