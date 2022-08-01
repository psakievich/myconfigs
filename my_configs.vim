set number
set relativenumber
:noremap <Home> 0
filetype plugin indent on
syntax on
set backspace=indent,eol,start
set noerrorbells
set hidden
set smartindent
set tabstop=2 softtabstop=2
set shiftwidth=2
set incsearch
set signcolumn=yes
set colorcolumn=80

:nnoremap <leader>ev :vsplit $MYVIMRC<cr>
:nnoremap <leader>sv :source $MYVIMRC<cr>
:inoremap nm <esc>
