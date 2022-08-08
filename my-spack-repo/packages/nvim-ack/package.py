from spack.package import *
from spack.pkg.psakievich.vimpackage import Vimpackage


class NvimAck(Vimpackage):
    """Vim plugin for the Perl module / CLI script 'ack'"""

    git = "https://github.com/mileszs/ack.vim.git"
    homepage = git
    url      = git
    version('master', branch='master')
    depends_on('the-silver-searcher')

