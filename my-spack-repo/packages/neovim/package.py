from spack.package import *
from spack.pkg.builtin.neovim import Neovim as builtin_neovim


class Neovim(builtin_neovim):
    depends_on('nv-telescope')
    def test_functions(self):
        pass
