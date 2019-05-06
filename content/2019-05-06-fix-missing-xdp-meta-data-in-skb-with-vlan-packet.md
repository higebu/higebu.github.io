title: XDP の meta data が VLAN のパケットのときに失われるバグを修正して Linux Kernel に貢献した
Slug: fix-missing-xdp-meta-data-in-skb-with-vlan-packet
Date: 2019-05-06 14:30
Category: Tech
Tags: ebpf,xdp,network,linux,debian
Summary: XDP の meta data が VLAN のパケットのときに失われるバグを修正して Linux Kernel に貢献した

## パッチについて

パッチは [こちら][1] で、stable では [4.19.37][2] か [5.0.10][3] からこの修正が入っています。

内容としては `bpf_xdp_adjust_meta()` でパケットに付けたメタデータが skb のビルドプロセス内の `skb_vlan_untag()` (さらに詳しく言うと `skb_reorder_vlan_header()` ) で失われて tc の cls_bpf などで参照できない問題を修正したものです。

## Linux へのパッチの送り方について

公式ドキュメントにパッチの送り方 [Submitting patches: the essential guide to getting your code into the kernel][4] が書いてあるので、これを読めばだいたいわかるようになっていた。

また、今回はネットワーク関連だったので、 [netdev FAQ][5] も読んだところ、バグフィックスは [net][6] ブランチ、新機能は [net-next][7] ブランチということがわかり、 [net][6] ブランチにパッチを送るべきということがわかった。

その他に注意する点として、メールの送り方があり、これは [Email clients info for Linux][8] というページにまとまっている。

自分はこれを読まずにGmail Web Clientでメールしてしまい、 [タブが全滅したパッチ][9] を送ってしまった。

## Debian でのカーネルのビルド方法について

[Debian Linux Kernel Handbook][10] の [Chapter 4. Common kernel-related tasks][11] が詳しいです。

`LOCALVERSION` を付けておくとわかりやすいので下記のようなコマンドでビルドしています。

```
make -j`nproc` LOCALVERSION=-hoge bindeb-pkg
```

 [1]: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=d85e8be2a5a02869f815dd0ac2d743deb4cd7957
 [2]: https://cdn.kernel.org/pub/linux/kernel/v4.x/ChangeLog-4.19.37
 [3]: https://cdn.kernel.org/pub/linux/kernel/v5.x/ChangeLog-5.0.10
 [4]: https://www.kernel.org/doc/html/latest/process/submitting-patches.html
 [5]: https://www.kernel.org/doc/html/latest/networking/netdev-FAQ.html
 [6]: https://git.kernel.org/pub/scm/linux/kernel/git/davem/net.git
 [7]: https://git.kernel.org/pub/scm/linux/kernel/git/davem/net-next.git
 [8]: https://www.kernel.org/doc/html/latest/process/email-clients.html
 [9]: https://patchwork.ozlabs.org/patch/1085113/
 [10]: https://kernel-team.pages.debian.net/kernel-handbook/index.html
 [11]: https://kernel-team.pages.debian.net/kernel-handbook/ch-common-tasks.html