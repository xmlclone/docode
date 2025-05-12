# 常用

```sh
# ===============================================================
# 每隔1秒输出 nvidia-smi 命令结果
watch -n 1 nvidia-smi

# ===============================================================
# 统计命令wc
# 默认显示3个数字，分别表示 行 单词数 字符数(包括空格)
# 即分别表示各参数的输出 wc -l, wc -w, wc -c
# 还有一个参数 wc -m 和 -c 类似
ls | wc

# ===============================================================
# find 第一个指定的查找目录，比如下面的.表示当前目录下查找
# -type 可以不指定
# 查找大于1G的文件
find . -type f -size +1G
# 并输出每个文件大小
find . -type f -size +1G -exec ls -lh {} \;
# 根据文件名查找
find . -type f -name test.log

# ===============================================================
# 压缩解压
upzip -d path/to/exact xxx.zip
tar -xvf xxx.tar -C path/to/dst

# ===============================================================
# 软件安装
dpkg -i xxx.deb || true
# 此步骤会根据上面的dpkg发现缺失的依赖并自动安装依赖
apt-get -y -f install
dpkg -i xxx.deb
rpm -ivh xxx.rpm
# 此方式会自动安装依赖
yum install xxxx.rpm

# ===============================================================
# 时间日期处理
# 修改时区
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
ln -sf /usr/share/zoneinfo/UTC /etc/localtime
```

# vim

```sh
# 复制 粘贴
yy p
# 删除
dd
set number
:wq!
/search n/N
# 首尾
gg GG  0 $
# 跳转到指定行
762G
# 撤销
u
```

# 免密认证

A是需要被免密访问的机器，B是访问者(比如需要通过B传输文件到A)

B上面通过`ssh-keygen -t rsa -C test@test.com -b 4096`生成公钥，文件`id_rsa.pub`里面内容复制到A的`authorized_keys`文件里面即可。

其中`authorized_keys`文件也在`.ssh`目录下，如果没有就创建一个