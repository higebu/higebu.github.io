title: 2018年振り返り
Slug: look-back-2018
Date: 2018-12-28 22:35
Category: Life,Tech
Tags: life
Summary: 2018年振り返り

2018年振り返りです。

# 仕事

2月に[さくらのセキュアモバイルコネクトをリリース](https://www.sakura.ad.jp/information/announcements/2018/02/01/1855/)した。
2016年8月に転職してからずっとやっていたので、とりあえずリリースできてよかったです。
実際には2017年5月くらいまでは sakura.io の裏の回線のみやる予定だったのが、突然これもやることになったり、リリースまではいろいろと困難があった。

リリース後もエンジニアリング全般とキャリアとのやり取りなどいろいろやっていて頭の切り替えが難しいなと言いまくっていました。
しかし、そのわりには案外機能追加もできていて、特に[SIMルート](https://cloud-news.sakura.ad.jp/2018/06/12/sim-root/)と[マルチキャリア対応](https://cloud-news.sakura.ad.jp/2018/11/28/multi-sim/)は作る方も面白かったです。

SIMルートはIPの世界の人ならただのL3トンネルではという感覚だと思いますが、モバイルの世界では新しかったらしく、人生で初めて特許出願までしました。詳しくは[こちら](https://sakura.io/blog/2018/09/18/simroute/)

マルチキャリア対応では、自作のHSSとPGWでキャリア毎に微妙に違う挙動をするMMEとSGWとの相互接続を実現できて何かに勝った気持ちになりました。

# Output

対外発表はあまりしておらず、[とうほぐモバイルミーティング #2](https://tohogu.connpass.com/event/84268/)とJANOG42での[GoでEPC作って本番運用している話](https://www.janog.gr.jp/meeting/janog42/program/goepc)をしたくらいでした。

VyOSの開発は40コミットくらいしかできていなかった。仕事ではないので厳しいという感じで、今後もネタがあって気が向いたら貢献するくらいのペースでゆるく続けるのがいいのかなと思っている。

その他外部リポジトリにマージしてもらったプルリクは [GitHub](https://github.com/pulls?utf8=✓&q=is%3Apr+author%3Ahigebu+archived%3Afalse+is%3Amerged+created%3A2018-01-01..2018-12-31) でだいたい確認できる。

XDP でいろいろやっているときにお世話になっている [iovisor/gobpf](https://github.com/iovisor/gobpf) や [vishvananda/netlink](https://github.com/vishvananda/netlink) の開発に少し貢献できたのがよかった。
