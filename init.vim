set runtimepath+=~/.vim/pack/vendor/start/*
source ~/.vimrc
let mapleader=" "

lua require('pluginsettings')

" Telescope mappings
nnoremap <leader>ff <cmd>Telescope find_files<cr>
nnoremap <leader>fg <cmd>Telescope live_grep<cr>
nnoremap <leader>fb <cmd>Telescope buffers<cr>
nnoremap <leader>fh <cmd>Telescope help_tags<cr>

" window navigations
noremap <C-h> <C-w>h
noremap <C-j> <C-w>j
noremap <C-k> <C-w>k
noremap <C-l> <C-w>l

" Delete trailing white space on save, useful for some filetypes ;)
fun! CleanExtraSpaces()
    let save_cursor = getpos(".")
    let old_query = getreg('/')
    silent! %s/\s\+$//e
    call setpos('.', save_cursor)
    call setreg('/', old_query)
endfun

:augroup autoformat
:  autocmd!
":  autocmd BufWritePre <buffer> lua vim.lsp.buf.formatting_sync()
:  autocmd BufWritePre * lua vim.lsp.buf.formatting_sync()
:  autocmd BufWritePre * :call CleanExtraSpaces()
:augroup END


