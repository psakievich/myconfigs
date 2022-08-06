from spack.package import *
from spack.pkg.psakievich.vimpackage import Vimpackage


class NvimCommentary(Vimpackage):
    """Comment stuff out"""

    git = "https://github.com/tpope/vim-commentary.git"
    homepage = git
    url      = git
    version('master', branch = 'master')
