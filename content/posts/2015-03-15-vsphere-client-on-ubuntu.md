---
title: vSphere Client 5.5 on Ubuntu 14.04
slug: vsphere-client-on-ubuntu
date: 2015-03-15T12:30:00Z
categories: 
- "Tech"
tags: 
- "vmware"
- " vsphere client"
- " vsphere"
- " wine"
- " ubuntu"
- " mono"
---


[TOC]

## 環境

* Ubuntu 14.04.2 amd64
* wine 1.7.38
* mono 4.5.4

## wine と .NET のインストール

* 下記のコマンドを実行

```
sudo add-apt-repository ppa:ubuntu-wine/ppa
sudo apt-get update
sudo apt-get install -y wine1.7 wine-mono4.5.4 wine-gecko2.34
```

* wine のバージョンの確認

```
$ wine --version
wine-1.7.38
```

* 32bit 環境の用意

```
WINEARCH=win32 WINEPREFIX=~/.wine32 winecfg
```

* XP になっているので、Windows7などにしておく

* .NET インストール

```
WINEARCH=win32 WINEPREFIX=~/.wine32 winetricks dotnet20
WINEARCH=win32 WINEPREFIX=~/.wine32 winetricks dotnet30
WINEARCH=win32 WINEPREFIX=~/.wine32 winetricks dotnet20sp1
WINEARCH=win32 WINEPREFIX=~/.wine32 winetricks dotnet30sp1
WINEARCH=win32 WINEPREFIX=~/.wine32 winetricks dotnet35
WINEARCH=win32 WINEPREFIX=~/.wine32 winetricks dotnet35sp1
```

途中でダウンロードして指定されたディレクトリに置けと言われるので、その通りにする。ディレクトリもダウンロード先のサイトも勝手に開くのでそこまで大変でもないです。

## vSphere Client インストール

* vSphere Client のインストーラをダウンロードして、下記のコマンドを実行

```
WINEARCH=win32 WINEPREFIX=~/.wine32 wine Downloads/VMware-viclient-all-5.5.0-1993072.exe
```

## vSphere Client 起動

* 下記のコマンドを実行する

```
WINEARCH=win32 WINEPREFIX=$HOME/.wine32 wine $HOME/.wine32/drive_c/Program\ Files/VMware/Infrastructure/Virtual\ Infrastructure\ Client/Launcher/VpxClient.exe
```

下記の画像のようになります。デスクトップにショートカットもできていて、これをダブルクリックでも起動できます。便利な世の中になりましたね。

![vsphere-client](/images/20150315-vsphere-client.png)
ただ、現状ではコンソールが使えません。コンソールを見たいときは VMware Workstation を使うか、 VNC で接続することになります。

## 参考

* [Wine](https://www.winehq.org/)
* [How to install vSphere Client 5.5 on Mac OSX using Wine](http://atmosphere147.blogspot.jp/2014/05/how-to-install-vsphere-client-55-on-mac.html)
