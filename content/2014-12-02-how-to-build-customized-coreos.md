Title: CoreOS のビルド方法とカスタマイズ
Slug: how-to-build-customized-coreos
Date: 2014-12-02 19:30
Category: Tech
Tags: coreos, docker
Summary: CoreOS のビルド方法とカスタマイズについての記事です。

この記事は、 [CoreOS Advent Calendar 2014][2] の2日目の記事です。

[TOC]

[CoreOS][1] は、 Chrome OS をフォークしたもので、 Chrome OS が [Gentoo Linux][3] ベースのため、 CoreOS も Gentoo Linux ベースになっており、 Gentoo のパッケージを持ってくるか、自分で ebuild ファイルを書くことで、パッケージを追加できます。

ただし、 rootfs はリードオンリーになっているため、ビルド時に追加する必要があります。

そこで、この記事では、ビルド方法と、パッケージの追加方法について説明します。

# 1 普通にビルドする方法

基本的には [公式ドキュメント][4]の方法に従います。

また、ここでは Ubuntu 14.04 を利用する前提でコマンドを記載します。

### 1.0. 準備

ドキュメントには記載がありませんが、 root ユーザでは、 cros_sdk コマンドがエラーになるため、ビルド用のユーザを作成してから作業します。

ここでは、 build という名前でユーザを作成します。

```
adduser build
```

curl と git をインストールします。

```
sudo apt-get install -y curl git
```

### 1.1. depot_tools のインストール

depot_tools というのは、[The Chromium Project][5] で使われている、ソースコード管理やコードレビューのためのツールの詰め合わせです。

インストールするには、下記のコマンドを実行します。

```
git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
export PATH="$PATH":`pwd`/depot_tools
```

`PATH` を `.bashrc` などで設定してしまっても良いのですが、自分はこの辺りの処理を全て1つのスクリプトで行っており、常にクリーンな状態からビルドするようにしているため、毎回 `git clone` して `export` しています。

### 1.2. SDK chroot をセットアップ

作業用ディレクトリを作成します。

```
mkdir coreos; cd coreos
```

`.repo` というディレクトリを指定した manifest で初期化します。

```
repo init -u https://github.com/coreos/manifest.git -g minilayout --repo-url https://chromium.googlesource.com/external/repo.git
repo sync
```

上記のコマンドでは、ブランチを指定していないため、 master ブランチが参照されます。

特定のバージョンの CoreOS をビルドするには下記のようにします。

```
repo init -u https://github.com/coreos/manifest.git -b refs/tags/v509.1.0 -g minilayout --repo-url https://chromium.googlesource.com/external/repo.git -m release.xml
repo sync
```

-b でタグを指定し、 -m で manifest ファイルを指定しています。

manifest ファイルを指定しない場合、 master.xml が参照され、 master.xml の内容では、coreos-overlay や docker などの各リポジトリの最新のソースを取ってきてしまうため、欲しいバージョンの CoreOS とはかけ離れたものになってしまいます。

release.xml では、各リポジトリの特定の revision が書いてあり、正しいソースを取得することができます。

ちなみに、実際に v509.1.0 の manifest で `repo sync` すると [docker のリポジトリが間違っている][6]ため、エラーになります。

v509.1.0 をビルドする場合は、 build-509 というブランチを利用しなければなりません。

repo については、詳しくは [Android の開発者用のサイト][7]を見ると良いです。

### 1.3. イメージのビルド

下記のコマンドを実行するとコンパイラなどの必要なツールを含んだ SDK chroot がダウンロードされ、 chroot 環境に入ります。

```
cros_sdk
```

chroot 環境に入らなかった場合は、 --enter を付けて再度実行すると入ります。

次に core ユーザのパスワードを設定します。

```
./set_shared_user_password.sh
```

ビルドする環境を設定します。

```
echo amd64-usr > .default_board
./setup_board
```

パッケージをビルドします。

```
./build_packages
```

イメージをビルドします。

```
./build_image --noenable_rootfs_verification dev
```

上記は開発用のイメージを作成するときのコマンドですが、プロダクション環境用のイメージを作るには次のようにします。

```
./set_official
COREOS_OFFICIAL=1 ./build_image prod --group Alpha
```

`./set_official` で、 coreos-au-key という自動アップデート時に使われる認証用の鍵がインストールされます。

また、 `COREOS_OFFICIAL=1` で、バージョン番号から日付が消えます。

最後に、各環境用のイメージに変換します。例えば、VMware 用のイメージであれば、下記のようにします。

```
./image_to_vm.sh --from=../build/images/amd64-usr/latest --board=amd64-usr --prod_image --format vmware
```

変換後のファイルは、 src/build/images/amd64-usr/latest/ 配下に作成されます。

# 2. カスタマイズする

ここからはおまけになってしまうかもしれませんが、 CoreOS をニフティクラウドの上で動かすために追加したパッケージについて説明します。

zsh 入れたいみたいな話ではなく、自分たち専用のイメージを作って OEM 対応したいという場合の話になっています。

### 2.1. oem-niftycloud パッケージの作成

CoreOS は、各 IaaS プロバイダや、 OpenStack 、 CloudStack などの IaaS 基盤向けに oem-hoge というパッケージを作って対応しています。

それらのソースは [coreos/coreos-overlay/coreos-base][8] 配下にあります。

oem-hoge でやっていることは、主に下記の4つです。

