Title: Selenium WebDriver (Java) で自己署名証明書のセキュリティ警告を出さないようにする
Slug: how-to-accept-untrasted-certificates-with-selenium-firefox-driver
URL: archives/354
save_as: archives/354/index.html
Author: higebu
Category: Tech
Tags: java, selenium, firefox

Seleniumでテストするときに自分で作ったSSL証明書だとセキュリティ警告が出てテストできないけど、
Firefoxの場合は以下の方法でスルーできます。

今回は2.0から追加されたWebDriverでやりました。
テスト用にプロファイル作って読み込ませる方法でもできます。
以下ソース。

```
FirefoxProfile profile = new FirefoxProfile();
profile.setAcceptUntrustedCertificates(true);
driver = new FirefoxDriver(profile);
```

Seleniumのダウンロードは[こちら](http://seleniumhq.org/download/ "Selenium Downloads")。
これを書いている時点での最新版は2.15.0でした。

あとはアップロード、ダウンロードのテストもできたら完璧なんですが・・・
