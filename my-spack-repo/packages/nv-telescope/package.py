from spack.package import *


class NvTelescope(Package):
    """Neovim plugin telescope"""

    homepage = "https://github.com/nvim-telescope/telescope.nvim"
    url      = homepage
    git      = homepage

    version('0.1.0', tag='0.1.0')

    depends_on('nv-plenary')

    def setup_dependent_run_environment(self, env, dependent_spec):
        env.append_flags('VIMRUNTIME', self.spec.prefix)

    def install(self, spec, prefix):
        # simply copy source to install
        install_tree(self.stage.source_path, prefix)

