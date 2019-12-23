---
title: eAcceleratorを有効にしているとphpmyadminが動かない
slug: phpmyadmin-does-not-work-with-eaccelerator
date: 2012-05-07T00:00:00+09:00
aliases:
- archives/389
categories: 
- "Tech"
tags: 
- "php"
- " wordpress"
- " eaccelerator"
- " phpmyadmin"
---

小ネタ

WordPressを移行するときにphpmyadmin使おうとしたら動かなくて、諦めてmysqldumpしたんだけど後から調べたら解決したのでメモ

環境

* Ubuntu 11.10
* PHP 5.3.6-13ubuntu3.6
* phpmyadmin 3.4.5deb1
* MySQL 5.1.58

現象

phpmyadminにアクセスすると以下のようなエラーが出る（画面上は500だったと思う）

/var/log/apache2/error.log

```
[Fri May 04 15:53:57 2012] [error] [client xxx.xxx.xxx.xxx] PHP Warning: Unknown: open_basedir restriction in effect. File() is not within the allowed path(s): (/usr/share/phpmyadmin/:/etc/phpmyadmin/:/var/lib/phpmyadmin/) in Unknown on line 0, referer: http://yyy.yyy.yyy.yyy/phpmyadmin/
[Fri May 04 15:53:57 2012] [error] [client xxx.xxx.xxx.xxx] PHP Warning: require(): open_basedir restriction in effect. File() is not within the allowed path(s): (/usr/share/phpmyadmin/:/etc/phpmyadmin/:/var/lib/phpmyadmin/) in /usr/share/phpmyadmin/libraries/common.inc.php on line 52, referer: http://yyy.yyy.yyy.yyy/phpmyadmin/
[Fri May 04 15:53:57 2012] [error] [client xxx.xxx.xxx.xxx] PHP Fatal error: Call to undefined function PMA_sanitize() in /usr/share/phpmyadmin/libraries/Message.class.php on line 601, referer: http://yyy.yyy.yyy.yyy/phpmyadmin/
```

解決方法

/etc/apache2/conf.d/phpmyadmin.conf に以下を追記する

```
<Directory /usr/share/phpmyadmin>
    php_admin_value eaccelerator.enable 0
</Directory>
```

でapache再起動すると動くようになる
