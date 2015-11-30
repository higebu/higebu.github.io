Title: VyOSを触り始めて少し経った人向けのFAQ
Slug: vyos-faq-for-beginners
Date: 2015-12-01 00:00
Category: Tech
Tags: vyos, vyatta
Summary: VyOSを触り始めて少し経った人向けのFAQです。

最終更新: 2015/12/01

これは、[VyOS Advent Calendar 2015](http://qiita.com/advent-calendar/2015/vyos)の1日目の記事です。

VyOSを触り始めるといろいろと疑問が湧いてくるのですが、調べるのが大変なことも多いので、まとめておきます。

初めて触る人向けの情報をまとめようと思っていたのですが、少し経ったくらいで気になることばかりになってしまいました。

内容は思いついたときに随時更新していくかもしれません。

以下、FAQです。

[TOC]

### 次のバージョンはいつ出るのか

VyOSのリリースのコードネームは元素名になっています。2015/12/01現在の最新は`Helium`なので、次は`Lithium`です。

`Lithium`についてのページは下記のURLです。

http://vyos.net/wiki/Lithium

Estimated release dateがSpring 2015になってますが、まだ出ていません。このページのRoadmapの`CONFIRMED`や`IN_PROGRESS`でSeverityが高いものが`RESOLVED`になればリリースされるかもしれません。

そろそろリリースしようかという話は、[開発者メーリス](https://lists.tuxis.nl/listinfo/vyos-developers)で流れています。

それぞれのIssueの進捗は[Bugzilla][0]で確認しましょう。

### 新しいDebianベースにならないのか

[@UnicronNL](https://github.com/UnicronNL)さんががんばっていましたが、最近忙しくて進んでいないようです。他にやっている人もいなそうなので、誰か手伝ってくれると助かると思います。

下記のURLにJessieに対応しようとしていたブランチがあります。

https://git.multi.eu/vyos/build-iso/tree/jessie-transit

### StrongSwanのバージョン新しくならないのか

[Bugzilla][0]に[Issue](http://bugzilla.vyos.net/show_bug.cgi?id=471)があるので、これを監視するか、テストに協力しましょう。

また、他のソフトの場合も同じなのですが、[Bugzilla][0]にIssueを作らないと新しいバージョンが出ていても需要がないのかなと思われてしまうのでIssueあげると良いです。

### Debianのパッケージを入れたい

やり方が公式FAQに載っています。

http://vyos.net/wiki/FAQ#How_do_I_install_debian_packages

### 古いバージョンのVyattaのISOやドキュメントが欲しい

VyOSはVyatta 6.5からフォークしたものなので、Vyattaのドキュメントが参考になったりします。

公式サイトからはなくなっていますが、下記のURLの配下にISOなどがアーカイブされています。

* ftp://ftp.het.net/iso/vyatta/
* http://docs.huihoo.com/vyatta/

ちなみに1つ目の方は[IRC](https://webchat.freenode.net/?channels=#vyos)で`@vyatta archive`と打つと`vybot`が教えてくれます。

失われてしまったVyattaのHacker Forumは下記のページで2013/06/01のスナップショットが見られます。

http://web.archive.org/web/20130601170522/http://vyatta.org/forum

困っていることは昔と変わらないことが多いので大変参考になります。

### カーネルをカスタマイズしてビルドしたい

自分のgistで申し訳ないですが、下記を参考にしてください。

https://gist.github.com/higebu/409c00db4aa1256e405b

普通にカーネルをリビルドしたい場合は、[公式ドキュメント](http://vyos.net/wiki/Rebuild_VyOS_kernel_Step)が参考になります。

### Intel DPDK対応しないのか

メンテナ少ないし、Debianの新しいバージョンに追随したり、バックエンドをきれいにする方をがんばりたいという話になっています。

素直にVyatta vRouter使うのがおすすめです。

もし自分で実装したという方がいらっしゃいましたら、プルリクエストお願いします。

### vyconfdはどこに行ってしまったのか

一旦開発停止して、下記URLに移動しています。

https://github.com/vyos-legacy/vyconfd


 [0]: http://bugzilla.vyos.net/
