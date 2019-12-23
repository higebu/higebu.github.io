---
title: Zabbix Java GatewayでDouble型の値を監視できるようにするパッチ
slug: fix-zabbix-jmx-double-type-value-monitoring
date: 2013-03-17T00:00:00+09:00
aliases:
- /archives/608
categories: 
- "Tech"
tags: 
- "zabbix"
- "cassandra"
- "java"
- "jmx"
- "patch"
---

Zabbix Java Gatewayを使ってJMX経由で何かしらの値を監視するときに、値の型がjava.lang.Doubleだとエラーになってしまい、監視できない。

そこで、エラーにならないように修正する。

元ネタは下記のフォーラムのコメント。

[jmx java.lang.Double bug?](https://www.zabbix.com/forum/showthread.php?t=26452 "jmx java.lang.Double bug?")

Zabbix 2.0.4のときに作ったけど、たぶん2.0.5でも動くはず。

パッチは下記の通りです。

<script src="https://gist.github.com/higebu/5083311.js"></script>

パッチの当て方

1. Zabbixのソースをダウンロード

[http://www.zabbix.com/download.php](http://www.zabbix.com/download.php "http://www.zabbix.com/download.php")

2. 解凍

```
tar zxvf zabbix-2.0.4.tar.gz
cd zabbix-2.0.4/src/zabbix_java/
```

3. パッチを当てる

```
patch src/com/zabbix/gateway/JMXItemChecker.java zabbix2.0.4_jmx_double_type.patch
```

4. コンパイル

```
mkdir -p class/src
mkdir -p class/tests
javac -d class/src -classpath lib/org-json-2010-12-28.jar:lib/logback-core-0.9.27.jar:lib/logback-classic-0.9.27.jar:lib/slf4j-api-1.6.1.jar src/com/zabbix/gateway/*.java
jar cf bin/zabbix-java-gateway-2.0.4.jar -C class/src .
```

5. インストールされているZabbix Java Gatewayと置き換える（RPMでインストールしてる場合）

```
cp -p bin/zabbix-java-gateway-2.0.4.jar /usr/sbin/zabbix_java/bin/
```

これでCassandraのLoadとか監視できます。

追記
Zabbixの寺島さんに言われてサポートサイトに投稿しました。

[https://support.zabbix.com/browse/ZBX-6404](https://support.zabbix.com/browse/ZBX-6404 "https://support.zabbix.com/browse/ZBX-6404")

今度からZabbix使っていてバグなどを見つけたらここに報告しよう。
