---
title: Ubuntuにapt-getでVMware Toolsをインストールする
slug: install-vmware-tools-to-ubuntu-with-apt-get
date: 2013-07-07T00:00:00+09:00
aliases:
- archives/648
categories: 
- "Tech"
tags: 
- "vmware"
- "vmware-tools"
- "apt"
- "ubuntu"
---

ESXi5.0上のUbuntu12.04にapt-getでVMware Toolsをインストールする手順です。

``` bash
wget http://packages.vmware.com/tools/keys/VMWARE-PACKAGING-GPG-RSA-KEY.pub -q -O- | sudo apt-key add -
echo 'deb http://packages.vmware.com/tools/esx/5.0latest/ubuntu precise main' | sudo tee /etc/apt/sources.list.d/vmware-tools.list
sudo apt-get update
sudo apt-get install vmware-tools-esx-kmods-3.2.0-29-generic
sudo apt-get install vmware-tools-esx-nox
```

ESXi5.1の場合は、5.0latestの部分を5.1latestにしてください。

最新の12.04のカーネルのバージョンは3.5.0-36ですが、2013/7/7現在、リポジトリには3.2.0-29までしかありませんので、
3.5.0-36にしてから入れたらいろいろとおかしくなるかもしれません。

また、 http://packages.vmware.com/tools/esx/5.0latest/ubuntu/dists/ 配下にpresiceまでしかないため、12.10以降のパッケージはないようです。

対応が中途半端ですね。

詳細は下記のページで

http://www.vmware.com/download/packages.html
