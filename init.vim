set runtimepath+=~/.vim/pack/vendor/start/*
source ~/.vimrc
let mapleader=" "

lua require('pluginsettings')

" Telescope mappings
nnoremap <leader>ff <cmd>Telescope find_files<cr>
nnoremap <leader>fg <cmd>Telescope live_grep<cr>
nnoremap <leader>fb <cmd>Telescope buffers<cr>
nnoremap <leader>fh <cmd>Telescope help_tags<cr>

:augroup autoformat
:  autocmd!
":  autocmd BufWritePre <buffer> lua vim.lsp.buf.formatting_sync()
:  autocmd BufWritePre * lua vim.lsp.buf.formatting_sync()
:  autocmd BufWritePre * :call CleanExtraSpaces()
:augroup END

