" Things specific to my installation of nvim go here and in lua/*
source ~/.vimrc
set runtimepath+=~/.vim/pack/vendor/start/*
let g:solarized_termcolors=256
colorscheme gruvbox

lua require('pluginsettings')

" ack pluging use ag TODO move somewhere else
let g:ackprg = 'ag --vimgrep'

:augroup autoformat
:  autocmd!
":  autocmd BufWritePre <buffer> lua vim.lsp.buf.formatting_sync()
:  autocmd BufWritePre * lua vim.lsp.buf.formatting_sync()
:  autocmd BufWritePre * :call CleanExtraSpaces()
:augroup END

