Title: Alpine Linux ベースで Docker イメージを作ると小さくて良い
Slug: build-docker-images-based-on-alpine-linux
Date: 2015-06-15 02:00
Category: Tech
Tags: docker, alpinelinux
Summary: Alpine Linux の Docker イメージは 5 MB くらいしかないので、これをベースにイメージを作ると小さくて良い

[TOC]

## Alpine Linux の Docker イメージのサイズ

最近仕事でいくつか Docker イメージを作っているんですが、その際の参考のために [Docker Hub](https://hub.docker.com/) を漁っていたら、 `FROM alpine` なイメージのサイズがとても小さいことを知りました。

[alpine:3.2](https://registry.hub.docker.com/_/alpine/) は 5.242MB しかありません。

Ubuntu など他の OS のイメージのサイズと比較してみると 100 MB 以上差があることがわかります。

| REPOSITORY:TAG | VIRTUAL SIZE |
|:---------------|:-------------|
| alpine:3.2     | 5.242 MB     |
| debian:jessie  | 125.2 MB     |
| ubuntu:trusty  | 188.3 MB     |
| fedora:22      | 186.5 MB     |

Docker はベースのイメージを初回しかダウンロードしないので、あまり気にする必要はないと思うかもしれませんが、数百台、数千台のクラスタを構築したいと思った時に、クラスタ全体が立ち上がるまでの時間が短縮されますし、ストレージもかなり節約できます。

そんなわけで、今後は Ubuntu でないと動かないなどという制約でもない限り、 [Alpine Linux][1] ベースでイメージを作っていこうと思っています。

## Alpine Linux ベースで Docker イメージを作る

例えば、zabbix-agent の Dockerfile は下記のような感じになります。

```
FROM alpine:latest

RUN apk --update add zabbix-agent \
     && rm -rf /var/cache/apk/*

COPY docker-entrypoint.sh /docker-entrypoint.sh

EXPOSE 10050

ENTRYPOINT ["/docker-entrypoint.sh"]
```

ソースは [GitHub](https://github.com/higebu/docker-zabbix-agent) に置いてあります。

[Alpine Linux][1] では [apk](http://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management) というコマンドでパッケージを管理します。

また、初期状態では下記の 15 パッケージしか入っておらず、必要なパッケージを自分でかなり入れる必要がある場合もあります。

```
# apk info
musl
busybox
alpine-baselayout
openrc
alpine-conf
zlib
libcrypto1.0
libssl1.0
apk-tools
busybox-initscripts
scanelf
musl-utils
libc-utils
alpine-keys
alpine-base
```

それ以外は他の Linux ディストリビューションと大きく違う点はないと思います。

ちなみに先ほどの [zabbix-agent のイメージ](https://registry.hub.docker.com/u/higebu/zabbix-agent/) は 8.527 MB で、 [Ubuntu でも作ってみた所](https://registry.hub.docker.com/u/higebu/zabbix-agent-ubuntu/)、 200.9 MB になりました。

[fluentd のイメージ](https://registry.hub.docker.com/u/higebu/fluentd/) は 176.7 MB になり、 [fluent/fluentd](https://registry.hub.docker.com/u/fluent/fluentd/) の半分以下のサイズなのですが、 ruby 自体が大きいためこれよりは小さくできなそうです。

以下、参考までに `docker images` の結果を貼っておきます。

```
% docker images
REPOSITORY                   TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
higebu/zabbix-agent-ubuntu   latest              eb7588d9a7f7        10 minutes ago      200.9 MB
higebu/fluentd               latest              889b0fa11ffc        About an hour ago   176.7 MB
fluent/fluentd               latest              212de73247af        2 days ago          491.4 MB
higebu/zabbix-agent          latest              31471e804003        4 days ago          8.527 MB
ubuntu                       latest              fa81ed084842        6 days ago          188.3 MB
ubuntu                       trusty              fa81ed084842        6 days ago          188.3 MB
alpine                       3.2                 8697b6cc1f48        9 days ago          5.242 MB
alpine                       latest              8697b6cc1f48        9 days ago          5.242 MB
```

 [1]: http://alpinelinux.org/
