# 日常使用

```shell
# 批量重启某些服务
docker ps | grep nginx | awk '{print $13}' | xargs docker restart
# 批量删除服务
docker ps | grep nginx | awk '{print $13}' | xargs docker restart

docker images
docker ps
docker ps -a

# 启动容器
docker run --rm -it ubuntu /bin/bash
# 进入容器
docker exec -it ubuntu /bin/bash

# root用户进入容器
docker exec -u 0 -it ubuntu /bin/bash

# 直接查看命令，比如想查看时间的date命令
docker exec -it ubuntu /bin/bash -c "date"
```

# 安装

## ubuntu

```shell
# 安装工具
apt-get -y install apt-transport-https ca-certificates curl software-properties-common

# 安装证书，成功会返回ok
curl -fsSL http://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -

# 修改镜像源
add-apt-repository "deb [arch=amd64] http://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"

# 更新并安装
apt-get update
apt-get -y install docker-ce

# 验证
docker version
```

<!-- more -->

## centos

离线安装方式

```shell
rpm -ivh docker-ce-cli-18.09.8-3.el7.x86_64.rpm
rpm -ivh container-selinux-2.107-3.el7.noarch.rpm
rpm -ivh containerd.io-1.2.2-3.el7.x86_64.rpm
rpm -ivh docker-ce-18.09.8-3.el7.x86_64.rpm
systemctl start docker
```

在线安装

```shell
yum install -y yum-utils device-mapper-persistent-data lvm2
sudo yum-config-manager --add-repo  http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
yum install docker-ce docker-ce-cli containerd.io docker-compose-plugin -y
systemctl enable docker
systemctl start docker
# 验证
docker run hello-world

# 卸载
yum remove docker-ce
rm -rf /var/lib/docker
```

# 镜像源修改

创建或修改 /etc/docker/daemon.json 文件，修改为如下形式

```json
{
    "registry-mirrors": ["http://hub-mirror.c.163.com"]
}
```

然后通过命令`systemctl restart docker.service`或`service docker restart`重启docker

其中`registry-mirrors`表示设置镜像地址，我们可以配置`insecure-registries`设置私有仓库地址

> 注意多个参数，需要有逗号分隔
> 百度的地址: https://mirror.baidubce.com
> windows的配置文件可能在`C:\Users\<username>\.docker`目录下

# 基本使用

```shell
# 查看本地images
docker images

# 基本使用
docker run ubuntu /bin/echo "Hello"

# 查看开启的容器
docker ps
# 查看所有容器，包括退出的
docker ps -a
# 格式化输出
docker ps --format "table{{.Names}}\t{{.ID}}"
docker ps --format "table{{.Names}}\t{{.ID}}\t{{.Status}}\t{{.Ports}}"

# 交互式容器
docker run -i -t ubuntu /bin/bash
# 非交互式容器(不需要后面的/bin/bash)，但是此时容器可能会停止(要根据这个容器是否会自动启动服务确定)
docker run -d ubuntu

# 后台运行
docker run -itd ubuntu /bin/bash

# 指定运行的名字，后续涉及到容器的ID的都可以使用这个name来替换
docker run -itd --name youname ubuntu /bin/bash

# 随系统启动
docker run --restart always

# 自动删除，和-d互斥，开发时使用或临时使用
docker run --rm xxx

# 传递环境变量
docker run -e VAR1=1 -e VAR2=2 XXX
# 传递宿主机的环境变量
docker run -e VAR1=$(hostname) xxx

# 指定容器hostname
# 当然，如果没有hostname，而是通过--name，那么处于同一个网段(配置了相同的--network)的主机之间也可以通过--name的参数进行访问(此时容器内hostname仍然是一堆码，并没有和--name指定参数一样)
docker exec -itd --hostname youname ubuntu /bin/bash

# 复制本地文件到docker
docker cp src [container]:dst
docker cp chromedriver test:/opt/app

# 复制docker内文件到本地
docker cp 220e464220de:/usr/local/lib/python3.6/site-packages/urllib3/connectionpool.py .

# 查看log
docker logs [ID]
# -f作用类似于tail -f，-t是输出时间戳
docker logs -f -t [ID]

# 停止容器
docker stop [ID]

# stop后的容器，如果没有被删除，可以通过start启动
docker start [ID]/[NAME]

# 重启容器，支持一次性重启多个，直接以空格区分即可
docker restart XXX1 

# 进入容器
docker exec -it [ID] /bin/bash

# 搜索镜像
docker search ubuntu

# 拉取镜像
docker pull ubuntu

# 删除镜像
docker rmi ubuntu

# 删除容器
docker rm [container]

# 查看容器状态和资源占用
docker stats

# 更新已存在容器配置
docker update --cpuset-cpus="0-2" [container]
# 如果更新映射的端口？？？

# 制作镜像
docker commit -m "commit msg" -a "author" [ID] main:tag
# 其中ID是容器ID，main是容器名，tag可以指定版本等信息，比如
docker commit -m="update" -a="test" e218edb10161 runoob/ubuntu:v2
# 还可以通过下面的方式对镜像新增
docker tag [ID] main:tag
# 注意这里的ID是镜像ID，docker commit是容器ID

docker login
docker loing 1.2.3.4
docker login -u admin -p 123456 1.2.3.4

docker logout 1.2.3.4

# push的时候，需要先docker tag，格式为ip/project/image:tag，其中ip是私有仓库的ip，如果不指定那就推送到人家docker的中央仓库了，并且project需要提前在harbor上建好
# 注意push镜像格式为 dockerhub_id/dockerhub_reponame:tag，其中id是你dockerhub上的名称，reponame是你在dockerhub上创建仓库的名字
docker push 1.2.3.4/ubuntu
```

