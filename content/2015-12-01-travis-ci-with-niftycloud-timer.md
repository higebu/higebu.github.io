Title: ニフティクラウドタイマーを使ってTravis CIで定期的にビルドを実行する
Slug: travis-ci-with-niftycloud-timer
Date: 2015-12-01 20:00
Category: Tech
Tags: niftycloud, travis-ci
Summary: ニフティクラウドタイマーを使ってTravis CIで定期的にビルドを実行する方法です。

これは、[NIFTY Cloud Advent Calendar 2015](http://qiita.com/advent-calendar/2015/niftycloud)の1日目の記事です。

ハードルを下げるため、ちょっとしたネタにしました。

[Travis CI][0]でGitHubへのpushをトリガーにビルドするのではなく、ビルドを定期的に実行したいときに、[ニフティクラウドタイマー][1]を使って実現する方法です。

タイマーって何？という方は[ニフティクラウドタイマーのご紹介](http://blog.cloud.nifty.com/4058/)をご参照ください。

簡単に言うと、サーバーなしでcronを使えるサービスです。

## 前提

* GitHubのアカウントを持っている
* GitHubのPersonal settingsでPersonal access tokenを作成済(`GITHUB_TOKEN`とする）
* Travis CIのアカウントを持っている
* Travis CIで定期的にビルドしたい何かがある
* ニフティクラウドのアカウントを持っている

## 手順

### Travis CIのAccess TokenをGitHubのPersonal access tokenから取得する

下記のコマンドを叩いてください。

```bash
curl -s -X POST -H 'Content-Type: application/json' -H 'Accept: application/vnd.travis-ci.2+json' https://api.travis-ci.org/auth/github -d '{"github_token":"GITHUB_TOKEN"}'
```

下記のようなレスポンスが返ってきます。

```json
{"access_token":"TRAVIS_TOKEN"}
```

`TRAVIS_TOKEN`の部分にTravis CIのAccess Tokenが入っているはずなので、メモしておきます。

Travis CIのAPI認証について、詳しくは[公式ドキュメント](http://docs.travis-ci.com/api/#authentication)をご参照ください。

### curlで実行してみる

ここで、APIの実行が可能か確認するため、下記のようにcurlでAPIを叩いてみます。

`{TRAVIS_TOKEN}`に先ほど取得したTravis CIのAccess Tokenを、`{ACCOUNT}`に自分のアカウント名、`{REPOSITORY}`に自分のリポジトリ名を入れてください。

成功すると、ビルドが実行されるはずです。

```bash
body='{
"request": {
  "branch":"master"
}}'

curl -s -X POST \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "Travis-API-Version: 3" \
  -H "Authorization: token {TRAVIS_TOKEN}" \
  -d "$body" \
  https://api.travis-ci.org/repo/{ACCOUNT}%2F{REPOSITORY}/requests
```

Travis CIでAPIからのビルドの実行について、詳しくは[公式ドキュメント](http://docs.travis-ci.com/user/triggering-builds/)ｒｙ

### ニフティクラウドタイマーに設定する

設定自体は上記でやってみた、HTTPのリクエストを設定するだけです。

以下、手順です。

ニフティクラウドにログインし、左上のメニューから、タイマーを選択します。

{% img /images/20151201-travis-ci-with-niftycloud-timer-1.png 1261 480 "Select NIFTY Cloud Timer""Select NIFTY Cloud Timer" %} 

タイマー作成ボタンがあると思いますので、それをクリックします。

タイマー名とスケジュールを設定します。メモも設定できます。

{% img /images/20151201-travis-ci-with-niftycloud-timer-2.png 1096 442 "Create Timer" "Create Timer" %}

タイプはHTTPにします。他にはサーバー起動、停止、再起動、削除、設定変更、イメージとして保存、スナップショット取得、MQTT、Fluentdがあります。

{% img /images/20151201-travis-ci-with-niftycloud-timer-3.png 1096 613 "Create Timer" "Create Timer" %}

HTTPを選択するとURL、メソッド、ヘッダー、ボディが設定できるようになるので、下記のように設定します。

* URL
    * `https://api.travis-ci.org/repo/{ACCOUNT}%2F{REPOSITORY}/requests`
* メソッド
    * POST
* ヘッダー

```
Content-Type: application/json
Accept: application/json
Travis-API-Version: 3
Authorization: token {TRAVIS_TOKEN}
```

* ボディ

```json
{
  "request": {
    "branch":"master"
  }}
```

通知の設定をします。

{% img /images/20151201-travis-ci-with-niftycloud-timer-4.png 1093 372 "Create Timer" "Create Timer" %}

確認して、"作成する"をクリックします。

これで、設定は完了です。定期的にビルドが実行されるはずです。

実行の履歴は、作成したタイマーを展開し、実行履歴タブを見ると確認できます。

## Travis CIとニフティクラウドタイマーを使って、自動で最新のCoreOSをインポートする

最後に、実際にこの仕組みを使ってCoreOSのインポートを自動化してみた例をご紹介します。

元々Jenkinsを立てて自動でやっていたんですが、タイマーを使うことでサーバーがいらなくなりました。

ソースは[GitHub](https://github.com/higebu/niftycloud-coreos-scripts)に置いてあるため、それを見てください。

ビルドの様子も[Travis CI](https://travis-ci.org/higebu/niftycloud-coreos-scripts)で見られます。

ほぼエラーになっているのは、新しいバージョンが出て、インポートされたときのみ成功と判定しているためです。

見た目が悪いので改善したいと思っています。


明日、12/02は[@thuydg](http://qiita.com/thuydg@github)がmBaaSとかMQTT辺りの話を書いてくれる予定です。

 [0]: https://travis-ci.org/
 [1]: http://cloud.nifty.com/service/timer.htm
