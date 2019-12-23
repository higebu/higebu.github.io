---
title: Vyattaにrvmとfluentd入れたけどうまくいかなかった
slug: how-to-install-fluentd-to-vyatta
date: 2012-06-03T00:00:00+09:00
aliases:
- /archives/423
categories: 
- "Tech"
tags: 
- "fluentd"
- "vmware"
- "vyatta"
- "rvm"
- "ruby"
---

Vyattaにfluentd入れて、fluentd→fluentdでログ集めようとしたけど失敗した

環境
* ESXi5.0 u1
* Vyatta Core 6.4 (VMXNET3、Debianのリポジトリを追加してからVMware公式のVMware Tools入れてる)
* fluentd 0.10.22

入れた手順

1. rvm入れる

```
# aptitude install ruby-full
# curl -L get.rvm.io | bash -s stable
# source /usr/local/rvm/scripts/rvm
# rvm requirements
# aptitude install build-essential openssl libreadline6 libreadline6-dev curl git-core zlib1g zlib1g-dev libssl-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt-dev autoconf libc6-dev ncurses-dev automake libtool bison subversion
# rvm install 1.9.3
# rvm use ruby-1.9.3
# rvm use 1.9.3 --default
```


2. fluentd入れる

```
# gem install fluentd
```

以下のエラーが出た

```
ERROR:  Loading command: install (LoadError)
    cannot load such file -- zlib
ERROR:  While executing gem ... (NameError)
    uninitialized constant Gem::Commands::InstallCommand
```


3. 必要なパッケージ入れる

```
# rvm pkg install readline
```

ここで

```
Error running 'autoreconf -is --force', please read /usr/local/rvm/log/readline/autoreconf.log
```

が出たら

```
# rvm --skip-autoreconf pkg install readline
```

で入れる

```
# rvm pkg install zlib
# rvm pkg install openssl

```


4. ruby1.9.3入れ直す
```
# rvm remove 1.9.3
# rvm install 1.9.3
# rvm use 1.9.3 --default
```


5. fluentd入れる

```
# gem install fluentd
# fluentd --setup /etc/fluent
# vi /etc/fluent/fluent.conf
# mkdir /var/log/fluent/
# touch /var/log/fluent/vyatta.log
# fluentd -d /var/run/fluentd.pid -c /etc/fluent/fluent.conf
```


これで、受け側のfluentdにログ飛ばす設定したんだけど、ログは飛ばかなくて以下のエラー

```
2012-06-06 17:25:26 +0900: starting fluentd-0.10.22
2012-06-06 17:25:26 +0900: reading config file path="/etc/fluent/fluent.conf"
2012-06-06 17:25:26 +0900: adding source type="tail"
2012-06-06 17:25:26 +0900: adding match pattern="**.**" type="forward"
2012-06-06 17:25:26 +0900: adding forwarding server '192.168.0.230:24224' host="192.168.0.230" port=24224 weight=60
2012-06-06 17:25:44 +0900: detached forwarding server '192.168.0.230:24224' host="192.168.0.230" port=24224 phi=8.148601411473535
2012-06-06 17:26:27 +0900: failed to flush the buffer, retrying. error="no nodes are available" instance=10245920
2012-06-06 17:26:27 +0900: /usr/local/rvm/gems/ruby-1.9.3-p194/gems/fluentd-0.10.22/lib/fluent/plugin/out_forward.rb:137:in `write_objects'
2012-06-06 17:26:27 +0900: /usr/local/rvm/gems/ruby-1.9.3-p194/gems/fluentd-0.10.22/lib/fluent/output.rb:440:in `write'
2012-06-06 17:26:27 +0900: /usr/local/rvm/gems/ruby-1.9.3-p194/gems/fluentd-0.10.22/lib/fluent/buffer.rb:274:in `write_chunk'
2012-06-06 17:26:27 +0900: /usr/local/rvm/gems/ruby-1.9.3-p194/gems/fluentd-0.10.22/lib/fluent/buffer.rb:258:in `pop'
2012-06-06 17:26:27 +0900: /usr/local/rvm/gems/ruby-1.9.3-p194/gems/fluentd-0.10.22/lib/fluent/output.rb:304:in `try_flush'
2012-06-06 17:26:27 +0900: /usr/local/rvm/gems/ruby-1.9.3-p194/gems/fluentd-0.10.22/lib/fluent/output.rb:121:in `run'
12-06-06 17:26:29 +0900: failed to flush the buffer, retrying. error="no nodes are available" instance=10245920
2012-06-06 17:26:29 +0900: /usr/local/rvm/gems/ruby-1.9.3-p194/gems/fluentd-0.10.22/lib/fluent/plugin/out_forward.rb:137:in `write_objects'
2012-06-06 17:26:29 +0900: /usr/local/rvm/gems/ruby-1.9.3-p194/gems/fluentd-0.10.22/lib/fluent/output.rb:440:in `write'
2012-06-06 17:26:29 +0900: /usr/local/rvm/gems/ruby-1.9.3-p194/gems/fluentd-0.10.22/lib/fluent/buffer.rb:274:in `write_chunk'
2012-06-06 17:26:29 +0900: /usr/local/rvm/gems/ruby-1.9.3-p194/gems/fluentd-0.10.22/lib/fluent/buffer.rb:258:in `pop'
2012-06-06 17:26:29 +0900: /usr/local/rvm/gems/ruby-1.9.3-p194/gems/fluentd-0.10.22/lib/fluent/output.rb:304:in `try_flush'
2012-06-06 17:26:29 +0900: /usr/local/rvm/gems/ruby-1.9.3-p194/gems/fluentd-0.10.22/lib/fluent/output.rb:121:in `run'</code>
```

tcpdumpとかいろいろして見てみたんだけど、fluentd同士が生き死にを確認するために飛ばしているというudpのパケットがVMから出ていないようだった

ってこういうの前あったなと思ってググったらKBにありましたよ

[UDP packets are dropped from Linux systems using the VMXNET3 Network
Adapter](http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=2019944 "UDP packets are dropped from Linux systems using the VMXNET3 Network Adapter")

E1000に変えろとかね・・・

もうちょっと検証してみます・・・
