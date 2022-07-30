from spack.package import *


class NvPlenary(Package):
    """Collection of functions used for many neovim plugins"""

    url      = 'https://github.com/nvim-lua/plenary.nvim'
    homepage = url
    git = url

    version('master', branch='master')


    def setup_dependent_run_environment(self, env, dependent_spec):
        env.append_flags('VIMRUNTIME', self.spec.prefix)

    def install(self, spec, prefix):
        # simply copy source to install
        install_tree(self.stage.source_path, prefix)
