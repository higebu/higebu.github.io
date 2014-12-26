Title: iPhoneのメッセージアプリが大量の添付ファイルを受けて起動しなくなったので直した
Slug: how-to-recover-crashing-iphone-message-app-because-of-recieving-many-attached-files
URL: archives/628
save_as: archives/628/index.html
Author: higebu
Category: Tech
Tags: iphone, message, crash

先日iPhone5のメッセージが開かなくなりました。

原因は、その直前に来た大量の添付ファイル付きのメール（MMS）です。

そこで、メッセージが参照しているDBから該当のメールを直接削除することで直しました。

環境

* Mac OSX 10.8.3
* iPhone5 ( iOS 6.1.4 )
* [iBackupBot](http://www.icopybot.com/itunes-backup-manager.htm) 3.5.2
* [MesaSQLite](http://www.desertsandsoftware.com/?page_id=99) 3.2.6

iBackupBot と SQLite をいじれるなんらかのツール（今回は MesaSQLite ）を用意してください。

以下、手順です。

1. iTunes で iPhone をバックアップ
2. iBackupBot で 先ほどのバックアップから `Library/SMS/sms.db` をエクスポート
3. エクスポートされた、 `Library_SMS_sms.db` を MesaSQLite で開き、該当のメール、添付ファイル情報を削除

    1. `Triggers` タブで、 `attachment` テーブルを選択し、`trigger delete_attachment_path` を削除。（後で戻します。）
    2. `message` テーブルから該当のメールを削除。（ `attachment` テーブルのデータも自動で消えます。 ）
    3. SQL Query タブで下記の SQL を実行し、 `attachment` テーブルの `trigger` を元に戻す。

    ```
    CREATE TRIGGER delete_attachment_files AFTER DELETE ON attachment BEGIN SELECT delete_attachment_path(old.filename); END
    ```

4.  iBackupBot で sms.db をインポート
5.  iTunes で iPhone を復元

iBackupBot の使い方は[他のブログ](http://iphone4tips.blog112.fc2.com/blog-entry-43.html)などで詳しく説明されているので割愛して、ここでは3のDBを編集するところを少し詳しく説明しました。

これで、iPhone から見ると添付ファイルが大量に付いたメールは見えなくなり、メッセージアプリが正常に起動するようになりました。
