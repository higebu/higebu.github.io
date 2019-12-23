---
title: "VMFork using mob"
slug: 2016-04-27-vmfork-using-mob
date: 2016-04-27T23:57:00Z
categories: 
- "Tech"
tags: 
- "vmware"
- "vsphere"
- "vmfork"
- "mob"
---

Lang: en

We cannot do VMFork without [PowerCLI Extension](https://labs.vmware.com/flings/powercli-extensions) for now. But that means there are VMFork related APIs in vSphere API.

I explored those APIs using the MOB(The Managed Object Browser). Then I found it and I understand how to use it.

**Disclaimer: VMFork is not officially supported by VMware, please use at your own risk.**

## Table of contents

[TOC]

## VMFork related APIs

There are following methods in VirtualMachine object.

* CreateForkChild_Task
* EnableForkParent_Task
* DisableForkParent_Task
* RetrieveForkChildren_Task
* RetrieveForkParent_Task

Also, there are `config.forkconfiginfo` and `runtime.quiescedforkparent` in VirtualMachine properties.

These methods and properties are found in the HTML source of VM page on the MOB.

This time, we want to run the VMFork, so we use `EnableForkParent_Task` and `CreateForkChild_Task`.

## How to run the VMFork using the MOB.

### 1. Open the MOB.

```
https://<vcenter_ip_or_hostname>/mob/
```

### 2. Open the VirtualMachine you want to use as parent VM.

Open the parent VM with using rootFolder or searchIndex. The URL would be like here.

```
https://<vcenter_ip_or_hostname>/mob/?moid=<your_vm_moid>
```

### 3. Run EnableForkParent_Task

Open following URL.

```
https://<vcenter_ip_or_hostname>/mob/?moid=<your_vm_moid>&method=enableForkParent
```

This method has no parameters, you have only to click `Invoke Method`.

### 4. Quiesce the parent VM

Run this command on the parent VM via console or SSH.

```
vmtoolsd --cmd 'vmfork-begin -1 -1'
```

If you want to automate it, you can use [GuestOperationsManager][GuestOperationsManager].ProcessManager.

PowerCLI's `Enable-InstantCloneVM` upload PreQuiesceScript and PostCloneScript with operations up to this point.

You can upload these scripts with [GuestOperationsManager][GuestOperationsManager] instead of PowerCLI.

Also, It seems that PowerCLI's `Enable-InstantCloneVM` runs PreQuiesceScript and PostCloneScript with [GuestOperationsManager][GuestOperationsManager]. The command is like here.

```
$prescript_path;vmtoolsd --cmd 'vmfork-begin -1 -1';$postscript_path
```

### 5. Run VMFork

Use `CreateForkChild_Task`. It is same as PowerCLI's `New-InstantCloneVM`. The URL is following.

```
https://<vcenter_ip_or_hostname>/mob/?moid=<your_vm_moid>&method=createForkChild
```

`CreateForkChild_Task` has parameters, `name` and `spec`. `name` is child VM name. And I guess `spec` is [VirtualMachineCreateChildSpec][VirtualMachineCreateChildSpec]. Minimun `spec` is here.

```xml
<spec>
    <persistent>false</persistent>
</spec>
```

Click `Invoke Method`. The child VM will be created in an instant.

## References

* [VMware Instant Clone is now at your fingertips with the updated PowerCLI Extensions fling!](http://blogs.vmware.com/PowerCLI/2015/08/vmware-instant-clone-now-fingertips-new-powercli-extensions-fling.html)
* [Instant Clone PowerCLI cmdlets Best Practices & Troubleshooting](http://www.virtuallyghetto.com/2015/08/instant-clone-powercli-cmdlets-best-practices-troubleshooting.html)
* [How to VMFork aka Instant Clone Nested ESXi?](http://www.virtuallyghetto.com/2015/08/how-to-vmfork-aka-instant-clone-nested-esxi.html)
* [lamw/vmfork-community-customization-scripts](https://github.com/lamw/vmfork-community-customization-scripts)
* [vSphere Integrated Containers](https://github.com/vmware/vic)
* [How to browse the internal vSphere APIs](https://communities.vmware.com/docs/DOC-11670)

 [GuestOperationsManager]: https://pubs.vmware.com/vsphere-60/topic/com.vmware.wssdk.apiref.doc/vim.vm.guest.GuestOperationsManager.html#field_detail
 [VirtualMachineCreateChildSpec]: https://www.vmware.com/support/developer/converter-sdk/conv61_apireference/vim.vm.CreateChildSpec.html