1. `/etc/environment` に `COREOS_PUBLIC_IPV4` などを設定する
1. oem 用の cloud-config で、必要なエージェントなどのデーモンを起動する
1. SSHキーを設定する
1. ユーザが設定した cloud-config を読み込んで、 coreos-cloudinit に渡す

oem-niftycloud は下記のようになりました。

```
coreos-overlay/coreos-base/oem-niftycloud/
├── files
│   ├── cloud-config.yml
│   ├── coreos-setup-environment
│   ├── niftycloud-coreos-cloudinit
│   ├── niftycloud-run-startup-scripts
│   └── niftycloud-ssh-key
└── oem-niftycloud-0.0.1.ebuild
```

* cloud-config.yml
    * niftycloud 用の cloud-config
* coreos-setup-environment
    * /etc/environment 作成用スクリプト
* niftycloud-coreos-cloudinit
    * ユーザが設定した cloud-config を読み込んで、 coreos-cloudinit に渡すスクリプト
* niftycloud-run-startup-scripts
    * ユーザが設定したスクリプトを読み込んで、実行するスクリプト
* niftycloud-ssh-key
    * sshキーを設定するスクリプト
* oem-niftycloud-0.0.1.ebuild
    * oem-niftycloud をインストールするための ebuild ファイル

各スクリプトについては、 [GitHub のリポジトリ][9]に置いてありますので、そちらをご参照ください。

### 2.2. niftycloud フォーマットの作成

CoreOS はイメージをビルドする際に各環境毎に必要なパッケージを入れるようになっています。

具体的には、 [coreos/scripts/image_to_vm.sh][10] の --format オプションで指定するのですが、当然ながら niftycloud というフォーマットはありません。

vmware であれば、 open-vm-tools が入るようになっていたり、 gce であれば、 GCE 上で動かすために必要なデーモンがインストールされるようになっています。

そこで、ニフティクラウド用のイメージを作成するため、 `--format niftycloud` と指定できるようにしました。

修正したのは、 [scripts/build_library/vm_image_util.sh][11] というスクリプトです。

修正内容は長くなってしまうので、 [GitHub のコミットログ][12]をご参照ください。

### 2.3. ビルド方法

ここまで読めばわかると思いますが、1.3. イメージのビルドの最後の手順のオプションが下記のようになるだけです。

```
./image_to_vm.sh --from=../build/images/amd64-usr/latest --board=amd64-usr --prod_image --format niftycloud
```

# 3. ビルドの自動化

これまでの作業を手で行うのは大変面倒なので自動化しています。

自動化する際の Tips を紹介しておきます。

### 3.1. repo コマンドを初めて実行したときに色の出力をどうするか聞かれないようにする

初めて `repo init` すると下記のような質問が出ます。

```
Your identity is: Yuya Kusakabe <yuya.kusakabe@gmail.com>
If you want to change this, please re-run 'repo init' with --config-name

Testing colorized output (for 'repo diff', 'repo status'):
  black    red      green    yellow   blue     magenta   cyan     white
  bold     dim      ul       reverse
Enable color display in this user account (y/N)?
```

これを回避するには、git の色の設定を前もってしておきます。

```
git config --global color.ui false
```

### 3.2. core ユーザのパスワード設定でパスワードを聞かれないようにする

下記のように引数にパスワードを渡します。

```
./set_shared_user_password.sh {password}
```

### 3.3. SDK chroot 環境に入らないようにする

`cros_sdk` コマンドの後ろに `--` を付けてから内部で実行したいコマンドを並べます。

```
cros_sdk --download
cros_sdk -- "./set_shared_user_password.sh" "core"
echo "amd64-usr" > src/scripts/.default_board
cros_sdk -- "./setup_board"
cros_sdk -- "./build_packages"
cros_sdk -- "./set_official"
cros_sdk -- "COREOS_OFFICIAL=1" "./build_image" "prod" "--group" "Alpha"
cros_sdk -- "./image_to_vm.sh" "--from=../build/images/amd64-usr/latest" "--board=amd64-usr" "--prod_image" "--format" "niftycloud"
```

# 最後に

CoreOS をビルドしたり、 OEM 対応したりする人は稀だと思いますが、似たようなことをする方の参考になれば幸いです。

実は、ここまでやってもニフティクラウドのイメージは自動アップデートに対応できていません。

~~理由は、本家の ohama サーバに oem-id が登録されていないせいのようなので、現在プルリクエスト中です。~~

2014/12/29 追記: アップデートできなかったのは別の問題だったようで、ビルドし直したところ、問題なくアップデートできました。

ちなみに `update_engine_client -update` で手動アップデートできるので便利です。

 [1]: http://qiita.com/advent-calendar/2014/coreos
 [2]: https://coreos.com/
 [3]: https://www.gentoo.org/
 [4]: https://coreos.com/docs/sdk-distributors/sdk/modifying-coreos/
 [5]: http://www.chromium.org/
 [6]: https://github.com/coreos/manifest/commit/70e6eadb9e729f0c9f14bff3f29270cfd32082c3
 [7]: https://source.android.com/source/using-repo.html
 [8]: https://github.com/coreos/coreos-overlay/tree/master/coreos-base
 [9]: https://github.com/higebu/coreos-overlay/tree/niftycloud/coreos-base/oem-niftycloud
 [10]: https://github.com/coreos/scripts/blob/master/image_to_vm.sh
 [11]: https://github.com/higebu/scripts/blob/niftycloud/build_library/vm_image_util.sh
 [12]: https://github.com/higebu/scripts/commit/73e3b17251a6690a09bf9af5d078453614b42e36

