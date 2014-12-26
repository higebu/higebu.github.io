Title: VyattaにVMware Tools入れる
Slug: install-vmware-tools-to-vyatta
URL: archives/393
save_as: archives/393/index.html
Author: higebu
Category: Tech
Tags: vmware, vmware-tools, vyatta

ただ入れるだけだと、VMware ToolsがONにならなかったり、IPが取れなかったりいろいろ不安定になるのですが、gccとかがないのが原因らしい。

というわけで、入れた手順。

バージョンはVyatta Core 6.3とESXi5.0です。
※追記
Vyatta Core 6.4やESXi4.1でもいけた

open-vm-toolsはいらないので消す（これと競合してたかもしれない）

```
## 6.3
sudo aptitude remove open-vm-tools open-vm-modules-2.6.37-1-amd64-vyatta-virt
## 6.4
sudo aptitude remove open-vm-tools open-vm-modules-3.0.23-1-amd64-vyatta-virt
```

Debianのリポジトリを追加する

```
configure
set system package repository squeeze components 'main contrib non-free'
set system package repository squeeze distribution 'squeeze'
set system package repository squeeze url 'http://ftp.jp.debian.org/debian/'
set system package repository squeeze username ''
set system package repository squeeze password ''
set system package repository squeeze/updates components 'main'
set system package repository squeeze/updates distribution 'squeeze/updates'
set system package repository squeeze/updates username ''
set system package repository squeeze/updates password ''
set system package repository squeeze/updates url 'http://security.debian.org/'
commit
save
```

gccとか入れる

```
sudo aptitude update
sudo aptitude install build-essential dh-make debhelper devscripts
```

VMware Toolsを入れる

```
mount /dev/cdrom /mnt
cp -p /mnt/VMwareTools-8.6.5-621624.tar.gz .
tar zxvf VMwareTools-8.6.5-621624.tar.gz
cd vmware-tools-distrib
sudo ./vmware-install.pl -d
```

これでまともに動くようになった。

ちゃんとDebian化させるにはlinux-headersも入れるべきなのかな。

6.4だとDebian squeezeとカーネルのバージョンが違うのが気になる。
