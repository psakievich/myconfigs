from spack.package import *
import spack.util.executable
import os

def config_link(src, dest):
    if os.path.islink(dest):
        os.unlink(dest)
    os.symlink(src, dest)


class neovim:
    def __init__(self):
        self.nvim = spack.util.executable.which('nvim')

    def __call__(self, args):
        exe_args = ['--headless']
        exe_args.extend([v for x in list(args) for v in ['-c', x]])
        exe_args.extend(['-c', 'q'])
        self.nvim(*exe_args)


class vim:
    def __init(self):
        self.vim = spack.util.executable.which('vim')

    def __call__(self, args):
        
        exe_args = [v for x in list(args) for v in ['-c', x]]
        exe_args.extend(['-c', 'q'])
        self.vim(*exe_args)



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

    def install(self, spec, prefix):

        mkdirp(self.plugin_location)
        install_tree(self.stage.source_path, self.install_path)
        config_link(self.install_path, os.path.join(self.plugin_location, self.name))
        if self.is_neovim:
            vim = neovim()
        else:
            vim = vim()
        vim([':helptags ALL'])


