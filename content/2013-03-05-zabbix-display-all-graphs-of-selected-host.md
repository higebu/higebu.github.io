Title: Zabbixのグラフ画面で選択したホストのグラフを全て表示するパッチ
Slug: zabbix-display-all-graphs-of-selected-host
URL: archives/561
save_as: archives/561/index.html
Author: higebu
Category: Tech
Tags: zabbix, php, patch

ちょっと前に、Zabbixのグラフ画面で選択したホストのグラフを全て表示するようにするパッチを作ったので。

Zabbix2.0.4でしかテストしてませんが、2.0.5でも動くはず。

パッチ当てるときは下記のような感じ。

``` bash
patch -p1 -d /usr/share/zabbix < zabbix2.0.4_display_all_graph.patch
```

中身は下記の通り。ダウンロードも下から。

<script src="https://gist.github.com/higebu/4591912.js"></script>
