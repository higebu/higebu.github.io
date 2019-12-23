---
title: Pythonでtail --follow=name
slug: python-tail-followname
date: 2012-09-15T00:00:00+09:00
aliases:
- archives/464
categories: 
- "Tech"
tags: 
- "python"
- "tail"
---

Pythonでログをtailして1行ずつ処理したいと思ったんだけど、じゃあtailコマンドの結果を受け取ればいいんじゃねっていうプログラムです。

{{< gist higebu 3727544 >}}

-n +1で一行目から読み込みます。

読み込みつつ、ポジションファイルとか作って何行目まで読んだとか保存しておけば、後でリカバリできます。

まぁ、Pythonで全部書けばいいじゃんて思うかもしれませんが、こういうやり方もあるよっていうことで。
