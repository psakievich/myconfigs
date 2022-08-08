from spack.package import *
from spack.pkg.psakievich.vimpackage import Vimpackage


class NvimTrouble(Vimpackage):
    """
    A pretty diagnostics, references, telescope results, quickfix and
    location list to help you solve all the trouble your code is causing
    """

    git = "https://github.com/folke/trouble.nvim.git"
    homepage = git
    url      = git
    version('main', branch = 'main')

