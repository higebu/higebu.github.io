title: Go と XDP を使って Network Function を作る方法
Slug: how-to-make-network-function-with-go-and-xdp
Date: 2019-01-17 18:30
Category: Tech
Tags: ebpf,xdp,go,network
Summary: Go と XDP を使って Network Function を作る方法。

コントロールプレーンが Go で、データプレーンが XDP な Network Function を作るときのプログラムの構成の話です。

具体的には、以前は [gobpf][1] を使い倒す感じで実装していたのが、今は全く使わなくなっているため、以前の構成と、現在の構成を説明した後に、 [gobpf][1] を使わなくなった理由を書いておきます。

## 以前の構成

* [gobpf][1] で XDP のプログラムをロードして NIC にアタッチ
* ebpf map へのアクセスも [gobpf][1]

これは [examples/bcc/xdp][10] をベースに作っていくと結構簡単に作ることができると思う。

## 現在の構成

* XDP のプログラムは Linux の [samples/bpf][4] や、 [Katran][5] のように自分でビルドしている
    * [samples/bpf][4] 同様、 [tools/testing/selftests/bpf][6] 配下の [bpf_helpers.h][7] などのヘッダファイルをincludeしている
    * ビルドの仕方はだいたいこんな感じ -> [ebpf-template](https://github.com/higebu/ebpf-template)
* できた elf ファイルのロードは [newtools/ebpf][2] を使っている
* ebpf map へのアクセスは [newtools/ebpf][2] を使うか、 [cilium][8] を参考に Go から syscall している
* ロードした XDP のプログラムの NIC へのアタッチは [vishvananda/netlink][9] でやっている

## [gobpf][1] を使わなくなった理由

* XDP のプログラムをロードしたいサーバ全てで [libbcc][3] を入れるのが面倒
* cgo で C++ 製のライブラリを呼んでいて、何かあったときに追うのが面倒
* [libbcc][3] が対応していない機能があったときに機能追加するのが困難
    * [bcc][3] はまだ Map-in-Map に対応していなくて、自分で追加できるかなと思ったけど C++ で Modified C を AST に変換していろいろしているソースを見て、すぐにできるものではないなと思って辞めた
        * Issueはある [Add support to Map-in-Map in BCC #1318](https://github.com/iovisor/bcc/issues/1318)

 [1]: https://github.com/iovisor/gobpf
 [2]: https://github.com/newtools/ebpf
 [3]: https://github.com/iovisor/bcc
 [4]: https://github.com/torvalds/linux/tree/master/samples/bpf
 [5]: https://github.com/facebookincubator/katran
 [6]: https://github.com/torvalds/linux/tree/master/tools/testing/selftests/bpf
 [7]: https://github.com/torvalds/linux/blob/master/tools/testing/selftests/bpf/bpf_helpers.h
 [8]: https://github.com/cilium/cilium/tree/master/pkg/bpf
 [9]: https://github.com/vishvananda/netlink
 [10]: https://github.com/iovisor/gobpf/tree/master/examples/bcc/xdp
