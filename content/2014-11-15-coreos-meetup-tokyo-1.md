Title: CoreOS + Docker Meetup Tokyo #1 に参加してきました
Slug: coreos-docker-meetup-tokyo-1
Date: 2014-11-15 20:00
Category: Tech
Tags: coreos, docker, meetup, google, heroku
Summary: CoreOS + Docker Meetup Tokyo #1 に参加してきました

[CoreOS + Docker Meetup Tokyo #1][1] に参加してきました。

[CoreOS, Inc][2] の [Kelsey Hightower][3] さんが日本に来ていたので、開催したようです。

開催してくれた、Google の Kazunori Sato さんありがとうございました。

イベントは全部英語だったので少しつらかったですが、事前に CoreOS には触っていたし、別のところで、 Kelsey さんの講演を聞く機会もあったので、だいたい理解できました。

## 感想

### Kelsey さんの発表

Kelsey さんは、 [Kubernetes][4] のコミッターで、 [etcd][5] のコントリビューターなので、どんな質問にもとても詳しく答えていて、参加できてよかったと思いました

発表内容は、 [Kelsey さんの GitHub リポジトリ][6]に置いてある Kubernetes のワークショップ用のテキストを元に行っていて、PCがあればその場で動かしながら話を聞けそうでした。
（この日はPCを持っていなかったので、メモすらしていません。）

また、 k8s 便利すぎてやばいので後で試さないといけないと思いました。

何が便利かというと、特に Docker コンテナのローリングアップデートができるところで、コマンド1発で全てのコンテナがアップデートされるというのが簡単に実現できます。

うちのシステムにも導入したいので、社内に布教しようと思います。

あと、 etcd の発音は、エティシーディに聞こえました。

### LT

1つ目は、 Daniel Dressler さんの btrfs の話で正直ついていけませんでした。

btrfs がいかにいけてるかをスライドなしで語っていて、すごく熱いやつだなと思いましたｗ

2つ目は、Wantedly の Seigo Uchida さんが自作 Docker コンテナ管理ツールを作った話とデモでした。

heroku は便利だけど、日本の DC を選べないので、自作したようです。

他にもツールはあるけど、自作することで、 Docker 周りの技術の理解が深まってよかったと言っていました。

もしかしたら、オープンソース化するかもしれないらしいので、期待しています。

あと、僕も英語でプレゼンできるようになりたいと思いました。

### 懇親会

Google さんのおごりでした。ごちそうさまでした。

最後は、 golang がいかに良いかを Kelsey さんが語っているのを聞いている感じでしたｗ

 [1]: http://www.meetup.com/Docker-Tokyo/events/218561812/
 [2]: https://coreos.com/about/
 [3]: https://github.com/kelseyhightower
 [4]: http://kubernetes.io/
 [5]: https://coreos.com/using-coreos/etcd/
 [6]: https://github.com/kelseyhightower/intro-to-kubernetes-workshop
