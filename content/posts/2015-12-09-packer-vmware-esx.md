---
title: PackerとESXiでPhotonのOVFを作る
slug: make-photon-ovf-by-packer-with-esxi
date: 2015-12-09T23:30:00Z
categories: 
- "Tech"
tags: 
- "packer"
- " esxi"
- " vmware"
- " photon"
- " vagrant"
---


これは、[HashiCorp Advent Calendar 2015](http://qiita.com/advent-calendar/2015/hashicorp)の9日目の記事です。

Packerって何というのは説明しませんので、[公式ページ](https://packer.io/)を読んでください。

Packer 0.8.7から[vmware-iso builder](https://packer.io/docs/builders/vmware-iso.html)でESXiを利用したときに、OVFを作ることができるようになるので、その紹介です。

この機能をマージしてもらえるまでに1年くらいかかってしまい、その間に[govmomi](https://github.com/vmware/govmomi)がリリースされているので、いつかgovmomiを使った実装に書き換えたいと思っています。

とても簡単に説明すると`vmware-iso`builderに`format`というオプションが追加されるので、template.jsonに`"format": "ovf"`と書くとOVFがエクスポートされるようになるというものです。

元々は、作ったVMがunregisterされ、データストアにVMXとVMDKだけ残るという仕様で、後からどうやって使うのかという状態でした。

この記事ではESXiのVagrant boxを作って、それを使ってOVFをビルドする手順になっていますが、ご自宅にESXiが入っているサーバがある方はそれでビルドしてみてください。

ただ、個人的にはESXiのVagrant boxを作っておくとノートPCの上などで手軽にESXiで遊べるのでおすすめです。

以下、環境とビルドの方法です。

## 環境

* Host OS: Ubuntu 14.04
* VMware Workstation 11.1.3
    * Fusionでもいいはずです。
* Packer 0.8.7.dev (77d9a89d1b3eef84a64edf7ca18b49c3ae5847c7)
    * まだ0.8.7がリリースされていないので、masterブランチからビルドしてください。
* ESXi 6.0 u1 3029758
    * [my vmware](https://my.vmware.com) から`VMware-VMvisor-Installer-6.0.0.update01-3029758.x86_64.iso`をダウンロードしてください。
* Vagrant 1.7.4
    * [公式ページ](https://www.vagrantup.com/)からダウンロードしてインストールしてください。
* vagrant-vmware-workstation 3.2.6
    * 有償なので[VMware provider](http://www.vagrantup.com/vmware)のページから購入してインストールしてください。。。
* vagrant-esxi 0.0.1
    * `vagrant plugin install vagrant-esxi`
    * ESXiのVagrant boxを使うために入れます。
* vagrant-triggers 0.5.2
    * `vagrant plugin install vagrant-triggers`
    * `vagrant up`で`packer build`まで走るようにするために入れます。
* ovftool 4.1.0
    * [VMwareのページ](https://www.vmware.com/support/developer/ovf/)からダウンロードしてインストールしてください。

## ESXiのVagrant boxの作成

[dougm/packer-esxi](https://github.com/dougm/packer-esxi)をフォークした、[higebu/packer-esxi](https://github.com/higebu/packer-esxi)を使って作ります。

VMwareの[@dougm](https://github.com/dougm)さんのリポジトリは古くていろいろと躓くので、フォークして修正したものを使います。

まず、リポジトリをcloneして`esxi60`ブランチをチェックアウトします。

```bash
git clone https://github.com/dougm/packer-esxi.git
git checkout esxi60
```

ビルドします。

```bash
packer build template.json
```

できあがったboxをインポートします。

```bash
vagrant box add --name esxi vmware_esxi60.box
```

これで、ESXiを`vagrant up`で起動できるようになります。

## VagrantでESXiを起動してPackerでOVFをビルド

では、上記で作成したESXiのboxを使ってOVFをビルドします。

[higebu/packer-esxi-example](https://github.com/higebu/packer-esxi-example)をcloneしてから、`vagrant up`します。

```bash
git clone https://github.com/higebu/packer-esxi-example.git
cd packer-esxi-example
vagrant up
```

いつもの`vagrant up`のログの後に`packer build`のログも流れるのが見えると思います。

エラーになってしまった場合、template.jsonの`<wait10>`の数が足りないところがあるかもしれません。

中身を見るとわかるのですが、これはVMware社がOSSとして公開している、[Photon](https://github.com/vmware/photon)のVMをビルドするテンプレートです。
Photonにはkickstartのような仕組みがないため、GUIのインストーラに対してコマンドを流しているからです。

## 最後に

ポイントは最初にも書きましたが、template.jsonに`format`というオプションを追加することです。

`ovf`、`ova`、`vmx`に対応しています。

Packerはとても便利なのですが、まじめに使っていると機能が足りなかったり動かなかったりすることも多いので、みんなでどんどんプルリクしていきましょう。