> format的格式化参数支持如下

```shell
# 注意区分大小写，比如ID不能是id
.ID - Container ID
.Image - Image ID
.Command - Quoted command
.CreatedAt - Time when the container was created.
.RunningFor - Elapsed time since the container was started.
.Ports - Exposed ports.
.Status - Container status.
.Size - Container disk size.
.Names - Container names.
.Labels - All labels assigned to the container.
.Label - Value of a specific label for this container. For example {{.Label "com.docker.swarm.cpu"}}
.Mounts - Names of the volumes mounted in this container.
```

> 参考： https://blog.csdn.net/qq_41757556/article/details/109026139

# 网络相关

```shell
# 首先创建docker网络环境(ip网段自定义的)
docker network create --driver bridge --subnet=172.18.0.0/16 --gateway=172.18.0.1 zknet

# 查看创建的docker网络
docker network ls
docker network list
ifconfig #可以看见有br-xxx的网络，IP地址是上面创建的网关地址172.18.0.1

# 运行，其它参数一致
docker run --name zk1 --privileged --network zknet --ip 172.18.0.2
```

# 挂载宿主机目录

```shell
docker run -it -v /usr/codeFile:/opt/code test /bin/bash

# 其中-v指定挂载目录，冒号前面是宿主机的目录，冒号后面是docker里面的目录
```

# 映射网络端口

```shell
docker run -it -p 5000:5000 test /bin/bash

# 其中-p 前者是宿主机的端口号，后者是容器的端口号
```

# docker打包

```shell
# 将容器打包为镜像
docker commit [容器ID] [待产生的镜像名称]

# 查看打包是否成功
docker images

# 镜像打包成tar
docker save -o xxx.tar imageName
docker export -o xxx.tar containerName

# 可以把tar压缩一下
tar -czvf xxx.tar.gz xxx.tar

# 把压缩包转移到其它机器后解压得到tar文件
tar -xzvf xxx.tar.gz

# 把tar转换为镜像
docker load < xxx.tar
docker load -i xxx.tar
# import和load功能相同，但是import可以重命名镜像
docker import xxx.tar -- imageName:tagName

# docker load后镜像为None，原因是dokcer save使用了镜像ID，可以修改为使用名称的方式即可
docker save -o xxx.tar xxx:v1.0
# docker load方式不变，但是不会出现None的情况
docker load < xxx.tar
docker load -i xxx.tar
# docker load的镜像tag如果已经存在，先前的image会被替换为none，故要注意删除none

# 在新机器上查看镜像是否已经生成
docker images
```

