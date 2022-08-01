from spack.package import *
import os

class Vimpackage(Package):
    """Meta class for vim packages"""

    @property
    def is_neovim(self):
        return 'nvim' in self.name

    @property
    def install_path(self):
        if self.is_neovim:
            return os.path.join(self.spec.prefix,
                                'share', 'nvim', self.name)
        else:
            return os.path.join(self.spec.prefix,
                                'share', 'vim', self.name)

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, self.install_path)

