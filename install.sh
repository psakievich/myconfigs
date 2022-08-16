#!/bin/bash
source ${HOME}/.bash_profile

mkdir -p ${HOME}/soft

# clone spack and activate it
git clone -c feature.manyFiles=true https://github.com/spack/spack.git ${HOME}/soft/spack
source ${HOME}/soft/spack/share/spack/setup-env.sh
spack repo add ${HOME}/soft/myconfigs/my-spack-repo
spack external find openssl curl

# create an environment for configs
spack env create myconfigs ${HOME}/soft/myconfigs/configs.yaml
spack -e myconfigs install

# TODO determine what python LSP server still
# python -m pip install --user pyright

# export bash stuff check to see if we've already appended file
if [ -z "${MYCONFIGINSTALLED}" ]; then
  echo 'source ${HOME}/.my_bash' >> ${HOME}/.bash_profile
fi