> 几个区别:
> docker save保存的是镜像（image），docker export保存的是容器（container）；
> docker load用来载入镜像包，docker import用来载入容器包，但两者都会恢复为镜像；
> docker load不能对载入的镜像重命名，而docker import可以为镜像指定新名称。
> docker load打包镜像通过docker import导入后，无法运行？？？

# iamges重命名

```shell
root@docker:~# docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
gcov                v1                  ae3e147b4d8b        3 hours ago         589MB
ubuntu              1802                ace29c6c05da        3 weeks ago         153MB
ubuntu              latest              72300a873c2c        6 weeks ago         64.2MB
nodesource/trusty   latest              28c48c5c54bd        3 years ago         552MB
```

```
root@docker:~# docker tag 28c48c5c54bd trusty:v1
root@docker:~# docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
gcov                v1                  ae3e147b4d8b        3 hours ago         589MB
ubuntu              1802                ace29c6c05da        3 weeks ago         153MB
ubuntu              latest              72300a873c2c        6 weeks ago         64.2MB
trusty              v1                  28c48c5c54bd        3 years ago         552MB
nodesource/trusty   latest              28c48c5c54bd        3 years ago         552MB
# 注意新建的和原始的image的image id一样，此时不能通过id来删除了，只能通过名字来删除
root@docker:~# docker rmi nodesource/trusty
```

# 创建私有仓库

```shell
docker pull registry
docker run -dti --name=registry -v x:x -p 5000:5000 registry

vim /etc/docker/daemon.json
# 修改为内容如下
{
    "registry-mirrors": ["http://hub-mirror.c.163.com"],
    "insecure-registries": ["192.168.46.50:5000"]
}
service docker restart
docker start registry

# 这里先拉取一个小的镜像来测试
docker pull busybox

# 标记一个需要提交的镜像
root@docker:/etc/docker# docker tag busybox 192.168.46.50:5000/busybox
# 查看一下
root@docker:/etc/docker# docker images
REPOSITORY                   TAG                 IMAGE ID            CREATED             SIZE
192.168.46.50:5000/busybox   latest              83aa35aa1c79        4 weeks ago         1.22MB
# 上传
root@docker:/etc/docker# docker push 192.168.46.50:5000/busybox
The push refers to repository [192.168.46.50:5000/busybox]
a6d503001157: Pushed 
latest: digest: sha256:afe605d272837ce1732f390966166c2afff5391208ddd57de10942748694049d size: 527

# 拉取镜像
docker pull 192.168.46.50:5000/busybox
```

> 注意私有仓库，必须给定IP地址，否则会默认push到官方的地址上去

> 注意如果拉取的时候报错`Error response from daemon: Get https://192.168.46.123:5000/v1/_ping: http: server gave HTTP response to HTTPS client`可以在客户端加入如下配置 `"insecure-registries": ["192.168.46.123:5000"]`

> registry的仓库目录为`/var/lib/registry`，可以挂载到本地

## 查看私有仓库

```shell
root@docker:~# curl -XGET http://192.168.46.123:5000/v2/_catalog
{"repositories":["gcov","ubuntu"]}
root@docker:~# curl -XGET http://192.168.46.123:5000/v2/gcov/tags/list
{"name":"gcov","tags":["latest"]}
root@docker:~# curl -XGET http://192.168.46.123:5000/v2/ubuntu/tags/list
{"name":"ubuntu","tags":["1404"]}
root@docker:~#
```

## 进入私有仓库

```shell
docker exec -it [ID] sh

配置文件在 /etc/docker/registry/config.yml下

如果要配置允许删除私有镜像，需要修改配置
storage:
  delete:
    enabled: true
    
然后通过docker restart [ID] 重启容器
```

## 删除私有仓库镜像

