" Inspitation and some blatent copying from
" https://github.com/amix/vimrc/blob/master/vimrcs/basic.vim
"
"-- SETS
set autoread
set background=dark
set backspace=indent,eol,start
set colorcolumn=80
set foldcolumn=1
set hidden
set incsearch
set history=500
set hlsearch
set laststatus=2
set lazyredraw
set loadplugins
set magic
set mat=2
set noerrorbells
set noswapfile
set nowrap
set number
set relativenumber
set ruler
set scrolloff=6
set signcolumn=yes
set showmatch
set smartindent
set statusline=\ %{HasPaste()}%F%m%r%h\ %w\ \ CWD:\ %r%{getcwd()}%h\ \ \ Line:\ %l\ \ Column:\ %c
set tabstop=2 shiftwidth=2 expandtab
set updatetime=50
set wildmenu
" Ignore compiled files
set wildignore=*.o,*~,*.pyc
if has("win16") || has("win32")
    set wildignore+=.git\*,.hg\*,.svn\*
else
    set wildignore+=*/.git/*,*/.hg/*,*/.svn/*,*/.DS_Store
endif
let mapleader=" "
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Helper functions
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Returns true if paste mode is enabled
function! HasPaste()
    if &paste
        return 'PASTE MODE  '
    endif
    return ''
endfunction
syntax on
let g:solarized_termcolors=256
colorscheme gruvbox

filetype plugin on
filetype indent on

"remaps
:noremap <Home> 0
:nnoremap <leader>ev :vsplit $MYVIMRC<cr>
:nnoremap <leader>sv :source $MYVIMRC<cr>
:nnoremap <leader>w :w!<cr>
" Move a line of text
:nnoremap n :m +1<CR>
:nnoremap m :m -2<CR>
" window navigations
:noremap <C-h> <C-w>h
:noremap <C-j> <C-w>j
:noremap <C-k> <C-w>k
:noremap <C-l> <C-w>l
" turn off arrows for finger training
:nnoremap <Up> <nop>
:nnoremap <Down> <nop>
:nnoremap <Left> <nop>
:nnoremap <Right> <nop>

" Delete trailing white space on save, useful for some filetypes ;)
fun! CleanExtraSpaces()
    let save_cursor = getpos(".")
    let old_query = getreg('/')
    silent! %s/\s\+$//e
    call setpos('.', save_cursor)
    call setreg('/', old_query)
endfun
