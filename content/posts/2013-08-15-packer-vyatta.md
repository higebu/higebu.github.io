---
title: PackerでVyattaのVagrant用boxを作る
slug: packer-vyatta
date: 2013-08-15T00:00:00+09:00
categories: 
- "Tech"
tags: 
- "packer"
- " vagrant"
- " virtualbox"
- " vmware"
- " vyatta"
---

[Packer](http://www.packer.io/)は[Vagrant](http://www.vagrantup.com/)を作った@mitchellhさんが作ったOSイメージ作成ツールです。
インストールは[ダウンロードページ](http://www.packer.io/downloads.html)から自分のOSにあったバイナリを取ってきて入れるだけです。

今回はあまり見かけないVyattaのboxを作ってみました。
テンプレートはgithubに置いてあります。

[packer-templates](https://github.com/higebu/packer-templates)

今のところ6.4、6.5R1、6.6R1の64bitのものを置いてあります。
Packerのバージョンは0.2.3、VirtualBoxのバージョンは4.1.26で作っています。
他のバージョンだと動かないかもしれません。
VMware用も書いておいたのでVMware Fusionでも動くと思います。（試してません。）

テンプレートを使うときは以下のようにします。

```bash
packer build --only=virtualbox template.json # virtualboxのみ
packer build --only=vmware template.json # vmwareのみ
```

テンプレートの作り方ですが、基本的にはveeweeのDebian用のテンプレートをパクっています。
Vyattaのために少し工夫したのは以下の点です。

* Vyattaにはdebian-installerが入っていないので初期設定をコンソールでやっている
* シェルでVyattaのsetコマンドを使えるようにしている

```bash
WRAPPER=/opt/vyatta/sbin/vyatta-cfg-cmd-wrapper
. /etc/bash_completion
```

* もろもろを入れるためにDebian化している
* GuestAdditions入れるのにkernel-headerが必要なので、vyatta-devリポジトリからlinux-vyatta-kbuildをインストールしている

ノートPC上でVyatta立ち上げて自宅やクラウド上のネットワークとVPN接続するときに便利です。

Chef入りのVyattaなんて誰が使うんだという感じですが、Chef入りもあります。
一応、ビルド済のboxファイルもダウンロード可能な場所に置いてあるので欲しいという方はコメントください。
