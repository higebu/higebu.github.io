Title: CassandraとHadoopの連携
Slug: cassandra-and-hadoop-integration
URL: archives/474
save_as: archives/474/index.html
Author: higebu
Category: Tech
Tags: cassandra, hadoop, java

{% img /images/Cassandra_logo.png 500 100 Cassandra Cassandra %}

Cassandraに入れたデータでMapReduceするサンプル（word count）を動かす。

環境

* CentOS 6.3
* Java 1.7.0_10
* Ant 1.8.4
* Cassandra 1.2.0-rc1
* Hadoop 1.1.1

構成

{% img https://cacoo.com/diagrams/FNvWKvGTnip41Zks-6FD2E.png 400 325 Architecture Architecture %}

CassandraとTaskTrackerが同じノードにいるようにする

それぞれのインストール方法は割愛

手順

1. HadoopがCassandraのライブラリを読み込むようにする

```bash
vi /etc/hadoop/hadoop-env.sh
# 末尾に追記
export HADOOP_CLASSPATH="/var/lib/cassandra/lib/*:$HADOOP_CLASSPATH"
```

2. HadoopとCassandraを起動しておく
3. Cassandraのビルド

```bash
git clone git://github.com/apache/cassandra.git
cd cassandra
ant
```

4.  word_countのビルド

```bash
cd examples/hadoop_word_count
vi ivy.xml
# バージョンを合わせる
<dependency org="org.apache.hadoop" name="hadoop-core" rev="1.1.1"/>
ant
```

5.  word_countの設定

```bash
vi bin/word_count
# 下記のように編集（mapred-site.xmlのパスは自分の環境に合わせる）
#$JAVA -Xmx1G -ea -cp $CLASSPATH WordCount output_reducer=$OUTPUT_REDUCER
$JAVA -Xmx1G -ea -cp $CLASSPATH WordCount -conf /etc/hadoop/mapred-site.xml output_reducer=$OUTPUT_REDUCER
```

6.  word_countの実行

```bash
bin/word_count_setup
bin/word_count
bin/word_count_counters
```

参考

* [Hadoop Integration](http://www.datastax.com/docs/1.1/cluster_architecture/hadoop_integration)
* [Hadoop Support](http://wiki.apache.org/cassandra/HadoopSupport#ClusterConfig)
    DataStaxのエンタープライズ版だともっと簡単にやれるらしい
