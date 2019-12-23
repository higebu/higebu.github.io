---
title: VyOS で Docker を動かす
slug: docker-on-vyos
date: 2014-12-10T23:30:00Z
categories: 
- "Tech"
tags: 
- "vyos"
- "docker"
---


この記事は、 [VyOS Advent Calendar 2014][1] の10日目の記事です。

[TOC]

## 作り方

VyOS は AUFS が入っていないので、カーネルからビルドし直します。

普通に入れようとすると `FATAL: Module aufs not found.` と怒られます。

AUFS に対応させる手順は下記の通りです。

まず、 `vyos-kernel` を `git clone` します。

```
git clone git@github.com:vyos/vyos-kernel.git
```

ここで、 `vyos-kernel` に適当なブランチを作っておきます。

`aufs3-standalone` のソースを持ってきてパッチを当てます。

```
git clone git://aufs.git.sourceforge.net/gitroot/aufs/aufs3-standalone.git
pushd aufs3-standalone
git checkout origin/aufs3.13
popd
cp -r aufs3-standalone/{Documentation,fs} vyos-kernel
cp aufs3-standalone/include/uapi/linux/aufs_type.h vyos-kernel/include/uapi/linux/aufs_type.h
cd vyos-kernel
cat ../aufs3-standalone/aufs3-{base,kbuild,loopback,mmap,standalone}.patch | patch -p1
```

また、 cgroup のオプションが足りないので、足します。

AUFS を足しただけだと、下記のようになります。

```
vyos@vyos:~$ docker info
Containers: 0
Images: 7
Storage Driver: aufs
 Root Dir: /var/lib/docker/aufs
 Dirs: 7
Execution Driver: native-0.2
Kernel Version: 3.13.11-1-amd64-vyos
Operating System: <unknown>
WARNING: No memory limit support
WARNING: No swap limit support
```

config の diff は最終的に下記のようになりました。

