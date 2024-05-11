[toc]

# 常用

```sh
# 每隔1秒输出 nvidia-smi 命令结果
watch -n 1 nvidia-smi

# 统计命令wc
# 默认显示3个数字，分别表示 行 单词数 字符数(包括空格)
# 即分别表示各参数的输出 wc -l, wc -w, wc -c
# 还有一个参数 wc -m 和 -c 类似
ls | wc

# find 第一个指定的查找目录，比如下面的.表示当前目录下查找
# -type 可以不指定
# 查找大于1G的文件
find . -type f -size +1G
# 并输出每个文件大小
find . -type f -size +1G -exec ls -lh {} \;
# 根据文件名查找
find . -type f -name test.log
```

# 网络

## centos

```sh
vi /etc/sysconfig/network-scripts/<network-name>
# 重启网络服务(不同版本可能命令不一样)
service network restart
systemctl restart network
systemctl restart NetworkManager


TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=dhcp
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
NAME=enp1s0
UUID=ffabaa68-f443-48a3-a4ca-b509673a7fc1
DEVICE=enp1s0
ONBOOT=yes


BOOTPROTO=static
IPADDR=<your_static_ip>
NETMASK=<your_subnet_mask>
GATEWAY=<your_gateway_ip>
DNS1=<your_dns_server_ip>
```

## ubuntu

配置文件`/etc/netplan/01-netcfg.yaml`  文件名可能会有不同，但配置基本如下：

```yml
network:
  version: 2
  renderer: networkd   # 这个有可能是 NetworkManager
  ethernets:
    ens33:   # 注意修改为你的网络接口名称，比如可能是 enp0s3
      dhcp4: no
      addresses: [10.0.2.101/24]
      gateway4: 10.0.2.1
      nameservers:
        addresses: [192.168.140.2, 192.168.170.2]
```

如果gateway4无法识别，可以使用routes配置

```yml
network:
  version: 2
  renderer: networkd   # 这个有可能是 NetworkManager
  ethernets:
    ens33:   # 注意修改为你的网络接口名称，比如可能是 enp0s3
      dhcp4: no
      addresses: [10.0.2.101/24]
      routes:
        - to: default
          via: 10.0.2.1
          metric: 200
      nameservers:
        addresses: [192.168.140.2, 192.168.170.2]
```

使用命令`netplan apply`重启网络服务即可。

> 可以通过命令`systemd-resolve --status`查看对应接口的dns-server

# ssh访问

```sh
# centos
sudo yum install openssh-server
sudo systemctl start sshd
sudo systemctl enable sshd
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
```

## 免密配置

A是需要被免密访问的机器，B是访问者

B上面通过`ssh-keygen -t rsa -C test@test.com -b 4096`生成公钥，文件`id_rsa.pub`里面内容复制到A的`authorized_keys`文件里面即可。

其中`authorized_keys`文件也在`.ssh`目录下，如果没有就创建一个

## 允许root登录

一般ubuntu系统会有此限制；首先需要确保root用户已配置密码

```sh
passwd root
su root
```

修改ssh的配置文件

```sh
# 编辑文件 /etc/ssh/sshd_config ，修改内容如下
PermitRootLogin yes

# 重新加载ssh服务
systemctl reload sshd
```

# 文件目录

```sh
# 软链接
ln -s path/to/src path/to/link
```

# 文件查找

```sh
# 查找超过1G的文件
find / -type f -size +1G
```

# 文本处理

```sh
# awk
# 获取docker image id
docker images | grep none | awk '{print $3}'

# 根据获取到的id删除镜像
docker images | grep none | awk '{print $3}' | xargs docker rmi
```

# 压缩解压

```sh
# 打包
tar -czvf xxx.tar xxx
# 解压
tar -xvf xxx.tar
# 解压到指定目录
tar -xvf xxx.tar -C path/to/dst
```

# 包安装

```sh
dpkg -i xxx.deb || true
# 此步骤会根据上面的dpkg发现缺失的依赖并自动安装依赖
apt-get -y -f install
dpkg -i xxx.deb
```

```sh
rpm -ivh xxx.rpm
# 此方式会自动安装依赖
yum install xxxx.rpm
```

## yum源修改

```sh
# centos8
# 备份
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
# 设置
wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-vault-8.5.2111.repo
# 更新和生成缓存
yum makecache 
```

# 存储

## 挂载额外硬盘

```sh
# 查看有哪些设备
lsblk

# 查看具体的设备，注意不是上面lsblk列出的路径，统一的/dev下，sda1 sda2才是和上面lsblk结果对应
fdisk -l /dev/sda1

# 挂载出来
mkdir /mnt/sda1
mount /dev/sda1 /mnt/sda1

# 取消挂载
umount /mnt/sda1

# 如果需要永久挂载(上面方式重启系统后会失效，需要重新挂载)，需要在/etc/fstab增加内容
/dev/sda1 /mnt/sda1 auto defaults 0 0
```

# 字体

```sh
# 查找，中文字体包，一般选择 Simplified Chinese fonts 包安装
yum search font | grep -i chinese

# 设置字符编码
export LANG=zh_CN.UTF-8

# 查看字符编码
locale
```

# 日期/时间处理

```sh
# 修改时区
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
ln -sf /usr/share/zoneinfo/UTC /etc/localtime
```