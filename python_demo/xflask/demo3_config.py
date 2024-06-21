import os

from pathlib import Path
from flask import Flask


app = Flask(__name__)

# app.testing = True
app.config['TESTING'] = True

app.config.update(
    TESTING=True,
    SECRET_KEY='192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
)


# 内置配置变量,后面定义的值是系统默认值
app.config['TESTING'] = False
app.config['DEBUG'] = False
app.config['PROPAGATE_EXCEPTIONS'] = None
app.config['TRAP_HTTP_EXCEPTIONS'] = None
app.config['TRAP_BAD_REQUEST_ERRORS'] = None
app.config['SECRET_KEY'] = None
app.config['SESSION_COOKIE_NAME'] = 'session'
app.config['SESSION_COOKIE_DOMAIN'] = None
app.config['SESSION_COOKIE_PATH'] = None
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SECURE'] = False
app.config['SESSION_COOKIE_SAMESITE'] = None


# 推荐的配置方式如下
# 运行方式
# 默认运行方式:       flask --app xctools run --debug
# 指定环境(比如prod): flask --app "your_app:create_app('prod')" run --debug
def create_app(config_name='default'):
    app = Flask(__name__, instance_relative_config=True, instance_path=Path('.').absolute() / 'instance') # type:ignore

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