```shell
curl --header "Accept:application/vnd.docker.distribution.manifest.v2+json" -I -XGET 192.168.46.123:5000/v2/gcov/manifests/latest   
HTTP/1.1 200 OK
Content-Length: 2631
Content-Type: application/vnd.docker.distribution.manifest.v2+json
Docker-Content-Digest: sha256:280b9f0e210fab23a31a98729119b51aa512040a2d0adc04acc06feea64e2b27
Docker-Distribution-Api-Version: registry/2.0
Etag: "sha256:280b9f0e210fab23a31a98729119b51aa512040a2d0adc04acc06feea64e2b27"
X-Content-Type-Options: nosniff
Date: Wed, 15 Apr 2020 06:28:08 GMT

curl -I -X DELETE http://192.168.46.123:5000/v2/gcov/manifests/sha256:280b9f0e210fab23a31a98729119b51aa512040a2d0adc04acc06feea64e2b27

# 这里的sha是Docker-Content-Digest对应的

# 进入仓库目录，如果挂载到宿主机，直接进入宿主机
docker/registry/v2/repositories
删除需要删除的镜像的目录即可

删除完成后，执行下面的命令清理
docker exec -it registry sh -c 'registry garbage-collect /etc/docker/registry/config.yml'
```

# 查看容器启动命令

```shell
docker inspect [容器ID或名字]

容器内部可以通过ps -ef 的ID为1的就是
```

# paused

```shell
docker pause [ID]
docker unpause [ID]
```

# 批量删除容器/镜像

```shell
# 删除所有镜像
docker images | awk '{print $3}' | xargs docker rmi -f

# 批量删除退出状态的容器
docker rm `docker ps -a|grep -E "Exited|Created"|awk '{print $1}'`
```

# push镜像到docker hub

```shell
docker login
docker login -u admin -p 12345 1.2.3.4

docker logout 1.2.3.4
```

> 如果docker login报错，可以看是否是http方式，如果是，需要修改/lib/systemd/system/docker.service的ExecStart配置项，增加--insecure-registry 1.2.3.4配置(ip地址修改为需要登录的ip地址)，然后重启docker服务

# 通过SSH访问docker容器

```shell
# docker启动的时候，挂载-p xxx:22，
# xxx表示外部端口，22是ssh默认登录端口，内部映射
apt-get install openssh-server

vim /etc/ssh/sshd_config
# 修改PermitRootLogin 为yes

service ssh restart

# 修改或创建root用户密码
sudo passwd root
```

# 图形化管理

```shell
docker search portainer
docker pull portainer/portainer

docker run -d -p 9000:9000 --restart=always -v /var/run/docker.sock:/var/run/docker.sock --name prtainer portainer/portainer

# 然后输入192.168.46.123:9000访问
```

# 容器资源

```shell
docker run -itd \
  -p 5557:5557 \
  -m 300G --oom-kill-disable \  # -m限制容器使用的内存，--oom-kill-disable避免容器内进程被杀，配合-m使用才能生效
  --cpuset-cpus="0-19" \ # 使用的cpu索引
  --name test --hostname test ubuntu:latest ./run.sh

# 查看容器资源
docker stats
# 查看指定容器的资源，可以跟容器名或者容器ID
docker stats test
```

# 常用docker

## mysql

```shell
docker search mysql

docker pull mysql:latest

docker images

# MYSQL_ROOT_PASSWORD=123456：设置 MySQL 服务 root 用户的密码
docker run -itd --name mysql-test -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 mysql

docker ps

# 宿主机可以通过以下命令访问数据库
mysql -h localhost -u root -p

# 可增加下面的命令把宿主机的/opt/docker_v/mysql/conf挂载到虚拟机的/etc/mysql/conf.d作为永久的配置
-v /opt/docker_v/mysql/conf.d:/etc/mysql/conf.d

# 下面命令把数据存储在本地
-v /data/mysql/data:/var/lib/mysql
```

## 图形化docker(vnc)

```shell
docker pull dorowu/ubuntu-desktop-lxde-vnc

# 无密码，然后可以直接通过http://1.2.3.4:6080/ 访问即可
docker run -it --rm -p 6080:80 dorowu/ubuntu-desktop-lxde-vnc

# 加密, 5900用于vnc
docker run -it --rm -p 6080:80 -p 5900:5900 -e VNC_PASSWORD=ab123456 dorowu/ubuntu-desktop-lxde-vnc
```

> 参考: https://blog.csdn.net/weixin_34795681/article/details/112381769
> docker hub: https://hub.docker.com/r/dorowu/ubuntu-desktop-lxde-vnc/

centos:

```shell
docker pull kasmweb/centos-7-desktop:1.10.0-rolling
docker run --rm  -it --shm-size=512m -p 6901:6901 -e VNC_PW=password kasmweb/centos-7-desktop:1.10.0-rolling
```

