---
title: Jenkins の Warnings Plugin で Python の依存パッケージの更新をチェックする
slug: use-piprot-with-jenkins-warnings-plugin
date: 2015-10-28T23:50:00Z
categories: 
- "Tech"
tags: 
- "python"
- " pip"
- " piprot"
- " jenkins"
---


[TOC]

Pythonで開発していると、依存しているパッケージたちが古いのかどうか自動でチェックしたくなりますが、クローズドなものだと [shields.io][0] のような外部のサービスでチェックすることができません。そこで、[piprot][1]と[Jenkins][2]の[Warnings Plugin][3]でチェックできるようにします。

 [0]: http://shields.io/
 [1]: https://piprot.io/
 [2]: https://jenkins-ci.org/
 [3]: https://wiki.jenkins-ci.org/display/JENKINS/Warnings+Plugin

## piprot について

[piprot][1] は `pip install -U piprot` でインストールでき、 `piprot requirements.txt` で依存パッケージが古いかどうかチェックできます。

コマンドでメールを送信したい場合は年間$25払ってとWebページには記載されていますが、メールを送信しなければフリーで使えます。

コマンドの実行結果は下記のような感じです。

```bash
$ piprot requirements.txt test_requirements.txt 
click (5.1) is up to date
elastictabstops (1.0.0) is up to date
pyvmomi (5.5.0-2014.1.1) is out of date. Latest is 5.5.0-2014.1
flake8-pep257 (1.0.3) is up to date
flake8 (2.5.0) is up to date
pep257 (0.6.0) is 80 days out of date. Latest is 0.7.0
pep8-naming (0.3.3) is up to date
piprot (0.9.4) is up to date
pytest-cov (2.2.0) is up to date
pytest-xdist (1.13.1) is up to date
pytest (2.8.2) is up to date
tox (2.1.1) is up to date
Your requirements are 65 days out of date
```

## Compiler Warnings の設定

いきなりですが、Jenkinsに[Warnings Plugin][3]をインストールしている前提です。

Jenkins -> Manage Jenkins -> Compiler Warnings でパーサを追加します。

設定は下記のようにします。

* Name: `Piprot`
* Link name: `Piprot`
* Trend report name: `Piprot Warnings Trend`
* Regular Expression: `(.+) \((.+)\) .* out of date. Latest is (.+)`
* Mapping Script:

```groovy
import hudson.plugins.warnings.parser.Warning

String requiredPackage = matcher.group(1)
String currentVersion = matcher.group(2)
String latestVersion = matcher.group(3)
String categories = "piprot"
String message = requiredPackage + " " + currentVersion + " is out of date. Latest is " + latestVersion

return new Warning(requiredPackage, 0, "Piprot Parser", categories, message)
```

## Job の設定

下記のような感じで、Build -> Execute shell にスクリプトを書き、 `piprot` を実行するようにします。

```bash
piprot requirements.txt
```

Post-build Actions -> Scan for compiler warnings の Scan console log に下記のように設定します。

* Parser: `Piprot`

さらに Advanced... で、下記のようにしています。

![status-thresholds](/images/20151028-status-thresholds.png)
## ビルド結果

下記の画像のようにビルド結果にPiprotというのが追加されます。

![build-result-warnings](/images/20151028-build-result-warnings.png)
クリックすると下記のような画面になります。

![piprot-details-files](/images/20151028-piprot-details-files.png)
Mapping Scriptでパッケージ名をファイル名としているので、パッケージ毎に情報が表示されています。

Warningsタブ。

![piprot-details-warnings](/images/20151028-piprot-details-warnings.png)
Detailsタブ。

![piprot-details-details](/images/20151028-piprot-details-details.png)
トレンドのグラフも表示されます。

![piprot-warnings-trend](/images/20151028-piprot-warnings-trend.png)