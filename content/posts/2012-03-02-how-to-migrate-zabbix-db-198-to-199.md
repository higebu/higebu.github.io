---
title: Zabbix1.9.8から1.9.9にするときのDBスキーマ変更パッチ
slug: how-to-migrate-zabbix-db-198-to-199
date: 2012-03-02T00:00:00+09:00
aliases:
- /archives/372
categories: 
- "Tech"
tags: 
- "zabbix"
- "db"
- "migration"
---

[![Zabbix](https://www.zabbix.com/img/zabbix_logo.png =120x31 "Zabbix")][1]

Zabbixを1.9.8から1.9.9にしたらエラーを吐いていたので、調べたらDBのスキーマ変わってて、パッチもあった。

ぐぐったら出てきたページ↓

<https://www.zabbix.com/forum/showthread.php?t=25046>

```
18031:20120209:100634.790 [Z3005] query failed: [1054] Unknown column 'mt.status' in 'field list'
 [select m.mediatypeid,m.sendto,m.severity,m.period,mt.stat us from media m,media_type mt where m.mediatypeid=mt.mediatypeid and m.active=0 and m.userid=3]
```

完全に一致。

パッチのページ

[https://zabbix.org/wiki/How\_to/trunk\_db_patches][2]

以下、パッチ当てる手順

* 環境
    * CentOS 5.7
    * MySQL 5.0.77
    * DB名 zabbix
    * DBユーザ zabbix svnは入ってる前提

最新のパッチをダウンロード

```bash
svn co https://www.zabbix.org/svn/zabbixorg/zabbix/upgrade_incremental/
cd upgrade_incremental
```


DBにバージョン情報登録

```bash
grep 1.9.8 releases
23551
mysql -uzabbix -p password zabbix -e create table dbdata (name varchar(32), value int)
mysql -uzabbix -p password zabbix -e insert into dbdata values ('dbversion', '23551')
```

パッチ生成

```bash
./upgrade_incremental zabbix
./generate_version_patch 1.9.8 1.9.9
```

パッチ実行

```bash
mysql -uzabbix -p password zabbix < zabbix_incremental_patch_1.9.8-1.9.9.sql
```

以上。
これで普通に動くし、エラーで動かなくなってても元に戻る。
でも、テンプレートのインポート/エクスポート機能にバグが直ってないから2.0出るまで待つべきだった。

 [1]: https://www.zabbix.com/
 [2]: https://zabbix.org/wiki/How_to/trunk_db_patches
