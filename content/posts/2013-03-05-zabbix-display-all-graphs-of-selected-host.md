---
title: Zabbixのグラフ画面で選択したホストのグラフを全て表示するパッチ
slug: zabbix-display-all-graphs-of-selected-host
date: 2013-03-05T00:00:00+09:00
aliases:
- /archives/561
categories: 
- "Tech"
tags: 
- "zabbix"
- "php"
- "patch"
---

ちょっと前に、Zabbixのグラフ画面で選択したホストのグラフを全て表示するようにするパッチを作ったので。

Zabbix2.0.4でしかテストしてませんが、2.0.5でも動くはず。

パッチ当てるときは下記のような感じ。

``` bash
patch -p1 -d /usr/share/zabbix < zabbix2.0.4_display_all_graph.patch
```

中身は下記の通り。ダウンロードも下から。

<script src="https://gist.github.com/higebu/4591912.js"></script>
