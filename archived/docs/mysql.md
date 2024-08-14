# 主备模式

使用docker创建两个容器演示

```sh
docker pull mysql

docker network create --driver bridge --subnet=172.18.0.0/16 --gateway=172.18.0.1 mysql

# test(默认用户名是root)
# # 启动一个服务
docker run --rm -itd --network mysql --ip 172.18.0.2 -e MYSQL_ROOT_PASSWORD=123456 -v3306:3306 mysql
# # 链接到服务
docker run -it --network mysql --rm mysql mysql -h172.18.0.2 -uroot -p


docker run --name some-mysql -v /my/custom:/etc/mysql/conf.d -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:tag
```

## 配置

## 以下是默认的配置

```conf
[mysqld]
host-cache-size=0
skip-name-resolve
datadir=/var/lib/mysql
socket=/var/run/mysqld/mysqld.sock
secure-file-priv=/var/lib/mysql-files
user=mysql
pid-file=/var/run/mysqld/mysqld.pid

[client]
socket=/var/run/mysqld/mysqld.sock

!includedir /etc/mysql/conf.d/
```

## Master配置

```conf
[mysqld]
host-cache-size=0
skip-name-resolve
datadir=/var/lib/mysql
socket=/var/run/mysqld/mysqld.sock
secure-file-priv=/var/lib/mysql-files
user=mysql
pid-file=/var/run/mysqld/mysqld.pid
# 新增以下内容
# 服务器标识，每个服务器要不一样
server-id=1
log-bin=mysql-bin

[client]
socket=/var/run/mysqld/mysqld.sock

!includedir /etc/mysql/conf.d/
```

# 常用命令

```sh
# 链接数据库
mysql -h172.18.0.2 -uroot -p

# 显示数据库
SHOW DATABASES;

# 创建数据库
CREATE DATABASE database_name;

# 选择数据库
USE database_name;

# 显示表
SHOW TABLES;

# 显示表结构
DESCRIBE table_name;
```

# 代码

可参考`python_demo/xdatabase/xmysql`下相关示例代码