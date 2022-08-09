########################################################
#  Machine specific
########################################################
# fix annoying completion issue in rhel7
shopt -u progcomp

# file permissions
umask u=rwx,go=rx

export SOFT_DIR=${HOME}/soft
export PATH=${HOME}/myconfig/bin:${PATH}
export EDITOR=nvim
alias vim=nvim

function update-congifs(){
git -C ~/soft/myconfigs pull
}

function cdh(){
  cd ${HOME}
}

