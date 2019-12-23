---
title: VyOS のインストールとアップグレード
slug: how-to-install-and-upgrade-vyos
date: 2014-12-02T23:30:00Z
categories: 
- "Tech"
tags: 
- "vyos"
---


この記事は、 [VyOS Advent Calendar 2014][1] の2日目の記事です。

[TOC]

今回は、インストールとアップグレードについて説明します。

使用するバージョンは、現在の最新の安定版である、 1.1.0 です。

# インストール

まず、 ISO イメージをダウンロードします。

[本家のミラー][2]か、[日本のミラー][3]からダウンロードします。

ダウンロードした ISO を実際のマシンでも仮想マシンでも良いのでマウントして起動します。

起動すると以下のような画面になるのでログインします。

![vyos](/images/vyos1-2014-12-02-22-43-58.png)
ブート画面にも書いてありますが、 ID とパスワードは共に vyos です。

インストールコマンドは `install system` と `install image` がありますが、推奨の `install image` を使います。

インストールの流れは下記の通りです。

パーティションを自分で設定したいとき以外は、大きな変更はないと思います。

```
vyos@vyos:~$ install image 
Welcome to the VyOS install program.  This script
will walk you through the process of installing the
VyOS image to a local hard drive.
Would you like to continue? (Yes/No) [Yes]: Yes
Probing drives: OK
Looking for pre-existing RAID groups...none found.
The VyOS image will require a minimum 1000MB root.
Would you like me to try to partition a drive automatically
or would you rather partition it manually with parted?  If
you have already setup your partitions, you may skip this step

Partition (Auto/Parted/Skip) [Auto]:   

I found the following drives on your system:
 sda	8589MB


Install the image on? [sda]:

This will destroy all data on /dev/sda.
Continue? (Yes/No) [No]: Yes

How big of a root partition should I create? (1000MB - 8589MB) [8589]MB: 

Creating filesystem on /dev/sda1: OK
Done!
Mounting /dev/sda1...
What would you like to name this image? [1.1.0]: 
OK.  This image will be named: 1.1.0
Copying squashfs image...
Copying kernel and initrd images...
Done!
I found the following configuration files:
    /config/config.boot
    /opt/vyatta/etc/config.boot.default
Which one should I copy to sda? [/config/config.boot]: 

Copying /config/config.boot to sda.
Enter password for administrator account
Enter password for user 'vyos':
Retype password for user 'vyos':
I need to install the GRUB boot loader.
I found the following drives on your system:
 sda	8589MB


Which drive should GRUB modify the boot partition on? [sda]:

Setting up grub: OK
Done!
```

インストールが終わったら再起動します。

```
vyos@vyos:~$ reboot
Proceed with reboot? (Yes/No) [No] Yes
```

バージョンを確認します。

```
vyos@vyos:~$ show version 
Version:      VyOS 1.1.0
Description:  VyOS 1.1.0 (helium)
Copyright:    2014 VyOS maintainers and contributors
Built by:     maintainers@vyos.net
Built on:     Thu Oct  9 22:27:26 UTC 2014
Build ID:     1410092227-af6433f
System type:  x86 64-bit
Boot via:     image
Hypervisor:   VMware
HW model:     VMware Virtual Platform
HW S/N:       VMware-56 4d 8c 89 9f 3f 1e 76-e3 89 53 a5 85 f5 46 fc
HW UUID:      564D8C89-9F3F-1E76-E389-53A585F546FC
Uptime:       13:54:20 up 0 min,  1 user,  load average: 0.37, 0.11, 0.04
```

今回は、 VMware Workstation 上でインストールしたため、 HW model が VMware Virtual Platform になっていますが、他の環境では異なる文字列になっています。

インストールについて、詳しくは、[公式のドキュメント][4]か[日本語訳][5]をご参照ください。

# アップグレード

次に先ほどインストールしたものから、 1.1.1 rc1 にアップグレードします。

アップグレードについては[公式のドキュメント][6]に書いてあります。

日本語訳はまだありません。。。

アップグレードの流れは下記の通りです。

`add system image` コマンドの引数に ISO イメージの URL を渡します。

イメージの名前は好きなものを指定できますが、ここでは、そのままにしています。

