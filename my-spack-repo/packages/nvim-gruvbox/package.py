from spack.package import *
from spack.pkg.psakievich.vimpackage import Vimpackage


class NvimGruvbox(Vimpackage):
    """Colorscheme gruvbox"""

    git = "https://github.com/morhetz/gruvbox.git"
    homepage = git
    url      = git
    version('master', branch='master')

