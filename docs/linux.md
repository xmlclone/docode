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

# 日期/时间处理

```sh
# 修改时区
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
ln -sf /usr/share/zoneinfo/UTC /etc/localtime
```