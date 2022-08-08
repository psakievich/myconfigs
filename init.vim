set runtimepath+=~/.vim/pack/vendor/start/*
source ~/.vimrc
let mapleader=" "

lua require('pluginsettings')


:augroup autoformat
:  autocmd!
":  autocmd BufWritePre <buffer> lua vim.lsp.buf.formatting_sync()
:  autocmd BufWritePre * lua vim.lsp.buf.formatting_sync()
:  autocmd BufWritePre * :call CleanExtraSpaces()
:augroup END

