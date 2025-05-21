请帮忙用python的flask搭建一个简单的论坛交流网站，网站的基本功能如下：
1. 所有页面都需要经过登录认证通过后才能访问
1. 角色分为管理员和普通用户，管理员具备所有权限，普通角色只能访问和管理被赋予的权限
2. 论坛可以发帖、回复等基本的论坛功能

技术需求：
1. 需要使用数据库技术，后端数据库是postgresql，请使用python的sqlachemy库交互
2. 需要有详细的后端日志记录
3. 请将代码合理划分模块，方便多人协作开发、管理与维护


```sh
export FLASK_ENV=production && flask run
flask init-db
flask run
```

python-dotenv: https://juejin.cn/post/7473396397519667200