默认用户名: kasm_user，浏览器访问6901端口即可，注意是https方式访问

> https://registry.hub.docker.com/r/kasmweb/centos-7-desktop

> 定义自己的镜像: https://kasmweb.com/docs/latest/how_to/building_images.html?utm_campaign=Dockerhub&utm_source=docker
> 如果需要增加sudo权限，需要在dockerfile增加如下配置，https://kasmweb.com/docs/latest/how_to/running_as_root.html?highlight=root

```yml
# ubuntu
RUN apt-get update \
    && apt-get install -y sudo \
    && useradd -m -d /home/kasm-user -s /bin/bash kasm-user \
    && echo 'kasm-user ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers \
    && rm -rf /var/lib/apt/list/*
    
# centos
RUN yum install -y sudo \
    && useradd -m -d /home/kasm-user -s /bin/bash kasm-user \
    && echo 'kasm-user ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers
```
安装后，可以通过命令`sudo su root`切换到root用户，使用`whoami`查看是否切换成功

## adminer(在线数据库管理工具)

```shell
docker pull adminer

docker run -itd -p 8080:8080 adminer
```

## redis

```shell
# 进入redis
docker exec -it redis redis-cli
docker exec -it redis redis-cli --raw
docker exec -it redis redis-cli --raw --pass [password]
# redis默认端口号: 6379
docker run -itd --name testredis -p 16379:6379 redis
```

## pgsql

```shell
# 进入pgsql
docker exec -it --user postgres postgres /bin/bash

# 进入后的链接命令
psql -h 1.2.3.4 -p 1234 -U linlei -W (这个是密码)
psql -U dory -W (这个是密码，不要敲，回车后会提示)
```

## adminer

```shell
docker run -itd -p 15434:8080 --rm --name adminer adminer
```

## vnc

```shell
docker run -itd --rm -p 6080:80 dorowu/ubuntu-desktop-lxde-vnc
```

# harbor

## 安装

```shell
# 下载
wget https://github.com/vmware/harbor/releases/download/v1.1.2/harbor-online-installer-v1.1.2.tgz

# 解压
tar -xzvf harbor-online-installer-v1.1.2.tgz

# 进入到解压的目录
cd harbor

# 修改配置harbor.conf，参考下面备注，修改后，直接./install.sh，另外配置项根据实际注释，安装的时候如果是必须的配置项安装会报错，重新取消注释即可
# 比如我这里默认只修改了hostname和customize_crt修改为false
./install.sh

# 安装后，会在harbor目录下产生common文件，里面有很多配置文件
# 并且会拉取很多image，启动很多容器

# 容器的启动文件是docker-compose.yml，可以对应的修改，比如nginx的端口号被占用，可以修订后在重新install.sh，比如我修订为8112，安装完成后就可以通过ip:8112访问，默认用户名密码是admin/Harbor12345
docker-compose.yml
```

> 配置文件内容大致如下

```
## Configuration file of Harbor

# hostname设置访问地址，可以使用ip、域名，不可以设置为127.0.0.1或localhost
hostname = 192.168.80.42

# 访问协议，默认是http，也可以设置https，如果设置https，则nginx ssl需要设置on
ui_url_protocol = http

# mysql数据库root用户默认密码root123，实际使用时修改下
db_password = root123

max_job_workers = 3 
customize_crt = on
ssl_cert = /data/cert/server.crt
ssl_cert_key = /data/cert/server.key
secretkey_path = /data
admiral_url = NA

# 邮件设置，发送重置密码邮件时使用
email_identity = 
email_server = smtp.mydomain.com
email_server_port = 25
email_username = sample_admin@mydomain.com
email_password = abc
email_from = admin <sample_admin@mydomain.com>
email_ssl = false

# 启动Harbor后，管理员UI登录的密码，默认是Harbor12345
harbor_admin_password = Harbor12345

# 认证方式，这里支持多种认证方式，如LADP、本次存储、数据库认证。默认是db_auth，mysql数据库认证
auth_mode = db_auth

# LDAP认证时配置项
#ldap_url = ldaps://ldap.mydomain.com
#ldap_searchdn = uid=searchuser,ou=people,dc=mydomain,dc=com
#ldap_search_pwd = password
#ldap_basedn = ou=people,dc=mydomain,dc=com
#ldap_filter = (objectClass=person)
#ldap_uid = uid 
#ldap_scope = 3 
#ldap_timeout = 5

# 是否开启自注册
self_registration = on

# Token有效时间，默认30分钟
token_expiration = 30

# 用户创建项目权限控制，默认是everyone（所有人），也可以设置为adminonly（只能管理员）
project_creation_restriction = everyone

verify_remote_cert = on
```

