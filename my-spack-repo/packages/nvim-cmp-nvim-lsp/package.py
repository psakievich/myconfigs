from spack.package import *
from spack.pkg.psakievich.vimpackage import Vimpackage

class NvimCmpNvimLsp(Vimpackage):
    """nvim-cmp source for neovim builtin LSP client"""

    git = "https://github.com/hrsh7th/cmp-nvim-lsp.git"
    homepage = git
    url = git

    version("main", branch = "main")
