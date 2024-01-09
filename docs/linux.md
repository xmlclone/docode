# 网络

```sh
# centos
vi /etc/sysconfig/network-scripts/<network-name>
# 重启网络服务(不同版本可能命令不一样)
service network restart
systemctl restart network
systemctl restart NetworkManager
```

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

# 文件目录

```sh
# 软链接
ln -s path/to/src path/to/link
```

# 文本处理

```sh
# awk
# 获取docker image id
docker images | grep none | awk '{print $3}'

# 根据获取到的id删除镜像
docker images | grep none | awk '{print $3}' | xargs docker rmi
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