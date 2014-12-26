Title: VyOS Users Meeting Japan #1を開催しました
Slug: vyos-user-meeting-japan-1
Date: 2014-07-27 23:00
Category: Tech
Tags: vyos, conference, vagrant, ansible
Summary: VyOS Users Meeting Japan #1を開催しました。

[ニフティクラウドユーザーブログ][1]にも書きましたが、[VyOS Users Meeting Japan #1][2]を開催しました。

* 発表資料

<iframe src="//www.slideshare.net/slideshow/embed_code/37392861" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/higebu/20140727-vyos-users-meeting-japan-1" title="20140727 VyOS Users Meeting Japan #1 VyOS 概要とデモ" target="_blank">20140727 VyOS Users Meeting Japan #1 VyOS 概要とデモ</a> </strong> from <strong><a href="//www.slideshare.net/higebu" target="_blank">Yuya Kusakabe</a></strong> </div>

VyOSができた経緯、Vyatta CoreからVyOSへの移行方法、VyOSのロードマップ、vyos-users.jpについて話した後、[vagrant][3]と[ansbile][4]を使ったデモを行いました。

デモで使ったVagrantfileとplaybookは、GitHubに置いてあります。

https://github.com/higebu/vagrant-ansible-examples-with-vyos/tree/master/site-to-site-ipsec-vpn

試し方はとても簡単で、VagrantとAnsibleをインストールした上で、下記のコマンドを実行するだけです。

```
vagrant plugin install vagrant-vyatta
git clone git@github.com:higebu/vagrant-ansible-examples-with-vyos.git
cd vagrant-ansible-examples-with-vyos/site-to-site-ipsec-vpn
vagrant up
```

コマンドに慣れていれば、素のLinuxのコマンドやコンフィグファイルをいじるより、わかりやすいため、自動化しやすいと思います。

L2TPv3の方はうまく動かない状態になっている気がするので、いつか直しておきたいと思います。

 [1]: http://blog.cloud.nifty.com/2307/
 [2]: http://vyosjp.connpass.com/event/6704/
 [3]: https://www.vagrantup.com/
 [4]: http://www.ansible.com/home
