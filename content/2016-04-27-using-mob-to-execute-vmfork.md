title: VMForkをmobから実行する
Slug: 2016-04-27-using-mob-to-execute-vmfork
Date: 2016-04-27 23:57
Category: Tech
Tags: vmware,vsphere,vmfork,mob
Summary: VMForkをmobから実行する手順です。

現状では[PowerCLI Extension](https://labs.vmware.com/flings/powercli-extensions)を使わないとVMForkは実行できませんが、PowerCLIを使って実行できるということはAPIがあるということです。

mobを探検したところ、VMFork関連のAPIが見つかり、実行方法もわかったので書いておきます。

**この記事の内容はVMware非公式で、私を含め、誰もサポートしていません。試すときは自己責任でお願いします。**

[TOC]

## VMFork関連の非公開のAPI

VirtualMachineに下記のメソッドがあります。

* CreateForkChild_Task
* EnableForkParent_Task
* DisableForkParent_Task
* RetrieveForkChildren_Task
* RetrieveForkParent_Task

これらは、mobでVMを開き、ページのソースを見ると見つかります。

今回はVMForkするところまでなので、`EnableForkParent_Task`と`CreateForkChild_Task`を使います。

## mobからVMForkを実行する方法

### 1. mobを開く

```
https://<vcenter_ip_or_hostname>/mob/
```

### 2. 親VMのページを開く

その後、rootFolderからたどるなり、searchIndexを使うなりして、親にするVMを開きます。URLは下記のようになっているはずです。

```
https://<vcenter_ip_or_hostname>/mob/?moid=vm-111
```

### 3. EnableForkParent_Taskを実行する

標準で実行できるメソッドであれば、ページ下方にリンクがありますが、非公開APIの場合、リンクはありません。

そこで、下記のようにURLに直接入れます。

```
https://<vcenter_ip_or_hostname>/mob/?moid=vm-111&method=enableForkParent
```

開けばわかりますが、パラメータはありませんので、`Invoke Method`をクリックするだけです。

### 4. 親VMをquiesced状態にする

これは親VM内から実行する必要があります。

親VMにコンソールやSSHで入るなりして、下記のコマンドを実行します。

```
vmtoolsd --cmd 'vmfork-begin -1 -1
```

自動でやる場合には、APIの[GuestOperationsManager][GuestOperationsManager]のProcessManagerを使えば良いと思います。

PowerCLIの`Enable-InstantCloneVM`ではここまでの操作と一緒に、PreQuiesceScriptとPostCloneScriptのアップロードを行っています。

PowerCLIを使わない場合、PreQuiesceScriptとPostCloneScriptのアップロードはやはり[GuestOperationsManager][GuestOperationsManager]を使うことになります。

子VMがForkされたときにPostCloneScriptが自動で実行されているようなので、CustomizationSpec辺りを使っているのかなと思っていますが、CustomizationGuiRunOnceはWindowsでしか使えなかった気がしていたり、vCloud Directorではstart up scriptをLinuxでも登録できたような気がしていたりして、どうやるのかはっきりとはわかっていません。

### 5. VMForkする

APIとしては`CreateForkChild_Task`です。PowerCLIの`New-InstantCloneVM`にあたります。

URLは下記の通りです。

```
https://<vcenter_ip_or_hostname>/mob/?moid=vm-112&method=createForkChild
```

パラメータは`name`と`spec`があるので、`name`に子VMの名前を入れ、`spec`には[VirtualMachineCreateChildSpec][VirtualMachineCreateChildSpec]を入れます。

[VirtualMachineCreateChildSpec][VirtualMachineCreateChildSpec]はググったらConverterのSDKのドキュメントに載っているものと同じだったのでそれを参考にします。

最小の`spec`は下記の通りで、これを入れて`Invoke Method`します。

```xml
<spec>
    <persistent>false</persistent>
</spec>
```

そうすると一瞬で子VMができると思います。

ここまでわかると[govmomi](https://github.com/vmware/govmomi)などに機能追加できそうなので、時間があったら追加して試してみたいです。

## 参考

* [VMware Instant Clone is now at your fingertips with the updated PowerCLI Extensions fling!](http://blogs.vmware.com/PowerCLI/2015/08/vmware-instant-clone-now-fingertips-new-powercli-extensions-fling.html)
* [Instant Clone PowerCLI cmdlets Best Practices & Troubleshooting](http://www.virtuallyghetto.com/2015/08/instant-clone-powercli-cmdlets-best-practices-troubleshooting.html)
* [How to VMFork aka Instant Clone Nested ESXi?](http://www.virtuallyghetto.com/2015/08/how-to-vmfork-aka-instant-clone-nested-esxi.html)
* [lamw/vmfork-community-customization-scripts](https://github.com/lamw/vmfork-community-customization-scripts)
* [vSphere Integrated Containers](https://github.com/vmware/vic)
* [How to browse the internal vSphere APIs](https://communities.vmware.com/docs/DOC-11670)

 [GuestOperationsManager]: https://pubs.vmware.com/vsphere-60/topic/com.vmware.wssdk.apiref.doc/vim.vm.guest.GuestOperationsManager.html#field_detail
 [VirtualMachineCreateChildSpec]: https://www.vmware.com/support/developer/converter-sdk/conv61_apireference/vim.vm.CreateChildSpec.html
