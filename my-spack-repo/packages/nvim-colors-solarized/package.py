from spack.package import *
from spack.pkg.psakievich.vimpackage import Vimpackage


class NvimColorsSolarized(Vimpackage):
    """Solarized color scheme for Vim"""

    git = "https://github.com/altercation/vim-colors-solarized.git"
    homepage = git
    url      = git
    version('master', branch = 'master')

