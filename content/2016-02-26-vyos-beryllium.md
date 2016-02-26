title: VyOS Beryllium について
Slug: 2016-02-26-vyos-beryllium
Date: 2016-02-26 08:00
Category: Tech
Tags: vyos
Summary: 開発中の VyOS Berylliumのまとめです。

## Beryllium

* 詳しくは[Wiki](http://vyos.net/wiki/Beryllium)参照
    * 大体このページの翻訳です
* Debian jessie ベース
    * 必然的に Systemd 対応を強いられる
* Linux 4.4.0
* 新しいビルドスクリプト
    * [vyos-build][vyos-build]
    * [build-iso](https://github.com/vyos/build-iso)から変更
    * 日本の[VyOS Users Meeting #2](http://vyosjp.connpass.com/event/9667/)にも来た[trickv](https://twitter.com/trickv)さんがAMIのビルドスクリプト作ってる [https://github.com/trickv/vyos-build/tree/vm](https://github.com/trickv/vyos-build/tree/vm)
* メタパッケージ、[vyos-world](https://github.com/vyos/vyos-world)
    * VyOS独自パッケージのまとめ
    * [パッケージリスト](https://github.com/vyos/vyos-world/blob/current/debian/control)
* DebianのパッケージをVyOSのリポジトリに置くのをやめて、Debianのリポジトリから取ってくるようにする
    * 今は必要なパッケージをVyOSのリポジトリにコピーしている
    * さらにVyOS以外でも使えるパッケージ（eventwatch, hvinfo, ipaddrcheckなど）はDebianのリポジトリに置いて、なるべく自分たちでビルドするパッケージを少なくする
    * 参考
        * [[Vyos-developers] End of squeeze-lts support, lithium,  and what to do next](https://lists.tuxis.nl/pipermail/vyos-developers/2016-January/000150.html)
        * [[Vyos-developers] Updates on squeeze-lts EOL and jessie migration issues](https://lists.tuxis.nl/pipermail/vyos-developers/2016-January/000177.html)
* 開発フローの変更
    * current ブランチが最新になる
        * Vyatta Core時代からの歴史的経緯によりmasterを使うのが難しいため
    * beryllium リリース時に beryllium ブランチが切られる
    * 新機能やバグフィックスは基本的に current にマージしていき、各リリースブランチにはバックポートで対応する
    * 中心的なメンテナはcurrentの開発に集中しているため、現行のHeliumやLithiumのメンテナンスは人を募集している
* リリースまでの流れ
    1. [vyos-build][vyos-build] を作る
    2. Kernelアップグレード
    3. 各パッケージをコンパイルできるか確認
        1. 必要ならupstreamに合わせてパッケージを入れ替えたりする
    4. ブートまでのバグを修正
    5. ビルドプロセスで公式AMIも作る
    6. すべてテストしてバグを直す
        * [Serverspec](https://github.com/mizzy/serverspec)を使う
        * [primeroz/serverspec_vyos_testing](https://github.com/primeroz/serverspec_vyos_testing)をベースにするっぽい
        * [Jenkins](https://ci.vyos.net/)でCIする

## 個人的にやりたいこと

* Virtual boxやVMware用の公式イメージの提供
    * 個人的に作っているVagrant用のbox
        * [vyos-1.1.7-amd64](https://atlas.hashicorp.com/higebu/boxes/vyos-1.1.7-amd64)
        * [vyos-1.2.0-beta1-amd64](https://atlas.hashicorp.com/higebu/boxes/vyos-1.2.0-beta1-amd64)
* Docker対応
    * Dockerが動くようにしたい
    * Jessieになるので簡単そう
    * [前にやってたやつ](blog/2014/12/10/docker-on-vyos/)

## 最近困ったこと（おまけ）

* webproxy(squid 3.1.6)で `http://xxx.xxx.xxx.xxx:3128/squid-internal-dynamic/netdb`などの`squid-internal-xxx`へのアクセスがループしてcache.logがあふれた
    * VyOSに入っているsquidではnetdbは無効のはずなのになぜか内部的にこのURLが叩かれて死んだ
    * バージョンアップすれば直るけど、コンフィグを直す必要があり、VyOSのコマンドで設定できなくなりそう
        * Stableの3.5.15にしたら直ったけどそのままのコンフィグだと起動しなかった
        * [ビルド方法](https://gist.github.com/higebu/2cb3c4c8fc1e236716ce)
        * 3.5.15だと下記のようなレスポンスが返ってくる

            ```
            curl http://xxx.xxx.xxx.xxx:3128/squid-internal-dynamic/netdb                                                                                       
            NETDB support not compiled into this Squid cache.
            ```

    * Jessieでは3.4.8なのでたぶん直っているはず(未確認)

 [vyos-build]: https://github.com/vyos/vyos-buld
