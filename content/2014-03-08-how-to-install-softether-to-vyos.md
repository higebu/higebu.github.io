Title: VyOS に SoftEther VPN Server をインストール
Date: 2014-03-08 23:49:20
Tags: vyos,vyatta,softether
Category: tech
Slug: how-to-install-softether-vpn-server-to-vyos
Authors: higebu
Summary: VyOS に SoftEther VPN Server をインストールする手順

[VyOS][1] は [Vyatta][2] からフォークしたOSSのネットワークOSです。

VyOS 1.0.2 に SoftEther VPN Server をインストールしてみます。

SoftEther VPN Server のバージョンは v4.05-9423-beta-2014.02.18 です。

VyOS のインストールは ISO をダウンロードしたら、マウントして`install system`を実行するだけなので省略します。

以下、手順です。

VyOS に Debian のリポジトリを追加
---------------------------------

```bash
set system package repository squeeze components 'main'
set system package repository squeeze distribution 'squeeze'
set system package repository squeeze url 'http://ftp.jp.debian.org/debian/'
commit
save
sudo aptitude update
```

build-essential インストール
----------------------------

```
sudo aptitude -y install build-essential
```

SoftEther VPN Server インストール
---------------------------------

```bash
wget http://jp.softether-download.com/files/softether/v4.05-9423-beta-2014.02.18-tree/Linux/SoftEther%20VPN%20Server/64bit%20-%20Intel%20x64%20or%20AMD64/softether-vpnserver-v4.05-9423-beta-2014.02.18-linux-x64-64bit.tar.gz
tar xf softether-vpnserver-v4.05-9423-beta-2014.02.18-linux-x64-64bit.tar.gz
cd vpnserver
make
# ここで、質問には全て 1 と回答します。
sudo mv vpnserver /usr/local
sudo chown -R root:staff /usr/local/vpnserver
sudo chmod 600 /usr/local/vpnserver/*
sudo chmod 700 /usr/local/vpnserver/vpncmd
sudo chmod 700 /usr/local/vpnserver/vpnserver
```

確認
----

* vpncmd コマンドを実行し、 VPN Tools を選択
* check コマンドの実行結果が下記のようになっていればインストール成功です

```bash
vyos@vyos:~$ sudo /usr/local/vpnserver/vpncmd
vpncmd command - SoftEther VPN Command Line Management Utility
SoftEther VPN Command Line Management Utility (vpncmd command)
Version 4.05 Build 9423   (English)
Compiled 2014/02/18 19:33:00 by yagi at pc25
Copyright (c) SoftEther VPN Project. All Rights Reserved.

By using vpncmd program, the following can be achieved. 

1. Management of VPN Server or VPN Bridge 
2. Management of VPN Client
3. Use of VPN Tools (certificate creation and Network Traffic Speed Test Tool)

Select 1, 2 or 3: 3

VPN Tools has been launched. By inputting HELP, you can view a list of the commands that can be used.

VPN Tools>check
Check command - Check whether SoftEther VPN Operation is Possible
---------------------------------------------------
SoftEther VPN Operation Environment Check Tool

Copyright (c) SoftEther VPN Project.
All Rights Reserved.

If this operation environment check tool is run on a system and that system passes, it is most likely that SoftEther VPN software can operate on that system. This check may take a while. Please wait...

Checking 'Kernel System'... 
              Pass
Checking 'Memory Operation System'... 
              Pass
Checking 'ANSI / Unicode string processing system'... 
              Pass
Checking 'File system'... 
              Pass
Checking 'Thread processing system'... 
              Pass
Checking 'Network system'... 
              Pass

All checks passed. It is most likely that SoftEther VPN Server / Bridge can operate normally on this system.

The command completed successfully.
```

以上です。

これで、VyOS で SoftEther の VPN も利用可能になります。

あとは、 VyOS の set コマンドで SoftEther の設定を行えるようにすると便利そうです。

追記: init スクリプト
---------------------

Debian用のものを作ったので、Gistにおいておきました。

[gist:id=9460194]

 [1]: http://vyos.net/wiki/Main_Page
 [2]: https://ja.softether.org/
