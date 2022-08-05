from spack.package import *
import spack.util.executable
import os

class Vimpackage(Package):
    """Meta class for vim packages"""

    @property
    def is_neovim(self):
        return 'nvim' in self.name

    @property
    def plugin_location(self):
        return os.path.expanduser('~/.vim/pack/vendor/start')

    @property
    def install_path(self):
        if self.is_neovim:
            return os.path.join(self.spec.prefix,
                                'share', 'nvim', self.name)
        else:
            return os.path.join(self.spec.prefix,
                                'share', 'vim', self.name)
    @staticmethod
    def link(src, dest):
        if os.path.islink(dest):
            os.unlink(dest)
        os.symlink(src, dest)


    def install(self, spec, prefix):

        mkdirp(self.plugin_location)
        install_tree(self.stage.source_path, self.install_path)
        Vimpackage.link(self.install_path, os.path.join(self.plugin_location, self.name))
        if self.is_neovim:
            vim = spack.util.executable.which('nvim')
            vim('--headless', '+:helptags {pdir}'.format(pdir = self.install_path), '+q')
        else:
            vim = spack.util.executable.which('vim')
            vim('-c', ':helptags {pdir}'.format(pdir = self.install_path), '-c', 'q')


