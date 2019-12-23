---
title: VyOS の Vagrant 用 box を Vagrant Cloud にアップしました
date: 2014-03-13T01:22:00+09:00
slug: put-vyos-box-to-vagrant-cloud
tags: 
- "vyos"
- "vyatta"
- "vagrant"
- "vagrant cloud"
categories: 
- "tech"
---


[Vagrant Cloud](https://vagrantcloud.com) が出たので、とりあえず、VyOS の box をアップしてみました。

Vagrant 1.5 をインストール後、下記の手順で使えます。

```bash
vagrant plugin install vagrant-vyatta
vagrant init higebu/vyos-1.0.2
vagrant up
```

[vagrant-vyatta](https://github.com/higebu/vagrant-vyatta) も VyOS 対応済です。
