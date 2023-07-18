########################################################
#  Machine specific
########################################################
# fix annoying completion issue in rhel7
shopt -u progcomp
set -o vi

# file permissions
umask u=rwx,go=rx

export SOFT_DIR=${HOME}/soft
export PATH=${HOME}/myconfig/bin:${PATH}
export EDITOR=nvim
export MYCONFIGINSTALLED=1

alias sspack=${SOFT_DIR}/spack/bin/spack

function update-congifs(){
git -C ~/soft/myconfigs pull
}

function git_branch_prune(){
    git branch | grep -v "$1" | xargs git branch -D
}

function cdh(){
  cd ${HOME}
}

function cds(){
  if [ -n "${SCRATCH}" ]; then
    cd ${SCRATCH}
  else
    echo "SCRATCH var is not set"
  fi
}

