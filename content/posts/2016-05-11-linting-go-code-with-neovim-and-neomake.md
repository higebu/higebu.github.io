---
title: "NeovimとNeomakeでGoの文法チェックをする"
slug: 2016-05-11-linting-go-code-with-neovim-and-neomake
date: 2016-05-11T08:07:00Z
categories: 
- "Tech"
tags: 
- "vim"
- "neovim"
- "neomake"
- "golang"
---


[Neomake](https://github.com/neomake/neomake)は[Neovim](https://github.com/neovim/neovim)のjob-controlに対応した[Syntastic](https://github.com/scrooloose/syntastic)の代わりとして使えるプラグインです。

パッケージマネージャは[dein.vim](https://github.com/Shougo/dein.vim)を使っています。

plugins.tomlに下記を追記します。

```toml
[[plugins]]
repo = 'neomake/neomake'
hook_add = '''
  autocmd! BufWritePost * Neomake
'''
```

plugins_lazy.tomlに下記を追記します。デフォルトでは`go`、`golint`、`govet`でのチェックになっていますが、[errcheck](https://github.com/kisielk/errcheck)を追加しています。

```
[[plugins]]
repo = 'fatih/vim-go'
on_ft = 'go'
hook_source = '''
  let g:go_fmt_command = 'goimports'
  let s:goargs = go#package#ImportPath(expand('%:p:h'))
  let g:neomake_go_errcheck_maker = {
    \ 'args': ['-abspath', s:goargs],
    \ 'append_file': 0,
    \ 'errorformat': '%f:%l:%c:\ %m, %f:%l:%c\ %#%m',
    \ }
  let g:neomake_go_enabled_makers = ['golint', 'govet', 'errcheck']
'''
```

下記のようにerrcheckの結果が表示されます。

![neomake](/images/20160511-neomake.png)