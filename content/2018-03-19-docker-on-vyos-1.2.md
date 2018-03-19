title: VyOS 1.2でDockerを動かす
Slug: docker-on-vyos-1.2
Date: 2018-03-19 12:43
Category: Tech
Tags: vyos,docker
Summary: VyOS 1.2でDockerを動かす

最近、VyOS 1.2のカーネルでコンテナを動かすのに必要なオプションを有効にしたので、Dockerも動くようになりました。
追加したときのPRは[これ](https://github.com/vyos/vyos-kernel/pull/16)と[これ](https://github.com/vyos/vyos-kernel/pull/17)で、4.4系のカーネルに入れたのにすぐに4.14系になって、そのとき漏れてたものを追加したので2回になっている。）

### 準備

VyOS 1.2はまだリリースされていませんが、開発版を下記からダウンロードできます。

https://downloads.vyos.io/?dir=rolling/current/amd64

これをどこかで動かしてください。

このとき、Dockerストレージ用のディスクを追加で付けておきます。（ここでは `/dev/vdb` として認識されるとします。）

Dockerストレージ用のディスクを別にするのは、VyOSではルートディスクをすでにoverlayfsでマウントしているからです。

起動できたら下記のようにするとDockerが動きます。

### Dockerストレージ用マウントポイント作成

```
sudo mkfs.ext4 /dev/vdb
sudo mkdir /mnt/docker-data
echo '/dev/vdb /mnt/docker-data ext4 defaults 0 0' | sudo tee -a /etc/fstab
sudo mount /mnt/docker-data
```

### Dockerデーモンの設定ファイル作成

```
sudo mkdir /etc/docker
echo '{"data-root": "/mnt/docker-data","storage-driver": "overlay"}' | sudo tee /etc/docker/daemon.json
```

### Debianリポジトリ追加

```
configure
set system package repository jessie components 'main contrib non-free'
set system package repository jessie distribution jessie
set system package repository jessie url 'http://deb.debian.org/debian'
commit
save
```

### 必須パッケージインストール

```
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common
```

### Dockerインストール

```
set system package repository docker components stable
set system package repository docker distribution jessie
set system package repository docker url https://download.docker.com/linux/debian
commit
save
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
sudo apt update
sudo apt install -y docker-ce
```

### vyosユーザをdockerグループに追加

```
set system login user vyos group docker
commit
save
```

### 確認

```
docker info
docker run --rm hello-world
```

`docker info` の結果は下記のようになります。

```
vyos@vyos:~$ docker info
Containers: 0
 Running: 0
 Paused: 0
 Stopped: 0
Images: 1
Server Version: 17.12.1-ce
Storage Driver: overlay
 Backing Filesystem: extfs
 Supports d_type: true
Logging Driver: json-file
Cgroup Driver: cgroupfs
Plugins:
 Volume: local
 Network: bridge host macvlan null overlay
 Log: awslogs fluentd gcplogs gelf journald json-file logentries splunk syslog
Swarm: inactive
Runtimes: runc
Default Runtime: runc
Init Binary: docker-init
containerd version: 9b55aab90508bd389d7654c4baf173a981477d55
runc version: 9f9c96235cc97674e935002fc3d78361b696a69e
init version: 949e6fa
Kernel Version: 4.14.26-amd64-vyos
Operating System: Debian GNU/Linux 8 (jessie)
OSType: linux
Architecture: x86_64
CPUs: 1
Total Memory: 489.6MiB
Name: vyos
ID: RPQC:225S:FULT:3434:AASR:CASH:NS7I:OQ4K:AYA2:DQMG:AGFM:CB3I
Docker Root Dir: /mnt/docker-data
Debug Mode (client): false
Debug Mode (server): false
Registry: https://index.docker.io/v1/
Labels:
Experimental: false
Insecure Registries:
 127.0.0.0/8
Live Restore Enabled: false
```

### おまけ: Vagrantfile

Vagrantとlibvirtが使える人は下記のVagrantfileを使うとサッと試せます。
他の環境でもディスク追加部分を書き換えればいけるはずです。

[gist:id=af2be3de0c5861f2a9b36a7f4e71ffa8]
