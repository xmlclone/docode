# 本地开发模式

```sh
# 安装依赖
pip install requirements.txt
# 初次安装，先初始化数据库
flask --app demo1 init-db
# 查看帮助
flask --app demo1 --help
# 以debug模式运行，端口号默认是5000，访问: http://127.0.0.1:5000
flask --app demo1 run --debug
# 为creat_app传递参数
flask --app "demo1:create_app('prod')" run --debug

# export FLASK_ENV=production && flask run
```

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