set number
set relativenumber
set loadplugins
set backspace=indent,eol,start
set noerrorbells
set hidden
set smartindent
set tabstop=2 softtabstop=2 shiftwidth=2
set incsearch
set signcolumn=yes
set colorcolumn=80
let mapleader=" "
filetype plugin indent on
syntax on

"remaps
:noremap <Home> 0
:nnoremap <leader>ev :vsplit $MYVIMRC<cr>
:nnoremap <leader>sv :source $MYVIMRC<cr>
:inoremap nm <esc>
