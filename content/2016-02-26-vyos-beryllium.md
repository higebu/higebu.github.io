title: VyOS Beryllium について
Slug: 2016-02-26-vyos-beryllium
Date: 2016-02-26 08:00
Category: Tech
Tags: vyos
Summary: 開発中の VyOS Berylliumのまとめです。

## Beryllium

* 詳しくは[Wiki](http://vyos.net/wiki/Beryllium)参照
* Debian jessie ベース
    * 必然的に Systemd 対応を強いられる
* Linux 4.4.0
* 新しいビルドスクリプト
    * [vyos-build](https://github.com/vyos/vyos-buld)
    * [build-iso](https://github.com/vyos/build-iso)から変更
    * trickv さんがAMIのビルドスクリプト作ってる [https://github.com/trickv/vyos-build/tree/vm](https://github.com/trickv/vyos-build/tree/vm)
* メタパッケージ、[vyos-world](https://github.com/vyos/vyos-world)
    * VyOS独自パッケージのまとめ
    * [パッケージリスト](https://github.com/vyos/vyos-world/blob/current/debian/control)

## 開発フローの変更

* current ブランチが最新
* beryllium リリース時に beryllium ブランチが切られる
* 新機能やバグフィックスは基本的に current にマージしていき、各リリースブランチにはバックポートで対応する
* 中心的なメンテナはcurrentの開発に集中しているため、現行のHeliumやLithiumのメンテナンスは人を募集している

## 個人的にやりたいこと

* Virtual boxやVMware用の公式イメージの提供
    * 個人的に作っているVagrant用のbox
        * [vyos-1.1.7-amd64](https://atlas.hashicorp.com/higebu/boxes/vyos-1.1.7-amd64)
        * [vyos-1.2.0-beta1-amd64](https://atlas.hashicorp.com/higebu/boxes/vyos-1.2.0-beta1-amd64)
* Docker対応
    * Dockerが動くようにしたい
    * Jessieになるので簡単そう
    * [前にやってたやつ](https://github.com/higebu/build-iso/tree/helium-docker)