```
# git diff HEAD^ debian/arch/amd64/config.amd64-vyos | cat -
diff --git a/debian/arch/amd64/config.amd64-vyos b/debian/arch/amd64/config.amd64-vyos
index 609abec..570c4a2 100644
--- a/debian/arch/amd64/config.amd64-vyos
+++ b/debian/arch/amd64/config.amd64-vyos
@@ -141,18 +141,26 @@ CONFIG_ARCH_WANTS_PROT_NUMA_PROT_NONE=y
 # CONFIG_NUMA_BALANCING is not set
 CONFIG_CGROUPS=y
 # CONFIG_CGROUP_DEBUG is not set
-# CONFIG_CGROUP_FREEZER is not set
-# CONFIG_CGROUP_DEVICE is not set
+CONFIG_CGROUP_FREEZER=y
+CONFIG_CGROUP_DEVICE=y
 CONFIG_CPUSETS=y
 CONFIG_PROC_PID_CPUSET=y
-# CONFIG_CGROUP_CPUACCT is not set
-# CONFIG_RESOURCE_COUNTERS is not set
-# CONFIG_CGROUP_PERF is not set
+CONFIG_CGROUP_CPUACCT=y
+CONFIG_RESOURCE_COUNTERS=y
+CONFIG_MEMCG=y
+CONFIG_MEMCG_SWAP=y
+CONFIG_MEMCG_SWAP_ENABLED=y
+CONFIG_CGROUP_MEM_RES_CTLR_SWAP=y
+CONFIG_CGROUP_MEM_RES_CTLR_SWAP_ENABLED=y
+CONFIG_MEMCG_KMEM=y
+CONFIG_CGROUP_HUGETLB=y
+CONFIG_CGROUP_PERF=y
 CONFIG_CGROUP_SCHED=y
 CONFIG_FAIR_GROUP_SCHED=y
-# CONFIG_CFS_BANDWIDTH is not set
-CONFIG_RT_GROUP_SCHED=y
-# CONFIG_BLK_CGROUP is not set
+CONFIG_CFS_BANDWIDTH=y
+# CONFIG_RT_GROUP_SCHED is not set
+CONFIG_BLK_CGROUP=y
+# CONFIG_DEBUG_BLK_CGROUP is not set
 # CONFIG_CHECKPOINT_RESTORE is not set
 CONFIG_NAMESPACES=y
 CONFIG_UTS_NS=y
@@ -273,6 +281,7 @@ CONFIG_BLOCK=y
 CONFIG_BLK_DEV_BSG=y
 CONFIG_BLK_DEV_BSGLIB=y
 CONFIG_BLK_DEV_INTEGRITY=y
+CONFIG_BLK_DEV_THROTTLING=y
 # CONFIG_BLK_CMDLINE_PARSER is not set
 
 #
@@ -307,6 +316,7 @@ CONFIG_BLOCK_COMPAT=y
 CONFIG_IOSCHED_NOOP=y
 CONFIG_IOSCHED_DEADLINE=y
 CONFIG_IOSCHED_CFQ=y
+CONFIG_CFQ_GROUP_IOSCHED=y
 # CONFIG_DEFAULT_DEADLINE is not set
 CONFIG_DEFAULT_CFQ=y
 # CONFIG_DEFAULT_NOOP is not set
@@ -4007,6 +4017,30 @@ CONFIG_CLKBLD_I8253=y
 # CONFIG_POWERCAP is not set
 
 #
+# AUFS Support
+#
+CONFIG_AUFS_FS=m
+CONFIG_AUFS_BRANCH_MAX_127=y
+# CONFIG_AUFS_BRANCH_MAX_511 is not set
+# CONFIG_AUFS_BRANCH_MAX_1023 is not set
+# CONFIG_AUFS_BRANCH_MAX_32767 is not set
+CONFIG_AUFS_SBILIST=y
+# CONFIG_AUFS_HNOTIFY is not set
+CONFIG_AUFS_EXPORT=y
+CONFIG_AUFS_XATTR=y
+# CONFIG_AUFS_FHSM is not set
+# CONFIG_AUFS_RDU is not set
+# CONFIG_AUFS_SHWH is not set
+CONFIG_AUFS_BR_RAMFS=y
+CONFIG_AUFS_BR_FUSE=y
+CONFIG_AUFS_BR_HFSPLUS=y
+# CONFIG_AUFS_DEBUG is not set
+# CONFIG_AUFS_MAGIC_SYSRQ is not set
+CONFIG_AUFS_BDEV_LOOP=y
+CONFIG_AUFS_INO_T_64=y
+CONFIG_AUFS_POLL=y
+
+#
 # Firmware Drivers
 #
 CONFIG_EDD=m
```

修正した `vyos-kernel` は [GitHub][2] に置いてあります。

ビルドの仕方は、昨日と同じで、シェルスクリプトにしてあって、 [gist][3] に置いてあります。

[hiroysato][4] さんの [Jessie 上で VyOS をビルドする手順][5]を参考に Wheezy でビルドしました。

興味のある方は読んでみてください。

## 使い方

ISO をダウンロードし、インストールします。

ビルド済みの ISO は [GitHub][6] に置いてあります。

起動して、`show version` すると下記のように表示されます。

```
vyos@vyos:~$ show version
Version:      VyOS 999.heliumdocker.12091651
Description:  999.heliumdocker.12091651
Copyright:    2014 VyOS maintainers and contributors
Built by:     root@contributors.vyos.net
Built on:     Tue Dec  9 16:51:21 UTC 2014
Build ID:     1412091651-cff5913
System type:  x86 64-bit
Boot via:     disk
Hypervisor:   VMware
HW model:     VMware Virtual Platform
HW S/N:       VMware-42 02 fc 13 49 8a c7 0f-e6 f2 dc 16 0c 81 91 12
HW UUID:      4202FC13-498A-C70F-E6F2-DC160C819112
Uptime:       15:29:54 up 3 min,  1 user,  load average: 0.01, 0.03, 0.02
```

Docker をインストールします。

```
configure
set system package repository squeeze url http://ftp.jp.debian.org/debian/
set system package repository squeeze distribution squeeze
set system package repository squeeze components 'main contrib non-free'
set system package repository squeeze-lts url http://ftp.jp.debian.org/debian/
set system package repository squeeze-lts distribution squeeze-lts
set system package repository squeeze-lts components 'main contrib non-free'
commit
save
exit
sudo apt-get update
curl -sSL https://get.docker.com/ | /bin/sh
```