```
vyos@vyos:~$ add system image http://dev.packages.vyos.net/iso/helium/amd64/VyOS-livecd-1412020000-af6433f-amd64.iso
Trying to fetch ISO file from http://dev.packages.vyos.net/iso/helium/amd64/VyOS-livecd-1412020000-af6433f-amd64.iso
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  231M  100  231M    0     0  1922k      0  0:02:03  0:02:03 --:--:-- 2568k
ISO download succeeded.
Checking for digital signature file...
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
curl: (22) The requested URL returned error: 404
Unable to fetch digital signature file.
Do you want to continue without signature check? (yes/no) [yes]    
Checking MD5 checksums of files on the ISO image...OK.
Done!
What would you like to name this image? [VyOS-999.helium.12020000]: 
OK.  This image will be named: VyOS-999.helium.12020000
Installing "VyOS-999.helium.12020000" image.
Copying new release files...
Would you like to save the current configuration 
directory and config file? (Yes/No) [Yes]: 
Copying current configuration...
Would you like to save the SSH host keys from your 
current configuration? (Yes/No) [Yes]: 
Copying SSH keys...
Setting up grub configuration...
Done.
```

インストールされたイメージを確認します。

```
vyos@vyos:~$ show system image
The system currently has the following image(s) installed:

   1: VyOS-999.helium.12020000 (default boot)
   2: 1.1.0
```

この状態ではまだアップグレードされていないので、 `reboot` で再起動します。

再起動後、 show version するとバージョンアップされているのを確認できます。

```
vyos@vyos:~$ show version
Version:      VyOS 999.helium.12020000
Description:  999.helium.12020000
Copyright:    2014 VyOS maintainers and contributors
Built by:     autobuild@vyos.net
Built on:     Tue Dec  2 00:00:38 UTC 2014
Build ID:     1412020000-af6433f
System type:  x86 64-bit
Boot via:     image
Hypervisor:   VMware
HW model:     VMware Virtual Platform
HW S/N:       VMware-56 4d 8c 89 9f 3f 1e 76-e3 89 53 a5 85 f5 46 fc
HW UUID:      564D8C89-9F3F-1E76-E389-53A585F546FC
Uptime:       14:15:36 up 0 min,  1 user,  load average: 0.29, 0.08, 0.03
```

では、前のバージョンに戻してみましょう。

`set system image default-boot` コマンドを使います。

```
vyos@vyos:~$ set system image default-boot 1.1.0
Default boot image has been set to "1.1.0".
You need to reboot the system to start the new default image.
```

もう一度再起動するとバージョンが戻っているのを確認できます。

```
vyos@vyos:~$ show version
Version:      VyOS 1.1.0
Description:  VyOS 1.1.0 (helium)
Copyright:    2014 VyOS maintainers and contributors
Built by:     maintainers@vyos.net
Built on:     Thu Oct  9 22:27:26 UTC 2014
Build ID:     1410092227-af6433f
System type:  x86 64-bit
Boot via:     image
Hypervisor:   VMware
HW model:     VMware Virtual Platform
HW S/N:       VMware-56 4d 8c 89 9f 3f 1e 76-e3 89 53 a5 85 f5 46 fc
HW UUID:      564D8C89-9F3F-1E76-E389-53A585F546FC
Uptime:       14:19:10 up 0 min,  1 user,  load average: 0.04, 0.01, 0.01
```

新しいバージョンが出たときに今の設定がそのまま動くか試すときにとても便利です。

簡単にできますので、ぜひ試してみてください。


 [1]: http://qiita.com/advent-calendar/2014/vyos
 [2]: http://mirror.vyos.net/iso/release/1.1.0/vyos-1.1.0-amd64.iso
 [3]: http://ftp.tsukuba.wide.ad.jp/software/vyos/iso/release/1.1.0/vyos-1.1.0-amd64.iso
 [4]: http://vyos.net/wiki/User_Guide#Installation
 [5]: http://wiki.vyos-users.jp/%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC%E3%82%AC%E3%82%A4%E3%83%89#.E3.82.A4.E3.83.B3.E3.82.B9.E3.83.88.E3.83.BC.E3.83.AB
 [6]: http://vyos.net/wiki/Upgrade