## 配置

## 使用

```shell
# 批量启动harbor容器
docker start `docker ps -a|grep vm | grep Exit |awk '{print $1}'`
```

# docker-compose

```yml
version: "3"
services:
  nginx:
    image: "ningx:latest"
    environment: #-e
      - XYZ=123 #容器内就会有XYZ这个环境变量，比如linux上，可通过$XYZ获取
      - P_HOSTNAME=${HOSTNAME} #把宿主机的HOSTNAME传递给docker容器P_HOSTNAME
      - PASSWD  # 也可以直接使用此方式继承宿主机的环境变量
    volumes:
      - "local_path:docker_path"
    ports:
      - "8080:80" # 把容器内80暴露到外部8080
    command: 
      - /bin/bash
```

## 宿主机环境变量修改后未生效

不管是上面哪种环境变量配置方式，直接使用`stop start`和`restart`均不会生效。也就是宿主机的环境变量变更后，容器内无法使用新的环境变量

```sh
docker stop nginx
docker start nginx
docker restart nginx

docker-compose stop
docker-compose start
docker-compose restart
```

如果是`docker-compose`，需要使用`docker-compose down`和`docker-compose up -d`来使环境变量重新生效。

# Dockerfile

```dockerfile
# docker build -t xxx:tag .(注意最后这个点)
# docker build -t xxx.tag -f xxxfile . (-f参数指定dockerfile名称)

FROM nginx

# 不能直接使用COPY mrtcdemo-key.pem /etc/nginx/cert，否则容器内的cert是mrtcdemo-key.pem这个文件
COPY mrtcdemo-key.pem /etc/nginx/cert/mrtcdemo-key.pem
COPY mrtcdemo.pem /etc/nginx/cert/mrtcdemo.pem

# ADD会自动把压缩文件解压到/usr/share/nginx/html目录下，注意文件路径，比如我的压缩文件里面是一个dist目录，那么index.html
# 会在/usr/share/nginx/html/dist/index.html路径
ADD mrtcdemo.tar.bz2 /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

# 忽略错误继续执行下一步，比如需要使用dpkg安装deb包，但是依赖不存在，需要先使用apt-get安装依赖后继续安装的情况
RUN dpkg -i google-chrome-stable_current_amd64.deb || true
RUN apt-get -y -f install
RUN dpkg -i google-chrome-stable_current_amd64.deb

# 修改工作目录，可以在Dockerfile文件里面多次指定
# 每次指定后都会生效，容器启动后的工作目录以最后一个WORKDIR生效
WORKDIR /opt

# 安装PYTHON
RUN yum install -y make && \
    yum install gcc openssl-devel bzip2-devel libffi-devel -y && \
    curl -O https://www.python.org/ftp/python/3.9.9/Python-3.9.9.tgz && \
    tar -xvf Python-3.9.9.tgz && \
    cd Python-3.9.9 && \
    ./configure --enable-optimizations && \
    make altinstall
RUN rm -rf /usr/bin/python && \
    ln -s /usr/local/bin/python3.9 /usr/bin/python && \
    ln -s /usr/local/bin/pip3.9 /usr/bin/pip && \
    sed 's/\!\/usr\/bin\/python/\!\/usr\/bin\/python2/' -i /usr/bin/yum && \
    sed 's/\!\ \/usr\/bin\/python/\!\/usr\/bin\/python2/' -i /usr/libexec/urlgrabber-ext-down && \
    python3.9 -m pip install -U pip -i https://pypi.tuna.tsinghua.edu.cn/simple/

ENTRYPOINT ["sh" ,"/opt/entrypoint.sh"]
CMD ["scripts/dory_case_demo.py", "--no-statis"]

# 声明一个端口，比如声明tomcat默认暴露的端口是8080
# 实际使用时可以使用-p 8081:8080进行映射，即外部通过8081访问
# 如果外部没有进行端口映射，那么这个8080只在容器内部生效，外部无法访问这个容器
EXPOSE 8080
```

