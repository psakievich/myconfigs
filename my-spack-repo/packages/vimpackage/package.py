from spack.package import *
import spack.util.executable
import llnl.util.tty as tty
import os

def config_link(src, dest):
    tty.debug('Linking {src} to {dest}'.format(src=src, dest=dest))
    if os.path.islink(dest):
        os.unlink(dest)
    elif os.path.isdir(dest):
        os.rmdir(dest)
    elif os.path.isfile(dest):
        os.remove(dest)
    os.symlink(src, dest)


class neovim:
    def __init__(self):
        self.executor = spack.util.executable.which('nvim')

    def __call__(self, args):
        exe_args = ['--headless']
        exe_args.extend([v for x in list(args) for v in ['-c', x]])
        exe_args.extend(['-c', 'q'])
        tty.debug('Calling nvim with args', *exe_args)
        self.executor(*exe_args)


class my_vim:
    def __init(self):
        self.executor = spack.util.executable.which('vim')

    def __call__(self, args):
        exe_args = [v for x in list(args) for v in ['-c', x]]
        exe_args.extend(['-c', 'q'])
        print(*exe_args)
        return
        self.executor(*exe_args)



class Vimpackage(Package):
    """Meta class for vim packages"""
    depends_on('neovim')

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
            provider = neovim()
        else:
            provider = my_vim()
        provider([':helptags ALL'])


