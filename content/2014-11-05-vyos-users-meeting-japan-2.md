Title: VyOS Users Meeting Japan #2 を開催しました
Slug: vyos-user-meeting-japan-2
Date: 2014-11-05 23:00
Category: Tech
Tags: vyos, conference, niftycloud
Summary: VyOS Users Meeting Japan #2 を開催しました。

[VyOS Users Meeting Japan #2][1] を開催しました。

今回は、Patrick van Staveren ([@trickv][2]) さんが上海から仕事で来るタイミングに合わせたため、急な開催となってしまいましたが、自分と Patrick さんを含めて、6人の発表者、32人の参加者となりました。

発表してくれた [@upaa][3] さん、 [@trickv][2] さん、 [@SatchanP][4] さん、 [@hiroysato][5] さん、 [@twovs][6] さん、参加者の皆様ありがとうございました。

[@trickv][2] さんは、 [vyos/build-ami][3] をメンテナンスしているのですが、 [vyos/build-ami][3] の元になっているブログ記事を書いた、 [@j3tm0t0][4] さんと会うことができ、大変喜んでいました。

（本人のブログ記事参照 -> <http://trick.vanstaveren.us/wp/2014/11/02/vyos-users-meeting-japan/>）

日本のコミュニティは世界最大という話がありましたが、新機能を作ったり、バグを直したりしている方が本当に多くて皆さん素晴らしいと思います。

欲しい機能や挙動がおかしいところは、とにかく周りに共有しましょう。

### 自分の発表内容について

* とりあえず発表資料

<iframe src="//www.slideshare.net/slideshow/embed_code/41133818" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/higebu/vyos-110-and-nifty-cloudnew-features" title="20141102 VyOS 1.1.0 and NIFTY Cloud New Features" target="_blank">20141102 VyOS 1.1.0 and NIFTY Cloud New Features</a> </strong> from <strong><a href="//www.slideshare.net/higebu" target="_blank">Yuya Kusakabe</a></strong> </div>

英語しかできない方が来るということで、英語で作りました。発表は日本語です。

1.1.0がリリースされたので、概要だけ触れました。

実際には、自分で触った方が良いと思いますので、中身はあまりしゃべっていません。

また、VyOSが使えるIaaSを紹介しましたが、IDCFさんのクラウドの VyOS のバージョンが 1.0.4 で古いという話をしたところ、それをツイートしてくれた方がいて、IDCFさんが拾ってくれたようです。

<blockquote class="twitter-tweet" lang="ja"><p><a href="https://twitter.com/myb1126">@myb1126</a> さん、ありがとうございます。開発サイドに連絡しました！<a href="https://twitter.com/hashtag/idcfrontier?src=hash">#idcfrontier</a></p>&mdash; IDCフロンティア (@idcfrontier) <a href="https://twitter.com/idcfrontier/status/529557496214880256">2014, 11月 4</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

後半は、自宅の YAMAHA RTX1200 とニフティクラウドの検証環境を L2TPv3 over IPsec でつなぐデモをしました。

時間を短縮するためにすでにできている環境を見せただけだったので、あまり面白くなかったかもしれません。

また、会場のノートPCを自宅に L2TPv2 over IPsec でつないでのデモだったので、レスポンスが悪かったのは申し訳なかったです。

デモで見せた開発中の画面は公開できませんが、リリース後にはわかるので、お楽しみにということで。

### 今後について

発表でも触れましたが、今後もニフティというか自分は、 VyOS に貢献するつもりなので、ミーティングもまた開催します。

次回は、新機能を使ってみた系の話や、今回もあったような VyOS を本気で使っている事例がより集まると良いと思っています。

あと、 VyOS のステッカー作りたいので、おすすめの作り方がある方はご連絡ください。


 [1]: http://vyosjp.connpass.com/event/9667/
 [2]: https://twitter.com/trickv
 [3]: https://twitter.com/upaa
 [4]: https://twitter.com/SatchanP
 [5]: https://twitter.com/hiroysato
 [6]: https://twitter.com/otsuka752
