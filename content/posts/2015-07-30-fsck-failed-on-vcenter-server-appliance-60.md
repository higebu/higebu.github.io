---
title: vCenter Server Appliance 6.0 fsck failed
slug: vcenter-server-appliance-60-fsck-failed
date: 2015-07-30T15:30:00Z
categories: 
- "Tech"
tags: 
- "vmware"
- " vCenter Server Appliance"
- " vCSA"
- " fsck"
---


[TOC]

![Shot"](/images/20150730-vcenter-server-appliance-60-fsck-failed.png)
検証環境の vCSA 6.0 が突然落ちて、コンソールを見たら画像のようになっていたので、直した話です。

## 環境

* vCenter Server Appliance 6.0.0
* Platform Services Controller は別に立てている

## 事象

画像のように `/dev/mapper/db_vg-db` の `fsck` に失敗したというエラーがコンソールに表示されます。

## 復旧方法

本来であれば、先ほどの画面でパスワードを2回入力した後、下記のコマンドを実行するとシェルにログインできます。

```
shell.set --enabled true
shell
```

しかし、今回は `shell.set` もエラーになってしまったため、 [KB2069041](http://kb.vmware.com/kb/2069041) の手順でシェルにログインしました。

以下、復旧手順です。

まず、 `pvscan`, `vgscan`, `lvscan` 辺りのコマンドを実行し、状態を確認します。

`pvscan` の実行結果は下記のようになるはずです。 `pvscan` でデバイスがないとか何かエラーが出ていたら今回の手順では復旧できないと思います。

```
Failed to find sysfs mont point
  PV /dev/sdk   VG invsvc_vg       lvm2 [9.99 GiB / 0    free]
  PV /dev/sdj   VG autodeploy_vg   lvm2 [9.99 GiB / 0    free]
  PV /dev/sdi   VG netdump_vg      lvm2 [1016.00 MiB / 0    free]
  PV /dev/sdh   VG seat_vg         lvm2 [24.99 GiB / 0    free]
  PV /dev/sdg   VG dblog_vg        lvm2 [4.99 GiB / 0    free]
  PV /dev/sdf   VG db_vg           lvm2 [9.99 GiB / 0    free]
  PV /dev/sde   VG log_vg          lvm2 [9.99 GiB / 0    free]
  PV /dev/sdd   VG core_vg         lvm2 [49.99 GiB / 0    free]
  PV /dev/sdc   VG swap_vg         lvm2 [24.99 GiB / 0    free]
  Total: 9 [145.93 GiB] / in use: 9 [145.93 GiB] / in no VG: 0 [0   ]
```

`db_vg` を active にします。

```
lvchange -ay db_vg
```

`e2fsck` を実行します。

```
e2fsck -y /dev/mapper/db_vg-db
```

`/dev/mapper/db_vg-db` がないと言われたら `vgcfgrestore db_vg` したら良いかもしれません。

この後、vCSA で Inventory Service が起動しない状態になっており、ログを見たところ、 ldap 関連のエラーが出ていたため、 Platform Services Controller を再起動して、 vCSA も再起動したら元の状態に戻りました。

本番環境では起きて欲しくない障害ですね。。。

## 参考

* [vCenter Appliance fsck failed](http://www.virtualizationteam.com/server-virtualization/vcenter-appliance-fsck-failed.html)
	* 5.5 で root fs の `fsck` をする話
* [fsck of vCenter Server Appliance 6.0 partitions](http://cormachogan.com/2015/06/03/fsck-of-vcenter-server-appliance-6-0-partitions/)
	* ほとんど同じ内容
	* この記事では `lvchange` していないが、しないと `/dev/mapper` ディレクトリが出現しなかった
* [Recovery of LVM partitions](http://www.softpanorama.org/Commercial_linuxes/LVM/recovery_of_lvm_partitions.shtml)
* [Recovering a Lost LVM Volume Disk](http://www.novell.com/coolsolutions/appnote/19386.html)
* [How to properly run fsck on (/) root or other partitions including LVM](https://unixbhaskar.wordpress.com/2010/08/16/how-to-properly-run-fsck-on-root-or-other-partitions-including-lvm/)
