---
title: Titaniumでエミュレータを動かすとNo such file or directoryと言われる
slug: titanium-android-emulator-no-such-file-or-directory-error
date: 2011-04-19T00:00:00+09:00
aliases:
- archives/256
categories: 
- "Tech"
tags: 
- "android"
- "titanium"
---

AndroidアプリとiPhoneアプリがJavaScriptで開発できるあれですが、

くだらないところで詰まってたので、メモっておく。

環境：Windows 7

Titaniumのインストールは[公式サイト][1]を見ればできると思う。

今回は、インストールは終わったのにサンプルが動かなかった。

使ったサンプルはもちろん[KitchenSink][2]です。

以下そのときのログ。

```
[INFO] Launching Android emulator...one moment
[INFO] Creating new Android Virtual Device (8 WVGA854)
[ERROR] Exception occured while building Android project:
[ERROR] Traceback (most recent call last):
[ERROR] File &quot;C:\ProgramData\Titanium\mobilesdk\win32\1.6.1\android\builder.py&quot;, line 1642, in <module>
[ERROR] s.run\_emulator(avd\_id, avd_skin)
[ERROR] File &quot;C:\ProgramData\Titanium\mobilesdk\win32\1.6.1\android\builder.py&quot;, line 348, in run_emulator
[ERROR] avd\_name = self.create\_avd(avd\_id,avd\_skin)
[ERROR] File &quot;C:\ProgramData\Titanium\mobilesdk\win32\1.6.1\android\builder.py&quot;, line 318, in create_avd
[ERROR] inifilec = open(inifile,'r').read()
[ERROR] IOError: [Errno 2] No such file or directory:
'C:\\Users\\yuya\\.android\\avd\\titanium\_8\_WVGA854.avd\\config.ini'
[INFO] Building KitchenSink for Android ... one moment
[INFO] plugin=C:\ProgramData\Titanium\plugins\ti.log&#92;&#48;.1\plugin.py
[INFO] Detected compiler plugin: ti.log/0.1
[INFO] Compiler plugin loaded and working for android
[INFO] Titanium SDK version: 1.6.1 (03/15/11 11:45 2fdc0c5)
[ERROR] Timed out waiting for emulator to be ready, you may need to close the emulator and try again
```

11、12行目を見ると、Virtual Deviceがないよと言っているようです。

パスを見ると`C:\Users`配下を見に行っているが、自分のパソコンではマイドキュメント系は

全てD:\Users配下に移動しているので.androidフォルダもそっちにある。

というわけで、`C:\Users\yuyaの下にD:\Users\yuya\.android`へのシンボリックリンクを作った。

コマンドプロンプトで以下のコマンドを打つ。

```
cd C:\Users\yuya
mklink .android D:\Users\yuya\.android
```

yuyaのところは自分のユーザ名にしてください。

これでサンプルが動いた。

サンプルが動いたので満足

 [1]: http://developer.appcelerator.com/ "Appcelerator Developer Center"
 [2]: http://developer.appcelerator.com/doc/kitchensink "Getting Started with KitchenSink"
