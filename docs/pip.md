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


# 下载包(依赖包也会被下载) -d 指定下载目录
pip download requests -d .
pip download -r requirements.txt -d .
# 从本地安装包，包括依赖
# --no-index指示不要从pypi等查找包
# --find-links指示本地包路径
pip install --no-index --find-links=/path/to/local/directory requests
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

```shell
pip install pip2pi
# pip2pi==0.8.2
dir2pi -S path/to/wheel
# 此时会在目录下生成simple文件夹,里面有index.html等文件
```

数据准备好后(各种需要的依赖包也需要同步,否则无法安装),就可以使用ningx来搭建服务,配置参考如下:

```conf
worker_processes  1;
error_log  logs/error.log;

events {
    worker_connections  1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                     '$status $body_bytes_sent "$http_referer" '
                     '"$http_user_agent" "$http_x_forwarded_for"';
    access_log  logs/access.log  main;
    sendfile        on;
    keepalive_timeout  65;

    server {
        listen       80;
        server_name  localhost;
        access_log  logs/host.access.log  main;

        location / {
            ; 注意修改root路径
            root   path/to/dist/simple;
            index  index.html index.htm;
            ; autoindex配置参考: https://www.python100.com/html/105173.html
            autoindex on;
            autoindex_exact_size off;
            autoindex_localtime on;
        }

        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
    }
}
```

启动或重启nginx

```shell
nginx
nginx -s reload
```

启动后,可以使用`pip install xxx -i http://localhost`测试安装效果

# 发布包

参考[python_demo/xsetuptools](https://github.com/xmlclone/docode/tree/main/python_demo/xsetuptools#%E5%8F%91%E5%B8%83%E5%8C%85)说明

# 参考链接

1. [官方PIP](https://pypi.org/)
2. [内网建自己的pip源](https://blog.csdn.net/qq_42817360/article/details/132690819)