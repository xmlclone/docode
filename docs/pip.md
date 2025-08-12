```sh
pip install selenium
pip install selenium==4.14.0
pip install selenium -i https://pypi.tuna.tsinghua.edu.cn/simple

pip download requests -d .
pip download -r requirements.txt -d .

pip install --no-index --find-links=/path/to/local/directory requests
```

whl下载: https://conda-forge.org/packages/

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

```conf
; 阿里云
[global]
index-url=http://mirrors.cloud.aliyuncs.com/pypi/simple/

[install]
trusted-host=mirrors.cloud.aliyuncs.com
```