# QA

## docker内部中文显示乱码

在windows上，找到`C:\Windows\Fonts`目录下的微软雅黑，直接复制出来，一般是ttc文件，我们用`msyh.ttc`即可，复制到容器的`/usr/share/fonts`目录下即可

## 报错: standard_init_linux.go:207: exec user process caused "no such file or directory"

一般是容器的ENTRYPOINT脚本不符合linux编码规则，比如\r被替换为了\r\n等不识别的问题导致

我遇到的是容器启动时启动startup.sh，但我自定义了startup.sh并挂在到容器，导致容器启动失败，通过
不挂载启动后拿到容器内部的startup.sh，然后在重新修改为自己的重新挂载启动后则启动成功

## docker容器时间同步

```shell
# 已经运行的容器，3d0ffe2c5b11是容器ID，可以使用date命令验证
docker cp -L /usr/share/zoneinfo/Asia/Shanghai 3d0ffe2c5b11:/etc/localtime
```

> 参考: https://blog.csdn.net/lengyue1084/article/details/114021753

## 执行docker命令提示无权限

找到docker.sock文件，一般在/var/run目录下，查看如果是root docker的权限，需要按照下面的方式修订

1. 如果当前用户有sudo权限，可通过sodo docker执行命令，如果没有则继续下面的步骤
2. `cat /etc/group | grep docker`查看当前登录用户是否在docker组，如果没有或者无docker组，需要按照下面步骤继续
3. 如果没有docker组，则需要先增加docker组，命令为`groupadd docker`
4. `gpasswd -a your_user docker` 把用户添加到docker组
5. `newgrp docker` 更新用户组，重新登录用户即可使用
6. 如果是普通用户，还需要使用`sudo chmod a+rw /var/run/docker.sock`需改权限

## docker挂载后的文件权限为root，宿主机无法删除

在执行`docker run`命令时指定-u参数，比如

```shell
docker run -itd \
  -u $(id -u) \
  -p 5557:5557 \
  -m 300G --oom-kill-disable \
  --cpuset-cpus="0-19" \
```

-u可指定具体的用户名，但是docker容器必须先存在这个用户

## docker login问题

### 登录http私有仓库报错

```shell
# 先查看配置文件，找到类型这一行: Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
systemctl status docker

# 编辑配置文件，找到ExecStart配置项，在最后增加一条配置--insecure-registry=1.2.3.4:8112，这里的端口默认是80，如果是harbor仓库，要和harbor仓库的前端页面端口一致
# 但是通过docker loing 1.2.3.4:8112指定端口号的时候始终报错，最后还是修改nginx为80端口，不指定端口号登录成功了
vi /lib/systemd/system/docker.service

# 重启docker服务
systemctl daemon-reload
systemctl restart docker
```

## windows挂载

1. 需要在setting->resources->file sharing(这里的配置菜单根据具体版本可能有变化)里面配置可挂载目录
2. 挂载的时候，需要指定全路径，比如`c:\users\xml\xxx`这个路径，挂载后是`-v /c/users/xml/xxx:/tmp`，即把盘符的`:`去掉，然后路径使用`/`即可

> 新版本可以直接用路径即可，`docker run --rm -it -v D:\dockermount:/workspace centos /bin/bash`

# 参考

1. [Docker使用Portainer搭建可视化界面](https://www.cnblogs.com/ExMan/p/11657069.html)
2. [完整的docker打包流程](https://www.cnblogs.com/pyweb/p/12751852.html)
3. [Centos7上安装docker](https://www.cnblogs.com/yufeng218/p/8370670.html)
4. [Centos7.6离线安装docker](https://www.cnblogs.com/eastonliu/p/11277014.html)
5. [Docker搭建Harbor私有仓库](https://blog.csdn.net/qq_35959573/article/details/80664353)
6. [Docker登录Harbor私有仓库](https://blog.csdn.net/u013201439/article/details/81271182)