---
title: VMware上のVyattaをクローンできるようにする
slug: how-to-use-vyatta-clone-helper
date: 2012-05-09T00:00:00+09:00
aliases:
- archives/418
categories: 
- "Tech"
tags: 
- "vmware"
- " vyatta"
- " clone"
---

最近の他のOS同様、Vyattaもクローンしたり、NIC付け替えるとeth0、eth1だったのがeth2、eth3になったりします。

configファイルはeth0、eth1のままなので、いちいち設定し直さないとネットワークにつながりません。

それは大変面倒なので、ググったらvyatta-clone-helperっていうすばらしいツールがあったので入れ方をメモ。

Vyatta4Peopleのリポジトリを追加

```
configure
set system package repository vyatta4people url http://packages.vyatta4people.org/debian
set system package repository vyatta4people distribution experimental
set system package repository vyatta4people components main
commit
save
```

vyatta-clone-helperをインストール

```
sudo aptitude update
sudo aptitude install vyatta-clone-helper
```

クローン後に起動してから、さらに再起動するとeth0、eth1・・・になっている。

すばらしいツールですね。

ソースは下記参照。

http://www.vyatta4people.org/vyatta-clone-helper-created/

作られたのは結構前だけど、6.4でもできました。
