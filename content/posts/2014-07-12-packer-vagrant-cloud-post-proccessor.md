---
title: Packer の Vagrant Cloud Post-Proccessor を試してみた
slug: packer-vagrant-cloud-post-proccessor
date: 2014-07-12T00:00:00+09:00
categories: 
- "Tech"
tags: 
- "packer"
- "vagrant"
- "virtualbox"
- "vmware"
---


Packer の次のバージョンで Vagrant Cloud Post-Proccessor が追加されるようで、 master ブランチではすでに使えるので試してみました。

[公式ドキュメント][1]では、2014/07/14 リリース予定になっています。

 [1]: http://www.packer.io/docs/post-processors/vagrant-cloud.html

ただし、この機能は Vagrant Cloud のホスティング機能を利用しているため、  Vagrant Cloud の有償プランにアップグレードしておく必要があります。

Pro でも毎月 $2 なので、 HashiCorp, Inc にお世話になっている方は払っておくといいと思いますｗ

<https://vagrantcloud.com/account/plans>

あと、 Vagrant Cloud がβじゃなくなってます。

<http://www.hashicorp.com/blog/vagrant-cloud-end-of-beta.html>


環境
----

* Ubuntu 14.04
* Go 1.3
* Packer 0.6.1.dev
* Vagrant 1.6.3

インストール
------------

* Go 言語をインストール

```bash
wget https://go.googlecode.com/files/go1.3.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.3.linux-amd64.tar.gz
```

* 環境変数の設定

下記を `.bash_profile` などに追記

```bash
export GOROOT=/usr/local/go
export PATH=$PATH:$GOROOT/bin
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin
```

* Packer をインストール

```bash
sudo apt-get install mercurial bzr
go get -u github.com/mitchellh/gox
git clone https://github.com/mitchellh/packer.git ~/go/src/github.com/mitchellh/packer
cd ~/go/src/github.com/mitchellh/packer
make
cp -p pkg/linux_amd64/* ~/go/bin/
```

テンプレート
------------

Post-Proccessor で vagrant の後に vagrant-cloud が動くようにします。

Builder などは省略していますが、下記のようになります。

```json
  "variables": {
    "version": "",
    "cloud_token": ""
  },
  "post-processors": [
    [{
      "type": "vagrant",
      "output": "./vyos-1.0.4-amd64_{{.Provider}}.box"
    },
    {
      "type": "vagrant-cloud",
      "access_token": "{{user `cloud_token`}}",
      "box_tag": "higebu/vyos-1.0.4-amd64",
      "version": "{{user `version`}}",
      "version_description": "Initial release"
    }]
  ],
```

実際のテンプレートは Github で公開しています。

<https://github.com/higebu/packer-templates/tree/master/VyOS-1.0.4-amd64>

ビルド
------

ビルドする前に Vagrant Cloud で box を作成しておく必要があります。

User Variables で `version` と `cloud_token` を指定できるようにしているので、下記のようになります。

`cloud_token` は自分のものと置き換えてください。

```bash
packer build -only=virtualbox-iso -var 'version=1.0.0' -var 'cloud_token=#####' template.json
packer build -only=vmware-iso -var 'version=1.0.0' -var 'cloud_token=#####' template.json
```

ビルドしたものは下記にあります。

<https://vagrantcloud.com/higebu/vyos-1.0.4-amd64>
