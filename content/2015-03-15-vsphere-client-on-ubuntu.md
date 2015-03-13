Title: vSphere Client 5.5 on Ubuntu 14.04
Slug: vsphere-client-on-ubuntu
Date: 2015-03-15 12:30
Category: Tech
Tags: vmware, vsphere client, vsphere, wine, ubuntu, mono
Summary: wine を使って vSphere Client 5.5 を Ubuntu 14.04 上で動かす方法です。

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

{% img /images/20150315-vsphere-client.png 1073 662 "Screen Shot" "Screen Shot" %} 
