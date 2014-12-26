Title: Pythonでtail --follow=name
Slug: python-tail-followname
URL: archives/464
save_as: archives/464/index.html
Author: higebu
Category: Tech
Tags: python, tail

Pythonでログをtailして1行ずつ処理したいと思ったんだけど、じゃあtailコマンドの結果を受け取ればいいんじゃねっていうプログラムです。

[gist:id=3727544]

-n +1で一行目から読み込みます。

読み込みつつ、ポジションファイルとか作って何行目まで読んだとか保存しておけば、後でリカバリできます。

まぁ、Pythonで全部書けばいいじゃんて思うかもしれませんが、こういうやり方もあるよっていうことで。
