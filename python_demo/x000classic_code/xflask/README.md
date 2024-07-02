# 常用命令

```sh
# 查看帮助
flask --app xflask --help

# 默认启动(勿部署生产)
flask --app xflask run --debug

# 初始化数据库
flask --app xflask test-init-db

# 已某个配置启动
flask --app "xflask:create_app('prod')" run --debug

# 启动端口
xflask run-server -p 80

# 服务器部署
pip install waitress
waitress-serve --call "xflask:create_app"

# 服务器部署2
flask --app "xflask:create_app('prod')" test-init-db
nohup xflask run-server &
nohup xflask run-server -p 80 &
```

# 数据库

```sh
# 连接数据库
sqlite3 xflask.db

# 查看有哪些表
.tables

# 查看所有表结构
.scheme

# 查看某个具体的表结构
.schema tablename
```