from spack.package import *
from spack.pkg.psakievich.vimpackage import Vimpackage


class NvimCoqNvim(Vimpackage):
    """Fast as F*** nvim completion. SQLite, concurrent scheduler, hundreds of hours of optimization."""

    git = "https://github.com/ms-jpq/coq_nvim.git"
    homepage = git
    url      = git

    version('main', branch='coq')
    depends_on('sqlite')
    depends_on('python@3.8.2:')
