---
title: Vimでただのメモをいい感じにハイライトしたい
slug: how-to-use-hybrid-vim
date: 2012-09-05T00:00:00+09:00
aliases:
- /archives/450
categories: 
- "Tech"
tags: 
- "vim"
- "solarized"
- "hybridtext"
- "neobundle"
- "plugin"
---

!["Vim"](/images/vim-editor_logo.png)
最近、Vimのカラーテーマを[Solarized](http://ethanschoonover.com/solarized)にしたんですが、そしたらxxx.txtに書いてたメモがすごく読みづらくなった。

ほんとは画像とか見せたらわかりやすいと思うんだけど、とにかく全部一色で見づらい。

それで今回導入したのが[HybridText](http://www.vim.org/scripts/script.php?script_id=4188)というやつ。

これ今年の8月22日にアップされてて、タイミング良すぎてわろた。

入れ方はvim.orgのページ見ればわかると思うけど、一応書くと以下のような感じ。

1. ダウンロードしたhybrid.vimをsyntaxフォルダに入れる
2. テキストファイル開いて`:set filetype=hybrid`って打ってみる
3. 2で色が変わったらOKなので、以下の行をvimrcに追加する
   `au BufRead,BufNewFile *.txt set syntax=hybrid` 実際どういろが付くかもvim.orgのページにあるサンプルを見るとわかりやすいんだけど、

行頭に「#」つけたり、タブでインデントしたり、`"`で囲ったりすると色が変わってとても見やすい。

特に普段からタブでインデントしてメモ書いてるので、すごく見やすくなった。

<del>あ、プラグインとかは[neobundle](https://github.com/Shougo/neobundle.vim)で管理してるからこれもNeoBundleで入れたかったけど、まだgithubにはちゃんとしたものは上がってないようだった。</del>

2013/03/01 追記：
githubにあるやつはバージョンが1.0で、vim.orgにあるやつは1.2なので、vim.orgのやつをダウンロードした方が良いです。

[vim-scripts/hybrid.vim](https://github.com/vim-scripts/hybrid.vim "vim-scripts/hybrid.vim")

あと、HybridTextのページに載ってた、[TEXT2MINDMAP](http://www.text2mindmap.com/ "TEXT2MINDMAP")っていうのが面白そう。

普段マインドマップ書かないんだけどちょっと遊んでみたい。

今4時なので、結構適当な文章になってるけど、Vim使いの人はぜひ使ってみてください。
