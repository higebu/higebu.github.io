Title: VyOS の OpenSSL パッケージをアップデートする
Date: 2014-06-09 12:50:00
Tags: vyos,vyatta,openssl,debian
Category: tech
Slug: upgrade-openssl-package-on-vyos
Authors: higebu
Summary: OpenSSL の脆弱性対策のため、 VyOS の OpenSSL パッケージをアップデートします。

CVE-2014-0224 などの OpenSSL の脆弱性対策のため、 VyOS では次のメンテナンスリリース（1.0.4）で、 OpenSSL のパッケージをアップデートするようです。
(http://vyos-dev.tumblr.com/post/88142058983/openssl-vulnerabilities)

ただ、上記の記事にも書いてありますが、緊急で対応したい場合、 OpenSSL のパッケージを自分でアップデートしなければならないので、そのやり方だけ書いておきます。

以下、手順です。

* リポジトリを追加

```bash
vyos@vyos# configure
vyos@vyos# set system package repository squeeze-lts url http://ftp.jp.debian.org/debian/
vyos@vyos# set system package repository squeeze-lts distribution squeeze-lts
vyos@vyos# set system package repository squeeze-lts components 'main contrib non-free'
vyos@vyos# commit
vyos@vyos# save
```

* インストール

```bash
vyos@vyos# sudo apt-get upgrade openssl
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages will be upgraded:
  libgnutls26 libssl0.9.8 openssl
3 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
Need to get 2639 kB of archives.
After this operation, 123 kB of additional disk space will be used.
Do you want to continue [Y/n]? Y
Get:1 http://ftp.jp.debian.org/debian/ squeeze-lts/main libssl0.9.8 amd64 0.9.8o-4squeeze15 [1004 kB]
Get:2 http://ftp.jp.debian.org/debian/ squeeze-lts/main libgnutls26 amd64 2.8.6-1+squeeze4 [573 kB]
Get:3 http://ftp.jp.debian.org/debian/ squeeze-lts/main openssl amd64 0.9.8o-4squeeze15 [1062 kB]
Fetched 2639 kB in 6s (425 kB/s)                                          
Preconfiguring packages ...
(Reading database ... 36818 files and directories currently installed.)
Preparing to replace libssl0.9.8 0.9.8o-4squeeze14 (using .../libssl0.9.8_0.9.8o-4squeeze15_amd64.deb) ...
Unpacking replacement libssl0.9.8 ...
Preparing to replace libgnutls26 2.8.6-1+squeeze2 (using .../libgnutls26_2.8.6-1+squeeze4_amd64.deb) ...
Unpacking replacement libgnutls26 ...
Preparing to replace openssl 0.9.8o-4squeeze14 (using .../openssl_0.9.8o-4squeeze15_amd64.deb) ...
Unpacking replacement openssl ...
Processing triggers for man-db ...
Setting up libssl0.9.8 (0.9.8o-4squeeze15) ...
Setting up libgnutls26 (2.8.6-1+squeeze4) ...
Setting up openssl (0.9.8o-4squeeze15) ...
```

* 確認
* openssl

```
dpkg -s openssl
Package: openssl
Status: install ok installed
Priority: optional
Section: utils
Installed-Size: 2368
Maintainer: Debian OpenSSL Team <pkg-openssl-devel@lists.alioth.debian.org>
Architecture: amd64
Version: 0.9.8o-4squeeze15
Depends: libc6 (>= 2.7), libssl0.9.8 (>= 0.9.8m-1), zlib1g (>= 1:1.1.4)
Suggests: ca-certificates
Conflicts: ssleay (<< 0.9.2b)
Conffiles:
 /etc/ssl/openssl.cnf 0b1cf9a835b829131d630b7c2fe55f3c
Description: Secure Socket Layer (SSL) binary and related cryptographic tools
 This package contains the openssl binary and related tools.
 .
 It is part of the OpenSSL implementation of SSL.
 .
 You need it to perform certain cryptographic actions like:
  -  Creation of RSA, DH and DSA key parameters;
  -  Creation of X.509 certificates, CSRs and CRLs;
  -  Calculation of message digests;
  -  Encryption and decryption with ciphers;
  -  SSL/TLS client and server tests;
  -  Handling of S/MIME signed or encrypted mail.
```

* libssl

```
dpkg -s libssl0.9.8
Package: libssl0.9.8
Status: install ok installed
Priority: important
Section: libs
Installed-Size: 2424
Maintainer: Debian OpenSSL Team <pkg-openssl-devel@lists.alioth.debian.org>
Architecture: amd64
Source: openssl
Version: 0.9.8o-4squeeze15
Depends: libc6 (>= 2.7), zlib1g (>= 1:1.1.4), debconf (>= 0.5) | debconf-2.0
Conflicts: libssl, libssl096-dev (<< 0.9.6-2), openssl (<< 0.9.6-2), ssleay (<< 0.9.2b)
Description: SSL shared libraries
 libssl and libcrypto shared libraries needed by programs like
 apache-ssl, telnet-ssl and openssh.
 .
 It is part of the OpenSSL implementation of SSL.
```
