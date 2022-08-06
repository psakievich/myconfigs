#!/bin/bash


mkdir -p ${HOME}/soft
git clone -c feature.manyFiles=true https://github.com/spack/spack.git
source ${HOME}/soft/spack/share/spack/setup-env.sh
spack repo add ${HOME}/soft/myconfigs/my-spack/repo
spack env create myconfigs configs.yaml
spack -e myconfigs install
echo 'export source ${HOME}/.my_bash >> ${HOME}/.bash_profile'
