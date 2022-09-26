from spack.package import *
from spack.pkg.psakievich.vimpackage import Vimpackage


class NvimCmp(Vimpackage):
    """A completion plugin for neovim coded in Lua."""

    git = "https://github.com/hrsh7th/nvim-cmp.git"
    homepage = git
    url      = git

    version('0.0.1', tag = 'v0.0.1')
    version('main', branch = 'main')
    depends_on('nvim-cmp-nvim-lsp')
    depends_on('nvim-cmp-buffer')
    depends_on('nvim-cmp-path')
    depends_on('nvim-cmp-cmdline')

    # lots of snippet options but we will only use the authors for nw
    depends_on("nvim-vim-vsnip")
    depends_on("nvim-cmp-vsnip")
