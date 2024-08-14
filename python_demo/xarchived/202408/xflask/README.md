[toc]

https://dormousehole.readthedocs.io/en/latest/index.html

# 命令行

```sh
# 执行命令

# 如果只有单个文件
flask --app hello run --debug

# 如果这个文件是 app.py 或 wsgi.py ，则不要指定 --app 也可运行

flask --app hello run --host 0.0.0.0 --port 80


python -c 'import secrets; print(secrets.token_hex())'
```

# 常用函数

这里只列举一些常用的，更多示例可以参考对应的`demo` code.

```python
# 常用函数

from markupsafe import escape


# file = request.files['the_file']
# file.save(f"/var/www/uploads/{secure_filename(file.filename)}")
from werkzeug.utils import secure_filename


# url_for('login')
# url_for('login', next='/')  login?next=/
# url_for('login', username='John Doe')  login/John%20Doe
# url_for('static', filename='style.css')
# url_for 还有一定的额外的参数
# _external=True, 可以生成全部的 url 地址，否则只有路径
# 更多可参考 demo5_url_for.py
from flask import url_for


# request.method == 'POST'
# request.form['username']
# request.args.get('key', '')   url里面具有 ?key=value的情形
# request.cookies.get('username')
# 获取远程访问的对象，可参考 demo2_logger.py 和 demo4_signal.py 记录远程访问信息
# request.remote_addr
# request.path
# request.method
# request.status_code
from flask import request


# resp = make_response(render_template(...))
# resp.set_cookie('username', 'the username')
# return resp
from flask import make_response


# session['username'] = request.form['username']
# if 'username' in session:
#     return f'Logged in as {session["username"]}'
# session.pop('username', None)
from flask import session


# render_template('hello.html', name=name)
from flask import render_template


# return redirect(url_for('login'))
# abort(401)
# abort(403)
# abort(404, f"Post id {id} doesn't exist.")
from flask import abort, redirect

# 修改默认的异常响应
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return 'bad request!', 400

# 另外一种注册方式
app.register_error_handler(400, handle_bad_request)


# if 'db' not in g:
#     g.db = xxx
# db = g.pop('db', None)
from flask import current_app, g


# app.cli.add_command(init_db_command)
@click.command('init-db')
def init_db_command():
    ...


# bp = Blueprint('auth', __name__, url_prefix='/auth')
# @bp.route('/register', methods=('GET', 'POST'))
# app.register_blueprint(auth.bp)
# url_for('auth.register')
from flask import Blueprint


# 路由参数
@app.route('/path/<path:subpath>')
@app.route('/post/<int:post_id>')
@app.route('/user/<username>') # 默认是string类型

# 请求方法
@app.route('/login', methods=['GET', 'POST'])
@app.get('/login')
@app.post('/login')

# 显示添加路由
app.add_url_rule('/', endpoint='index', view_func=xxx_func, methods=['POST', 'GET'])
```


# 关于响应

1. 所有视图的返回，都会被转换为一个`响应对象`，也就是 `make_response` 包装后的对象
2. 每个视图函数可以返回`一个值`或`元组`, `元组`的值可以是 `(response, status, headers)` 或 `(response, status)` 或 `(response, headers)`

# 工厂函数

```python
# 一般在项目的 __init__.py文件内定义

import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
```

另外一种方式

```python

# 运行方式
# 默认运行方式:       flask --app xctools run --debug
# 指定环境(比如prod): flask --app "your_app:create_app('prod')" run --debug

def create_app(config_name='default'):
    app = Flask(__name__, instance_relative_config=True, instance_path=Path('.').absolute() / 'instance')

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # 所有配置文件应该在 instance 文件夹下提供
    if config_name == 'prod':
        app.config.from_pyfile('config_prod.py')
    elif config_name == 'test':
        app.config.from_pyfile('config_test.py')
    elif config_name == 'dev':
        app.config.from_pyfile('config_dev.py')
    else:
        app.config.from_pyfile('config.py')
    

    return app
```

# 模板

`flaskr/templates/base.html`

```html
<!doctype html>
<title>{% block title %}{% endblock %} - Flaskr</title>
<!-- 注意这里引用了一个 css 文件，下面会描述这个文件的位置和内容 -->
<!-- 其实所有静态文件都可以放置到 static 目录下，通过此方式引用 -->
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
<nav>
  <h1>Flaskr</h1>
  <ul>
    {% if g.user %}
      <li><span>{{ g.user['username'] }}</span>
      <li><a href="{{ url_for('auth.logout') }}">Log Out</a>
    {% else %}
      <li><a href="{{ url_for('auth.register') }}">Register</a>
      <li><a href="{{ url_for('auth.login') }}">Log In</a>
    {% endif %}
  </ul>
</nav>
<section class="content">
  <header>
    {% block header %}{% endblock %}
  </header>
  <!-- 配合 flask.flash 函数使用 -->
  {% for message in get_flashed_messages() %}
    <div class="flash">{{ message }}</div>
  {% endfor %}
  {% block content %}{% endblock %}
</section>
```

`flaskr/templates/auth/register.html`

```html
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Register{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="username">Username</label>
    <input name="username" id="username" required>
    <label for="password">Password</label>
    <input type="password" name="password" id="password" required>
    <input type="submit" value="Register">
  </form>
{% endblock %}
```

`flaskr/static/style.css`

```css
html { font-family: sans-serif; background: #eee; padding: 1rem; }
body { max-width: 960px; margin: 0 auto; background: white; }
h1 { font-family: serif; color: #377ba8; margin: 1rem 0; }
a { color: #377ba8; }
hr { border: none; border-top: 1px solid lightgray; }
```