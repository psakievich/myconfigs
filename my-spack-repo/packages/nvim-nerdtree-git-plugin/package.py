from spack.package import *
from spack.pkg.psakievich.vimpackage import Vimpackage


class NvimNerdtreeGitPlugin(Vimpackage):
    """A plugin of NERDTree showing git status"""

    git = "https://github.com/Xuyuanp/nerdtree-git-plugin.git"
    homepage = "https://www.example.com"
    url      = "nvim-nerdtree-git-plugin"

    depends_on('nvim-nerdtree')

    version('master', branch = 'master')

