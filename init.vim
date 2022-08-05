source ~/.vimrc
set runtimepath+=~/.vim/pack/vendor/start/*
let mapleader=" "

lua require('pluginsettings')

" Telescope mappings
nnoremap <leader>ff <cmd>Telescope find_files<cr>
nnoremap <leader>fg <cmd>Telescope live_grep<cr>
nnoremap <leader>fb <cmd>Telescope buffers<cr>
nnoremap <leader>fh <cmd>Telescope help_tags<cr>




