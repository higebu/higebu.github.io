---
title: VyOS の概要
slug: vyos-overview
date: 2014-12-01T23:00:00Z
categories: 
- "Tech"
tags: 
- "vyos"
- " vyatta"
---


この記事は、 [VyOS Advent Calendar 2014][1] の1日目の記事です。



# VyOS とは

VyOS って何？という方も多いと思いますので、まずは、 VyOS の概要を説明したいと思います。

VyOS は、開発が停止してしまった、 Vyatta Core 6.6 R1 をフォークしたものです。

Vyatta 自体は、 Brocade 社に買収された後も開発が続けられておりますが、 OSS ではなくなっています。

開発は、元 Vyatta 社の [Daniil Baturin][2] が中心になって行っています。

VyOS の元になっている、 Vyatta Core 6.6 というバージョンでは、 Vyatta の商用版のルーティングソフトウェアが Quagga から ZebOS に変わっており、その影響で、無償版の Vyatta Core では IPv4 の BGP ピアグループが動かないというバグがありました。

このバグは、 VyOS 1.0.0 で修正されており、 [AS5612 のルータが Vyatta Core 6.5 から VyOS 1.0.0 にアップグレード][3]しています。

最新版は、 1.1.0 でもうすぐ 1.1.1 がリリースされそうです。

# VyOS の特徴

### Junos ライクなコマンド

Junos ライクなコマンドと設定ファイルで各機能の設定を行うことができます。

configure でコンフィグレーションモードに入るところや、設定の流れが、 commit で有効化、 save で保存になっており、 rollback も可能なところが、 Junos ライクなところだと思っています。

ネットワーク機器が全て Junos ライクなわけではないですが、ネットワーク機器のような操作感があるため、ネットワークエンジニアがいじりやすいインターフェースになっています。

※私は元々ネットワークエンジニアではないので、よくわかっていません。

### Debian ベース

VyOS は、 Debian ベースの Linux ディストリビューションです。

Debian ベースのため、使い慣れた Linux のコマンドを使うことができます。
また、自分でパッケージを追加し、機能を追加することが可能です。

現状では、 Squeeze ベースになっていますが、より新しい Debian リリースに更新することが、プロジェクトのゴールの1つになっていますので、近い将来、 Wheezy ベースになるのではないかと思います。

### イメージベースのインストール方法

VyOS では、 overlayfs を用いた、イメージベースのインストールを行えるようになっています。

（1.0.x までは unionfs を使っていました。）

これにより、同じホストに複数のバージョンの VyOS をインストールできますので、新しいバージョンへのアップグレードが失敗したときなどに、簡単に前のバージョンの VyOS にロールバックすることが可能になっています。

具体的な方法は、後で書こうと思います。

# 機能

長くなるので、詳しくは後日書きますが、普通のルータとしての機能は大抵揃っています。

また、 Vyatta Core からフォークした後に追加された機能も増えてきていますので、それらについても後日説明したいと思います。

# コミュニティ

VyOS は OSS であり、コミュニティで開発が行われています。

ここでは、コミュニティへの参加の仕方を紹介します。

### 日本のコミュニティ

日本には、世界最大の Vyatta Users Group があるため、 VyOS についても最初から世界最大になっております。

vyos-users.jp では、 [vyos-users.jp][6] というまとめサイトを作っており、 [Wiki][7] の翻訳や、勉強会の開催をしています。

フォーラムとして、 [Google Group][8] を用意していますが、 [Twitter][9] の方が活発です。

Twitter には [vyosjp のアカウント][10]もありますので、何かありましたら、リプライしてください。

また、 IRC の [#vyosjp][11] でもたまに会話しています。

Wiki の翻訳をしてくれる方は常に募集していますし、勉強会の開催を手伝ってくれたり、発表してくれる方も随時募集しています。

ご協力よろしくお願いいたします。

### 勉強会について

現在のところ、世界でも勉強会やミートアップが開催されたのは、日本だけで、これまでに2回開催しています。

だいたい、半年に1度はやろうと思っています。

過去の2回については、下記のページをご参照ください。

* [VyOS Users Meeting Japan #1][12]
* [VyOS Users Meeting Japan #2][13]

発表者や参加者の方々のおかげで、大変濃い内容になっており、私もいつも勉強させていただいています。

### バグ報告について

バグ報告には、やり方があります。

詳しくは、下記のページに日本語訳がありますので、そちらをご参照ください。

[バグ報告の方法][5]

### 開発について

開発は、 GitHub 上で行われています。

開発の Issue もバグと同じように、まずは、 [Bugzilla][4] に登録しており、次のバージョンに含むものには、バージョン番号が入っています。

バージョン番号付けは、 Bugzilla の管理権限を持っているメンテナによって行われており、どのバージョンに入れるかは IRC で相談しています。

# 最後に

本日はギリギリになってしまいましたが、明日以降も書く人がいなければ、 [VyOS Advent Calendar][1] がんばります。

 [1]: http://qiita.com/advent-calendar/2014/vyos
 [2]: http://baturin.org/
 [3]: http://blog.vyos.net/post/72805171110/border-router-upgrade
 [4]: http://bugzilla.vyos.net/
 [5]: http://wiki.vyos-users.jp/%E3%83%90%E3%82%B0%E3%81%AE%E5%A0%B1%E5%91%8A%E6%96%B9%E6%B3%95
 [6]: http://www.vyos-users.jp/
 [7]: http://wiki.vyos-users.jp/
 [8]: http://groups.google.com/d/forum/vyos-users-jp
 [9]: https://twitter.com/hashtag/vyosjp?src=hash
 [10]: https://twitter.com/vyosjp
 [11]: https://webchat.freenode.net/?channels=#vyosjp
 [12]: http://vyosjp.connpass.com/event/6704/
 [13]: http://vyosjp.connpass.com/event/9667/
