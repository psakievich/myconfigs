set number
set relativenumber
set loadplugins
set backspace=indent,eol,start
set noerrorbells
set wildmenu
" Ignore compiled files
set wildignore=*.o,*~,*.pyc
if has("win16") || has("win32")
    set wildignore+=.git\*,.hg\*,.svn\*
else
    set wildignore+=*/.git/*,*/.hg/*,*/.svn/*,*/.DS_Store
endif
set hidden
set smartindent
set noswapfile
set incsearch
set signcolumn=yes
set foldcolumn=1
set lazyredraw
set hlsearch
set magic
set colorcolumn=80
set scrolloff=6
set nowrap
let mapleader=" "
filetype plugin indent on
syntax on
set background=dark
let g:solarized_termcolors=256
colorscheme gruvbox

"remaps
:noremap <Home> 0
:nnoremap <leader>ev :vsplit $MYVIMRC<cr>
:nnoremap <leader>sv :source $MYVIMRC<cr>
