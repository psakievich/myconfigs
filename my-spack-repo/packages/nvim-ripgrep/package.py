from spack.package import *
from spack.pkg.psakievich.vimpackage import Vimpackage


class NvimRipgrep(Vimpackage):
    """
    ripgrep recursively searches directories for a regex
    pattern while respecting your gitignore
    """

    git = "https://github.com/BurntSushi/ripgrep.git"
    homepage = git
    url      = git
    version('master', branch='master')

