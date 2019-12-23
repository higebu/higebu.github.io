---
title: Vyatta用のVagrantプラグイン
slug: vagrant-vyatta
date: 2013-08-23T00:00:00+09:00
aliases:
- /archives/697
categories: 
- "Tech"
tags: 
- "vagrant"
- "vyatta"
- "packer"
- "virtualbox"
---

先日、[PackerでVyattaのVagrant用boxを作る][1]という記事を書きましたが、Vyattaはそのままでは`vagrant halt`が実行できないなど不便です。

そこで、VyattaをVagrantから制御するためのプラグインを作りました。

使い方は下記の通りです。

```bash
vagrant plugin install vagrant-vyatta
vagrant box add vyatta http://higebu.com/box/vyatta-livecd_VC6.5R1_amd64_virtualbox.box # chefなし
vagrant box add vyatta http://higebu.com/box/vyatta-livecd_VC6.5R1_amd64_chef_virtualbox.box # chef入り
vagrant init vyatta
vagrant up
vagrant halt
```

`vagrant halt`の他にホスト名の設定とネットワークの設定ができるようにしています。

ソースは[Github][2]に置いてあります。

 [1]: /blog/2013/08/15/packer-vyatta/
 [2]: https://github.com/higebu/vagrant-vyatta
