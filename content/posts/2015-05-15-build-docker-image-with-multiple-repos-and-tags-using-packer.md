---
title: Packer で複数のリポジトリ名や複数のタグが付いた Docker イメージを作る
slug: build-docker-image-with-multiple-repos-and-tags-using-packer
date: 2015-05-15T11:00:00Z
categories: 
- "Tech"
tags: 
- "packer"
- " docker"
---


[TOC]

## 環境

* Ubuntu 15.04
* Docker 1.6.0
* Packer 0.7.5

## 例

いきなりですが、実際の例を見た方が早いので、テンプレートの例です。

```json
{
  "builders":[{
    "type": "docker",
    "image": "fedora",
    "commit": "true"
  }],
  "provisioners":[
    {
      "type": "shell",
      "inline": [
        "yum update -y",
        "yum clean all"
      ]
    }
  ],
  "post-processors": [
    [
      {
        "type": "docker-tag",
        "repository": "higebu/fedora1",
        "tag": "0.1"
      },
      "docker-push"
    ],
    [
      {
        "type": "docker-tag",
        "repository": "higebu/fedora1",
        "tag": "latest"
      },
      "docker-push"
    ],
    [
      {
        "type": "docker-tag",
        "repository": "higebu/fedora2",
        "tag": "0.1"
      },
      "docker-push"
    ],
    [
      {
        "type": "docker-tag",
        "repository": "higebu/fedora2",
        "tag": "latest"
      },
      "docker-push"
    ]
  ]
}
```

`tag` の部分に配列を渡せたらきれいなんですが、現状渡せないので、少し複雑なテンプレートになってしまっています。

これを使って `packer build` すると `higebu/fedora1:0.1`、`higebu/fedora1:latest`、`higebu/fedora2:0.1`、`higebu/fedora2:latest` が [Docker Hub](https://hub.docker.com/) 上に作成されます。

複数のタグを付けようと思って試していたら、複数のリポジトリもいけると気づいたんですが、何に使うのかは不明です。


## 解説

普通に `docker-tag` post proccessor を並べると

```
* Post-processor failed: Unknown artifact type: packer.post-processor.docker-tag
Can only tag from Docker builder artifacts.
```

というエラーになります。
エラーメッセージには、Docker builder の artifacts しかタグ付けられないよと書いてあるんですが、実際には `docker-import` post proccessor の artifacts も受け取れますし、Docker Builder でも、`export_path` を指定してエクスポートたものは受け取れません。

普通に並べるというのは下記のような感じです。

```json
  "post-processors": [
    [
      {
        "type": "docker-tag",
        "repository": "higebu/fedora1",
        "tag": "0.1"
      },
      {
        "type": "docker-tag",
        "repository": "higebu/fedora1",
        "tag": "latest"
      },
      "docker-push"
    ]
  ]
```

これだと、`docker-tag` で処理されたものが `docker-tag` に渡されてしまいエラーになるので、上の例では並列にならべて、それぞれ `docker-push` しています。
また、`export_path` ではなく、 `"commit": "true"` にして、エクスポートしないようにしています。
