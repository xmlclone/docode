# 基本命令

```sh
# 查看帮助
# 如果app在文件app.py或wsgi.py里面，则不需要--app
flask --app demo1 --help

# 以debug模式运行，端口号默认是5000，访问: http://127.0.0.1:5000
flask --app demo1 run --debug

# 为creat_app传递参数
flask --app "demo1:create_app('prod')" run --debug
```

# demo分类

- demo1: 基础能力
- demo2: Bootstrap ElementUI
- 数据库分页
- restfulapi
- 前端技术
- 线上部署

# 数据库操作

## sqlite3

```sql
.tables
.schema tablename # 注意不要有;
```

# 参考文档

- [flask](https://dormousehole.readthedocs.io/en/latest/)
- [flask-apis](https://dormousehole.readthedocs.io/en/latest/api.html)
- [flask-login](https://flask-login-cn.readthedocs.io/zh/latest/)
- [flask-login-应用介绍](https://blog.csdn.net/be_racle/article/details/128081618)
- [flask-sqlalchemy](https://docs.jinkan.org/docs/flask-sqlalchemy/)
- [flask-sqlalchemy-apis](https://docs.jinkan.org/docs/flask-sqlalchemy/api.html)
- [flask-wtf](https://docs.jinkan.org/docs/flask-wtf/index.html)
- [flask-form-应用介绍](https://cloud.tencent.com/developer/article/1574765)