title: Golang、Raspberry pi 3、Wi-SUNモジュールを使って電力を監視する
Slug: 2016-04-29-watt-monitoring-with-golang-and-raspberry-pi-3
Date: 2016-04-29 23:45
Category: Tech
Tags: raspberry pi,golang,BP35A1,fluentd,easticsearch
Summary: Golang、Raspberry pi 3、Wi-SUNモジュールを使って電力を監視するツールを作った話です。

{% img /images/20160429-raspberrypi3-with-wsr35a1-00.png 800 594 raspberrypi3-with-wsr35a1-00 %}

## 目次

[TOC]

## Wi-SUNモジュールについて

Wi-SUNモジュールは[WSR35A1-00](http://www.rohm.co.jp/web/japan/news-detail?news-title=2014-10-02_news&defaultGroupId=false)を使いました。

Wi-SUNモジュールの使い方は[Raspberry PiとWi-SUNモジュールでスマートメーターから情報取得](http://chappnet.hateblo.jp/entry/2015/08/20/024137)がとても詳しいのでこちらをご参照ください。

## Raspberry pi 3でGolangで書いたものを動かす

Raspberry pi 3上でビルドする必要はありません。他のLinuxとかで下記のように`GOARCH`と`GOARM`を指定してビルドするだけです。さすがGolangですね。

```
GOARCH=arm GOARM=7 go build
```

Raspberry pi 3には64bitのARMv8が載っていますが、今のところ、Raspbianは32bitのARMv7用なので`GOARCH=arm64`にすると動きません。`uname`の結果も下記の通りです。

```
pi@raspberrypi:~ $ uname -a
Linux raspberrypi 4.1.19-v7+ #858 SMP Tue Mar 15 15:56:00 GMT 2016 armv7l GNU/Linux
```

## このツールについて

プログラムは[GitHub](https://github.com/higebu/wattmonitor)にアップしてあります。

使い方はREADMEを見てください。

このツールはfluentdに投げることを前提にしていますが、ちょっと書き換えれば他の何かに送ることもできると思います。

自分はfluentdからElasticsearchに入れて、直近1時間の消費電力とか、1日の消費電力量を見られるようにしています。

{% img /images/20160429-es.jpg 1351 632 直近1時間 %}

1日の消費電力量はElasticsearch側で計算しています。

{% img /images/20160429-es-kwh.jpg 1024 477 1日の電力量 %}
