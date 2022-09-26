from spack.package import *
from spack.pkg.psakievich.vimpackage import Vimpackage

class NvimVimVsnip(Vimpackage):
    """Snippet plugin for vim/nvim that supports LSP/VSCode's snippet format."""

    git = "https://github.com/hrsh7th/vim-vsnip.git"
    homepage = git
    url = git

    version("master", branch = "master")
    variant('vsnip_integ', default = True, description = "Include a snip integration plugin")

    depends_on('nvim-vim-vsnip-integ', when = '+vsnip_integ')
