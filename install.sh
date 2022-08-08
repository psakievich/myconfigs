#!/bin/bash

mkdir -p ${HOME}/soft

# clone spack and activate it
git clone -c feature.manyFiles=true https://github.com/spack/spack.git ${HOME}/soft/spack
source ${HOME}/soft/spack/share/spack/setup-env.sh
spack repo add ${HOME}/soft/myconfigs/my-spack-repo

# create an environment for configs
spack env create myconfigs ${HOME}/soft/myconfigs/configs.yaml
spack -e myconfigs install

# TODO determine what python LSP server still
# python -m pip install --user pyright

# export bash stuff
echo 'source ${HOME}/.my_bash' >> ${HOME}/.bash_profile
