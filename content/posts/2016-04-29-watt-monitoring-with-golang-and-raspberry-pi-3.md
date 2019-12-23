---
title: "Golang、Raspberry pi 3、Wi-SUNモジュールを使って電力を監視する"
slug: 2016-04-29-watt-monitoring-with-golang-and-raspberry-pi-3
date: 2016-04-29T23:45:00Z
categories: 
- "Tech"
tags: 
- "raspberry pi"
- "golang"
- "BP35A1"
- "fluentd"
- "easticsearch"
---


![raspberrypi3-with-wsr35a1-00](/images/20160429-raspberrypi3-with-wsr35a1-00.png)


## Wi-SUNモジュールについて

Wi-SUNモジュールは[WSR35A1-00](http://www.rohm.co.jp/web/japan/news-detail?news-title=2014-10-02_news&defaultGroupId=false)を使いました。

Wi-SUNモジュールの使い方は[Raspberry PiとWi-SUNモジュールでスマートメーターから情報取得](http://chappnet.hateblo.jp/entry/2015/08/20/024137)がとても詳しいのでこちらをご参照ください。

## Raspberry pi 3でGolangで書いたものを動かす

Raspberry pi 3上でビルドする必要はありません。他のLinuxとかで下記のように`GOARCH`と`GOARM`を指定してビルドすると、できたバイナリはRaspberry pi 3上で動きます。さすがGolangですね。

```
GOARCH=arm GOARM=7 go build
```

Raspberry pi 3には64bitのARMv8が載っていますが、今のところ、Raspbianは32bitのARMv7用なので`GOARCH=arm64`にすると動きません。`uname`の結果も下記の通りです。

```
pi@raspberrypi:~ $ uname -a
Linux raspberrypi 4.1.19-v7+ #858 SMP Tue Mar 15 15:56:00 GMT 2016 armv7l GNU/Linux
```

## Golangでシリアル通信

[github.com/tarm/serial](https://github.com/tarm/serial)を使いました。

使い方はREADMEに書いてある通りで、とても簡単です。

今回作ったツールでは[bp35a1.go](https://github.com/higebu/wattmonitor/blob/master/bp35a1/bp35a1.go)で使っています。

## ツールについて

プログラムは[GitHub](https://github.com/higebu/wattmonitor)にアップしてあります。

使い方はREADMEを見てください。

このツールはfluentdに投げることを前提にしていますが、ちょっと書き換えれば他の何かに送ることもできると思います。

自分はfluentdからElasticsearchに入れて、直近1時間の消費電力とか、1日の消費電力量を見られるようにしています。

![直近1時間](/images/20160429-es.jpg)
1日の消費電力量はElasticsearch側で計算しています。

![1日の電力量](/images/20160429-es-kwh.jpg)