vyos ユーザを docker グループに所属させます。

```
sudo usermod -aG docker vyos
```

ログアウト、ログインします。

`start-stop-daemon` が古く、 `--no-close` に対応していないので、 `/etc/init.d/docker` から消します。
```
sudo sed -i '/--no-close/d' /etc/init.d/docker
```

Docker を起動します。

```
sudo /etc/init.d/docker start
```

`docker info` を見てみます。

```
vyos@vyos:~$ docker info
Containers: 0
Images: 0
Storage Driver: aufs
 Root Dir: /var/lib/docker/aufs
 Dirs: 0
Execution Driver: native-0.2
Kernel Version: 3.13.11-1-amd64-vyos
Operating System: <unknown>
```

WARNING は出ていません！

Operating System が `<unknown>` ですが気にしないことにして、 VyOS の Docker イメージを起動してみます。

```
vyos@vyos:~$ docker run -d --privileged -v /lib/modules:/lib/modules -v /boot:/boot higebu/vyos:latest /sbin/init
01f328b0b8dbf763a1aada80e85980577146be377c4ea4d284583f02b8c44355
vyos@vyos:~$ docker ps -l
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
01f328b0b8db        higebu/vyos:1.1.1   "/sbin/init"        4 seconds ago       Up 3 seconds                            suspicious_morse
```

中に入ってみます。

```
vyos@vyos:~$ docker exec -ti suspicious_morse /bin/vbash
vbash-4.1# su - vyos
vyos@vyos:~$ show version
WARNING: terminal is not fully functional
Version:      VyOS 1.1.1
Description:  VyOS 1.1.1 (helium)
Copyright:    2014 VyOS maintainers and contributors
Built by:     maintainers@vyos.net
Built on:     Sun Dec  7 21:41:28 UTC 2014
Build ID:     1412072141-129950d
System type:  x86 64-bit
Boot via:     disk
Hypervisor:   VMware
HW model:     VMware Virtual Platform
HW S/N:       VMware-42 02 fc 13 49 8a c7 0f-e6 f2 dc 16 0c 81 91 12
HW UUID:      4202FC13-498A-C70F-E6F2-DC160C819112
Uptime:       06:47:14 up 21 min,  0 users,  load average: 0.03, 0.05, 0.05
```

一応動いていますね。

しかし、 VyOS の Docker イメージがおかしいようで、 IP アドレスが付きません。

```
vbash-4.1# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default 
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
6: eth0: <BROADCAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 02:42:ac:11:00:03 brd ff:ff:ff:ff:ff:ff
    inet6 fe80::42:acff:fe11:3/64 scope link 
       valid_lft forever preferred_lft forever
```

下記のように `debian:latest` のイメージを取ってきて動かすと IP アドレスが付いているので、 VyOS 上で Docker を動かすという部分については、今のところ問題ないと思っています。

```
vyos@vyos:~$ docker run -it debian:latest /bin/bash
Unable to find image 'debian:latest' locally
debian:latest: The image you are pulling has been verified
511136ea3c5a: Pull complete 
f10807909bc5: Pull complete 
f6fab3b798be: Pull complete 
Status: Downloaded newer image for debian:latest
root@2e86576d3b90:/# 
root@2e86576d3b90:/# 
root@2e86576d3b90:/# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN 
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
4: eth0: <BROADCAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP qlen 1000
    link/ether 02:42:ac:11:00:02 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.2/16 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:acff:fe11:2/64 scope link 
       valid_lft forever preferred_lft forever
```

VyOS の Docker イメージを直すことができたら、またブログに書きたいと思います。

以上です。

 [1]: http://qiita.com/advent-calendar/2014/vyos
 [2]: https://github.com/higebu/vyos-kernel/tree/helium-docker
 [3]: https://gist.github.com/higebu/409c00db4aa1256e405b
 [4]: https://twitter.com/hiroysato
 [5]: https://gist.github.com/hiroyuki-sato/201032fe75d2cf9f5801
 [6]: https://github.com/higebu/build-iso/releases/download/vyos%2F1.1.1-docker/VyOS-livecd-1412091651-cff5913-amd64.iso
