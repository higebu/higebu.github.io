---
title: "XDP のプログラムをビルドする方法"
slug: how-to-build-xdp-program
date: 2019-01-20T0:30:00Z
categories: 
- "Tech"
tags: 
- "ebpf"
- "xdp"
- "network"
---


## 前置き

社内向けにコントロールプレーンが Go で、データプレーンが XDP な Network Function を作る方法をまとめていましたが、特に社内に閉じている必要のない情報なので、こちらに書いていきます。

Go で XDP/eBPF というと [gobpf][1] が [IO Visor](https://www.iovisor.org/) 公式ということもあって有名ですが、いろいろあって使っていません。

使わなくなった理由は後で。。。

[gobpf][1] を使わない場合、自分で XDP のプログラムをビルドする必要があります。

そこで、とりあえずビルドする方法についてまとめておきます。

## XDP のプログラムをビルドする方法

XDP のプログラムをビルドするときに参考になるのは Linux の [samples/bpf][2] や Facebook の [Katran][3] で、どちらもカーネルのソースツリー内でビルドする方法を取っています。

説明するのが面倒なので、 XDP のプログラムをビルドするためのテンプレートとして [ebpf-template][7] を作りました。

`git clone` した後に、 `./setup.sh` して `./build.sh` が通ったら XDP のプログラムを開発する環境がすでに整っていて、通らなかったら、何か足りないのでパッケージを入れるなりして解決してください。

Debian の場合 `gcc clang llvm make linux-headers-amd64 bison flex libelf-dev bc libssl-dev` 辺りは必要です。

このテンプレートでは [tools/testing/selftests/bpf][4] 配下の [bpf_helpers.h][5] などを使うことを前提にしています。

そのため、 `#include "bpf_helpers.h"` をして、 `bpf_map_lookup_elem` などの関数を使えて、 [samples/bpf][2] 配下のプログラムと同じ雰囲気で開発することができます。

また、ビルド環境は Docker コンテナにもしてあるので、こちらも参考にしてください。

[higebu/ebpf-build][6]

 [1]: https://github.com/iovisor/gobpf
 [2]: https://github.com/torvalds/linux/tree/master/samples/bpf
 [3]: https://github.com/facebookincubator/katran
 [4]: https://github.com/torvalds/linux/tree/master/tools/testing/selftests/bpf
 [5]: https://github.com/torvalds/linux/blob/master/tools/testing/selftests/bpf/bpf_helpers.h
 [6]: https://cloud.docker.com/repository/docker/higebu/ebpf-build
 [7]: https://github.com/higebu/ebpf-template
