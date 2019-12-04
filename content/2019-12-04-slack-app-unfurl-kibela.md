title: Kibela のリンクを Slack に貼ったときに展開されるようにした
Slug: slack-app-unfurl-kibela
Date: 2019-12-04 23:30
Category: Tech
Tags: kibela,slack,golang
Summary: Kibela のリンクを Slack に貼ったときに展開されるようにした

この記事は [BBSakura Networks Advent Calendar 2019](https://adventar.org/calendars/4517) の4日目の記事です。

BBSakura Networksでは[Kibela](https://kibe.la/ja)を使っていて、Slackでは日々Kibelaのリンクが飛び交っているのですが、リンクを貼っても展開されないため、何のドキュメントなのかわからず不便でした。
そこで、KibelaのリンクをSlackに貼ったときに展開されるようにするSlack Appを作ったので、使い方を書いておきます。
ソースコードは [https://github.com/higebu/slack-app-unfurl-kibela](https://github.com/higebu/slack-app-unfurl-kibela) に置いてあります。

以下、手順です。

# Kibelaのアクセストークンを取得する

以下のURLにアクセスし、 `アクセストークンの作成` ボタンをクリックすると作成できます。
権限は `read` のみで大丈夫です。

[https://my.kibe.la/settings/access_tokens](https://my.kibe.la/settings/access_tokens)

# Slack Appを作成する

以下の手順で作成します。

1. [https://api.slack.com/apps](https://api.slack.com/apps) を開く
2. `Create New App` ボタンをクリック
3. 名前を入れて、 `Create App`
4. `Event Subscriptions` をクリック
5. `Enable Events` を `On` にする
6. `OAuth & Permissions` を開き、 `Scopes` で `link:write` を追加する
7. `App unfurl domains` を展開し、 `Add Domain` で、 `{TEAM_NAME}.kibe.la` を入力し、 `Save Changes`
8. 左メニューから `Install App` を開き、 `Install App to Workspace` -> `Allow`
9. OAuth Access Token が表示されるのでメモしておく

※後で戻ってくるので、Slack Appの管理画面は開いたままにしておきます。

# herokuにslack-app-unfurl-kibelaをデプロイ

下記のボタンからデプロイできます。

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy/?template=https://github.com/higebu/slack-app-unfurl-kibela)

`App name` に入れた名前がURLになります。具体的には `https://{app name}.herokuapp.com/` のようになります。

`KIBELA_TEAM` にはKibelaのチーム名、 `KIBELA_TOKEN` にKibelaのアクセストークン、 `SLACK_TOKEN` にSlackのOAuth Access Tokenを入力し、 `Deploy App` ボタンを入力してください。

# Slack AppにURLを登録

1. `Event Subscriptions` を開き、 `Request URL` に `https://{app name}.herokuapp.com/` を入力する
2. `Verified` と表示さたら `Enable Events` を `On` にして `Save Changes`

# 動作確認

SlackでKibelaのリンクを含んだメッセージを投稿してみてください。
下記のように展開されるはずです。

{% img /images/20191204-slack-unfurl-kibela.png 500 slack-unfurl-kibela %}
