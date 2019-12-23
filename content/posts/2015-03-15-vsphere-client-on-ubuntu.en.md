---
title: vSphere Client 5.5 on Ubuntu 14.04
slug: vsphere-client-on-ubuntu
date: 2015-03-15T12:30:00Z
categories: 
- "Tech"
tags: 
- "vmware"
- "vsphere client"
- "vsphere"
- "wine"
- "ubuntu"
- "mono"
---

## Versions

* Ubuntu 14.04.2 amd64
* wine 1.7.38
* mono 4.5.4

## Install Wine and .NET

* Run following commands:

```shell
sudo add-apt-repository ppa:ubuntu-wine/ppa
sudo apt-get update
sudo apt-get install -y wine1.7 wine-mono4.5.4 wine-gecko2.34
```

* Confirm Wine version

```shell
$ wine --version
wine-1.7.38
```

* Set up 32bit Wine

```shell
WINEARCH=win32 WINEPREFIX=~/.wine32 winecfg
```

* Install .NET

```shell
WINEARCH=win32 WINEPREFIX=~/.wine32 winetricks dotnet20
WINEARCH=win32 WINEPREFIX=~/.wine32 winetricks dotnet30
WINEARCH=win32 WINEPREFIX=~/.wine32 winetricks dotnet20sp1
WINEARCH=win32 WINEPREFIX=~/.wine32 winetricks dotnet30sp1
WINEARCH=win32 WINEPREFIX=~/.wine32 winetricks dotnet35
WINEARCH=win32 WINEPREFIX=~/.wine32 winetricks dotnet35sp1
```

If the above commands exits with error, and shows a download url. Download the file and put into specified directory.

## Install vSphere Client

* Download vSphere Client Installer, and run following command:

```shell
WINEARCH=win32 WINEPREFIX=~/.wine32 wine Downloads/VMware-viclient-all-5.5.0-1993072.exe
```

## Run vSphere Client

Run following command:

```shell
WINEARCH=win32 WINEPREFIX=$HOME/.wine32 wine $HOME/.wine32/drive_c/Program\ Files/VMware/Infrastructure/Virtual\ Infrastructure\ Client/Launcher/VpxClient.exe
```

Or double click the shortcut on your desktop.

![vsphere-client](/images/20150315-vsphere-client.png)
Console doesn't work now. If you want to use console, you should use VMware Workstation or VNC.

## References

* [Wine](https://www.winehq.org/)
* [How to install vSphere Client 5.5 on Mac OSX using Wine](http://atmosphere147.blogspot.jp/2014/05/how-to-install-vsphere-client-55-on-mac.html)
