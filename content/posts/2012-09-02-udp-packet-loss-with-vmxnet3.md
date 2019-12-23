---
title: VMware上のVMでvNICをVMXNET3にしたときにUDPのパケットが飛ばない現象のまとめ
slug: udp-packet-loss-with-vmxnet3
date: 2012-09-02T00:00:00+09:00
aliases:
- archives/441
categories: 
- "Tech"
tags: 
- "vmware"
- "packet"
- "udp"
- "vmxnet3"
- "network"
---

ESXi上のVMで fluentd → fluentd しようとしたらハートビート用のudpの通信ができていなかったので、調べた結果のまとめ。

調べた範囲ではパターンは3つ。

vNICは全てVMXNET3です。

E1000にすると直ります。

ESX or ESXi 4.0 4.1でVMのOSがRHEL 5.3以上の場合

以下のVMwareのKBに当てはまります。

[UDP packet loss with MSI interrupts on VMXNET3](http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=1026055 "UDP packet loss with MSI interrupts on VMXNET3")

いくつか対処法が載っているけど、ESXを4.1u1以上にするのがいいですね。

VMのOSがRHEL6系の場合

以下のRed Hat KBに当てはまります。

[Why does the vmxnet3 driver shipped with RHEL 6 update 2 drops small UDP packets?](https://access.redhat.com/knowledge/ja/node/67823 "Why does the vmxnet3 driver shipped with RHEL 6 update 2 drops small UDP packets?")

カーネルをアップデートすると直るけど、あまりやりたくないですね。

とりあえず、楽にカーネルをアップデートしたいときは[ELRepo](http://elrepo.org/tiki/tiki-index.php "ELRepo")を使うといいです。

CentOS6.4でカーネルを3.5.3にしたら直ったのは確認しました。

ESXi5系の場合

以下のVMwareのKBに当てはまります。

[UDP packets are dropped from Linux systems using the VMXNET3 Network Adapter](http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=2019944 "UDP packets are dropped from Linux systems using the VMXNET3 Network Adapter")

<del>これはもうどうしようもない。</del>

<del>最後のは何とかして欲しいですね。。</del>

追記：パッチが出ていて、それを当てれば直るようです。
