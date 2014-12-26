Title: Ubuntu11.10にJenkinsをインストールする（Apacheの裏で動かす）
Slug: how-to-install-jenkins-to-ubuntu1110
URL: archives/360
save_as: archives/360/index.html
Author: higebu
Category: Tech
Tags: jenkins, ubuntu, apache

[{% img http://jenkins-ci.org/sites/default/files/jenkins_logo.png Jenkins %}](http://jenkins-ci.org/)

最近、Jenkinsを入れたので入れ方のメモ。

Jenkinsって何なのっていうのはJenkinsユーザー会が翻訳しているドキュメントに任せます。

<https://wiki.jenkins-ci.org/display/JA/Jenkins>

* バージョン
    * Ubuntu11.10
    * Apache 2.2.20
    * Java 1.6.0_23
    * Ant 1.8.2
    * Maven 2.2.1

JDKインストール
---------------

```bash
sudo aptitude update
sudo aptitude install -y openjdk-6-jdk
```

AntとMavenインストール
----------------------

```bash
sudo aptitude install -y ant
sudo aptitude install -y maven2
```

Jenkinsインストール
-------------------

```bash
sudo aptitude install -y jenkins
```

この時点で8080でJenkins立ち上がってる

以下、`http://localhost:8080/`から`http://localhost/jenkins`に変更するための設定

```bash
sudo vi /etc/init/jenkins.conf

env HTTP_PORT=12345 # 変更
env PREFIX="/jenkins" # 追記
env JAVA_HOME="/usr/lib/jvm/java-6-openjdk/" 変更

JENKINS_ARGS="--webroot=$JENKINS_RUN/war --httpPort=$HTTP_PORT --ajp13Port=$AJP_PORT --prefix=$PREFIX" # 変更（最後の--prefix=$PREFIXを追加）
```

Apacheインストール
------------------

```bash
sudo aptitude install -y apache2
```

mod_proxyインストール＆設定
---------------------------

```bash
sudo a2enmod proxy_http
sudo vi /etc/apache2/mods-enabled/proxy.conf
# 追記
ProxyRequests Off
Order deny,allow
Allow from all
ProxyPass /jenkins http://localhost:12345/jenkins
ProxyPassReverse /jenkins http://localhost:12345/jenkins
```

Apache再起動
------------

```bash
sudo service apache2 restart
```

Jenkins再起動
-------------

```bash
sudo service jenkins restart
```

以上。

あと、Jenkinsの本の紹介をしておく。

[{% img "http://ecx.images-amazon.com/images/I/51bR%2Bvw-EvL._SL160_.jpg" "Jenkins実践入門　～ビルド・テスト・デプロイを自動化する技術 (WEB+DB PRESS plus)" "Jenkins実践入門　～ビルド・テスト・デプロイを自動化する技術 (WEB+DB PRESS plus)" %}](http://www.amazon.co.jp/Jenkins%E5%AE%9F%E8%B7%B5%E5%85%A5%E9%96%80-%EF%BD%9E%E3%83%93%E3%83%AB%E3%83%89%E3%83%BB%E3%83%86%E3%82%B9%E3%83%88%E3%83%BB%E3%83%87%E3%83%97%E3%83%AD%E3%82%A4%E3%82%92%E8%87%AA%E5%8B%95%E5%8C%96%E3%81%99%E3%82%8B%E6%8A%80%E8%A1%93-WEB-DB-PRESS-plus/dp/4774148911%3FSubscriptionId%3DAKIAJ3OPGEYIQUTBLNFA%26tag%3Dhigebu-22%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3D4774148911)

これ見れば大抵のことはできると思う。

[{% img "http://ecx.images-amazon.com/images/I/51v-MV54goL._SL160_.jpg" "Jenkins" "Jenkins" %}](http://www.amazon.co.jp/Jenkins-John-Ferguson-Smart/dp/4873115345%3FSubscriptionId%3DAKIAJ3OPGEYIQUTBLNFA%26tag%3Dhigebu-22%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3D4873115345)

最後にプラグインの作り方が載っていて熱い。

[{% img "http://ecx.images-amazon.com/images/I/51SQr0pWG8L._SL160_.jpg" "WEB+DB PRESS Vol.67" "WEB+DB PRESS Vol.67" %}](http://www.amazon.co.jp/WEB-DB-PRESS-Vol-67-%E5%B7%9D%E5%8F%A3/dp/4774149942%3FSubscriptionId%3DAKIAJ3OPGEYIQUTBLNFA%26tag%3Dhigebu-22%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3D4774149942)

特集されている。すぐ読めるので、Jenkinsって何って人におすすめ。

次回はSubversionとの連携か、その先のSeleniumとの連携とか、何かプラグイン関連の話かな。
