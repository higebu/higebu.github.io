title: TCPパケットがGeneric XDPで処理されない件について
Slug: tcp-packet-is-not-processed-by-generic-xdp
Date: 2018-11-07 12:55
Category: Tech
Tags: ebpf,xdp,tcp
Summary: TCPパケットがGeneric XDPで処理されなかったので調べた。

Twitterにも書いたけど忘れそうなのでメモしておく。

下記の図のような構成でns2のveth2とveth3にXDPのプログラムをアタッチし、 `XDP_REDIRECT` でns1とns3の間でパケットが往復できるかどうかテストしていたときにTCPのパケットだけ通らなかった。

{% img /images/20181108-network-diagram.png 1009 262 network-diagram network-diagram %}

ググったところ下記のメールスレッドが見つかり、結論としてはGeneric XDPではTCPのパケットがPASSされていて、アタッチしたXDPのプログラムを通らない。

[Generic XDP and veth](https://www.spinics.net/lists/xdp-newbies/msg00440.html)

実際のソースは [ここ](https://github.com/torvalds/linux/blob/v4.18/net/core/dev.c#L4028-L4032) でXDPのプログラムに入る前に `XDP_PASS` している。

回避策としては、Native XDPをサポートしているNICを使うか、下記のパッチをカーネルに当てるかで、カーネルのパッチで回避ができることは確認した。

[cilium/cilium#3077 (comment)](https://github.com/cilium/cilium/issues/3077#issuecomment-430801467)
