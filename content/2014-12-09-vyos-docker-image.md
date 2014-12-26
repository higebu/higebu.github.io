Title: VyOS の Docker イメージを作ってみる
Slug: vyos-docker-image
Date: 2014-12-09 23:30
Category: Tech
Tags: vyos,docker
Summary: VyOS の Docker イメージの作り方です。

この記事は、 [VyOS Advent Calendar 2014][1] の9日目の記事です。

[TOC]

VyOS のコンテナがあったら面白そうということで作ってみました。

## 作り方

VyOS には `debootstrap` が入っていないため ISO から作っています。

基本的には、 [vyos/build-ami][2] と [Docker 公式ドキュメント][3]を参考にしています。

また、イメージの作成は手元の Ubuntu 14.04 で行いました。

流れは下記の通りですが、シェルスクリプトにしてしまったので、1つ1つは説明しません。

* `docker` をインストール
* `overlayroot` をインストール
* ISO をダウンロード
* ISO をマウント
* ISO の中身から root パーティションを構築
* イメージビルド用ディレクトリにコピー
* イメージビルド用ディレクトリを圧縮
* Dockerfile を作成
* `docker build`

また、スクリプト内でイメージ名に Docker Hub のユーザ名を含めているため `docker login` しておきます。

引数に ISO の URL を指定して実行します。

```
wget https://gist.githubusercontent.com/higebu/c152e73c20d438e33134/raw/cacc01517e2898e09bd98dd7303693af74b82aff/mkimage_vyos.sh
chmod +x mkimage_vyos.sh
./mkimage_vyos.sh http://mirror.vyos-users.jp/iso/release/1.1.1/vyos-1.1.1-amd64.iso
```

スクリプトは [gist][5] に置いてありますので、興味のある方はご参照ください。

できあがったものは [Docker Hub][4] に置いてあります。

## 使い方

使い方は模索中ですが、下記のようにすると一応起動します。

```
docker run -d --privileged -v /lib/modules:/lib/modules higebu/vyos:latest /sbin/init
```

カーネルモジュールが必要なサービスばかりのため、 `-v /lib/modules:/lib/modules` でホストのカーネルモジュールを読み込めるようにしています。

`--privileged` を付けないと `/lib/modules` 配下のファイルを読めず、カーネルモジュールが必要なサービスが起動しません。

その後、下記のようにすると vyos ユーザになれます。

```
docker exec -ti {name} /bin/vbash
su - vyos
```

`configure` などのコマンドも普通に動きます。

ただ、このままだと、 Ubuntu のカーネルモジュールで動いており、パッチを当てている、 VyOS のカーネルモジュールとは別物の可能性もあるので、 VyOS の上で Docker を動かせないかやってみたというのを明日書こうと思います。

 [1]: http://qiita.com/advent-calendar/2014/vyos
 [2]: https://github.com/vyos/build-ami
 [3]: https://docs.docker.com/articles/baseimages/
 [4]: https://registry.hub.docker.com/u/higebu/vyos/
 [5]: https://gist.github.com/higebu/c152e73c20d438e33134
