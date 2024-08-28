

```shell
sudo apt-get install linux-headers-$(uname -r)
Reading package lists... Done
Building dependency tree       
Reading state information... Done
linux-headers-5.11.0-41-generic is already the newest version (5.11.0-41.45~20.04.1).
linux-headers-5.11.0-41-generic set to manually installed.
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
```

```shell
sudo apt-get update
sudo apt-get install linux-headers-generic
[sudo] password for shyuan: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  libblkid1:i386 libmount1:i386 libuuid1:i386 linux-headers-5.4.0-176 linux-headers-5.4.0-176-generic
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  linux-headers-5.4.0-190 linux-headers-5.4.0-190-generic
The following NEW packages will be installed:
  linux-headers-5.4.0-190 linux-headers-5.4.0-190-generic linux-headers-generic
0 upgraded, 3 newly installed, 0 to remove and 200 not upgraded.
Need to get 12.4 MB of archives.
After this operation, 86.5 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 https://mirrors.zju.edu.cn/ubuntu focal-security/main amd64 linux-headers-5.4.0-190 all 5.4.0-190.210 [11.0 MB]

```

```shell
sudo apt-get install linux-source
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  libblkid1:i386 libmount1:i386 libuuid1:i386 linux-headers-5.4.0-176 linux-headers-5.4.0-176-generic
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  linux-source-5.4.0
Suggested packages:
  kernel-package libqt3-dev
The following NEW packages will be installed:
  linux-source linux-source-5.4.0
0 upgraded, 2 newly installed, 0 to remove and 200 not upgraded.
Need to get 135 MB of archives.
After this operation, 143 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 https://mirrors.zju.edu.cn/ubuntu focal-security/main amd64 linux-source-5.4.0 all 5.4.0-190.210 [135 MB]
Get:2 https://mirrors.zju.edu.cn/ubuntu focal-security/main amd64 linux-source all 5.4.0.190.188 [2,480 B]                         
Fetched 135 MB in 1min 45s (1,290 kB/s)                                                                                            
Selecting previously unselected package linux-source-5.4.0.
(Reading database ... 304434 files and directories currently installed.)
Preparing to unpack .../linux-source-5.4.0_5.4.0-190.210_all.deb ...
Unpacking linux-source-5.4.0 (5.4.0-190.210) ...
Selecting previously unselected package linux-source.
Preparing to unpack .../linux-source_5.4.0.190.188_all.deb ...
Unpacking linux-source (5.4.0.190.188) ...
Setting up linux-source-5.4.0 (5.4.0-190.210) ...
Setting up linux-source (5.4.0.190.188) ...

```

```shell
cd /usr/src
sudo tar -xvf linux-source-*.tar.bz2
```
