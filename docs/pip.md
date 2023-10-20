# 基础命令

```shell
# 安装库
pip install selenium
# 安装指定版本的库
pip install selenium==4.14.0

# 导出当前环境的库信息
pip freeze
pip freeze > requirements.txt
# 根据文件进行库安装
pip install -r requirements.txt

# 指定安装源
pip install selenium -i https://pypi.tuna.tsinghua.edu.cn/simple
```

# 源配置

## 常用源

1. 阿里云 https://mirrors.aliyun.com/pypi/simple/
2. 中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
3. 豆瓣(douban) https://pypi.douban.com/simple/
4. 清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/

## windows

配置文件为: `~/pip/pip.ini`(不存在就创建一个)，文件内容如下：

```ini
[global]
timeout = 6000
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn
```

> `~`表示用户的home目录，比如`C:\Users\test`

## linux

配置文件为: `~/.pip/pip.conf`(不存在就创建一个)，文件内容如下：

```conf
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

## 搭建自己源服务