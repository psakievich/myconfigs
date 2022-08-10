from spack.package import *
from spack.pkg.psakievich.vimpackage import Vimpackage


class NvimPeaksea(Vimpackage):
    """Peaksea colorscheme for Vi"""

    git = "https://github.com/calincru/peaksea.vim.git"
    homepage = git
    url      = git
    version('master', branch='master')

