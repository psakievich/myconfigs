from spack.package import *
from spack.pkg.psakievich.vimpackage import Vimpackage


class NvimDracula(Vimpackage):
    """A dark theme for vim"""

    git = "https://github.com/dracula/vim.git"
    homepage = git 
    url      = git 
    version('master', branch = 'master')

