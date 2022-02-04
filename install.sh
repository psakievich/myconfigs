#!/bin/bash

# symlink files
ln -s ${HOME}/.tmux.conf tmux.conf
ln -s ${HOME}/.my_bash my_bash

# install vim stuff
git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime
sh ~/.vim_runtime/install_awesome_vimrc.sh
cp my_configs.vim ~/.vim_runtime/my_configs.vim

# append files

# determine architecture
unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     machine=Linux;;
    Darwin*)    machine=Mac;;
    CYGWIN*)    machine=Cygwin;;
    MINGW*)     machine=MinGw;;
    *)          machine="UNKNOWN:${unameOut}"
esac

echo 'export source ${HOME}/.my_bash >> ${HOME}/.bash_profile'
