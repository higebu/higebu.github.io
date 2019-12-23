---
title: "TCPパケットがGeneric XDPで処理されない件について"
slug: tcp-packet-is-not-processed-by-generic-xdp
date: 2018-11-07T12:55:00Z
categories: 
- "Tech"
tags: 
- "ebpf"
- "xdp"
- "tcp"
---


Twitterにも書いたけど忘れそうなのでメモしておく。

下記の図のような構成でns2のveth2とveth3にXDPのプログラムをアタッチし、 `XDP_REDIRECT` でns1とns3の間でパケットが往復できるかどうかテストしていたときにTCPのパケットだけ通らなかった。

![network-diagram](/images/20181107-network-diagram.png)
ググったところ下記のメールスレッドが見つかり、結論としてはGeneric XDPではTCPのパケットがPASSされていて、アタッチしたXDPのプログラムを通らない。

[Generic XDP and veth](https://www.spinics.net/lists/xdp-newbies/msg00440.html)

実際のソースは [ここ](https://github.com/torvalds/linux/blob/v4.18/net/core/dev.c#L4028-L4032) でXDPのプログラムに入る前に `XDP_PASS` している。

回避策としては、Native XDPをサポートしているNICを使うか、下記のパッチをカーネルに当てるかで、カーネルのパッチで回避ができることは確認した。

[cilium/cilium#3077 (comment)](https://github.com/cilium/cilium/issues/3077#issuecomment-430801467)
