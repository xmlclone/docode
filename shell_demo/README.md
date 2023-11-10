# 常用命令

```shell
# 查看系统版本
lsb_release -a
cat /etc/os-release
cat /etc/issue
uname -r
hostnamectl

# 查看系统位数
uname -m 
cat /proc/cpuinfo

# 查看系统资源
df -h
du -h
top   (shift+e 切k m g)
```

# 基础命令

## 文本处理

```shell
# 统计行数 wc -l
cat /proc/cpuinfo | grep processor | wc -l
```

## 日期相关

```shell
date

# 指定格式
date '+%Y%d%m-%H%M'
```

## 环境PATH

```shell
# .bashrc在你的home目录下，即类似/home/linlei下
echo 'export PATH="/home/linlei/anaconda3/bin:$PATH"' >> .bashrc
source .bashrc
```

# 高级命令

## grep

```shell
-i 不区分大小写
-n 打印行号
--color 高亮显示，部分操作系统默认加上了
-c 输出统计信息，而不显示具体匹配信息
-e 表示或
-E 表示使用扩展正则表达式
-v 表示反向查找，即输出不匹配指定内容的数据

# 表示输出包含log或sh的文件
ls | grep -e log -e sh

# 正则表达式，正则表达式的匹配符号需要使用\进行转义，比如下面的\*
ls | grep -E \*.log

# 反向查找
ls | grep -v log
```

## awk

```shell
awk -F: '{print $1}' /etc/passwd
awk -F: '{print $1, $3}' /etc/passwd
```

## xargs

```shell
# 与管道符的区别
echo "--help" | cat  # 把前一个命令的输出作为cat命令的输入
echo "--help" | xargs cat # 把前一个命令的输出作为cat命令的参数
# rm mv kill等命令，需要接收的是参数，而不是作为标准输入

# -i参数
# 假设目录下有3个日志文件a.log b.log c.log，需要批量重命名为a.log.bak b.log.bak c.log.bak
# 即可以把前面命令的参数传递多次或者指定位置(默认在最末尾)，-i使用{}作为替换符来替换内容
ls | grep log | xargs -i mv {} {}.bak

# -d参数，设置分隔符，默认是空格
# 批量创建文件(注意echo -n参数指定不换行，否则最后的c\n.log文件是无法创建的)
echo -n "a@b@c@" | xargs -d @ -i touch {}.log

# 批量删除文件
ls | grep log | xargs rm -rf
```

> 这篇文章讲的比较好: https://zhuanlan.zhihu.com/p/556154777?utm_id=0

## sed

```shell
sed 's/src_str/replace_str/flag'

# flag有以下几个选项
# n-也就是直接指定数字，表示替换每行第几次匹配的内容
# g-表示全局替换，也就是全部都替换
```

```shell
[root@2e781dfb0124 /]# cat test1.txt
lin lin lin
lei lin lei
li lin lei

[root@2e781dfb0124 /]# sed 's/lin/xiaolin/' test1.txt
xiaolin lin lin
lei xiaolin lei
li xiaolin lei

sed 's/lin/xiaolin/g' test1.txt
xiaolin xiaolin xiaolin
lei xiaolin lei
li xiaolin lei

[root@2e781dfb0124 /]# sed 's/lin/xiaolin/2' test1.txt
lin xiaolin lin
lei lin lei
li lin lei

[root@2e781dfb0124 /]# sed -i 's/lin/xiaolin/2' test1.txt
[root@2e781dfb0124 /]# cat test1.txt
lin xiaolin lin
lei lin lei
li lin lei
```

# 软件安装

## Ubuntu

```shell
# 离线安装
dpkg -i google-chrome-stable_current_amd64.deb
# 如果离线安装的包依赖不存在，可以通过在线安装的方式自动安装，执行下面命令即可
apt-get -y -f install

# 在线安装
apt-get install python
```