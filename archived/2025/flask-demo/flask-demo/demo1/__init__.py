from flask import Flask
from flask import (
    render_template,
    make_response,
    redirect,
    abort,
    jsonify,
    has_request_context
)
# 以下对象可以在html模版内直接使用
from flask import (
    url_for,
    request,
    get_flashed_messages,
    config,
    session,
    g
)
from markupsafe import escape, Markup
from werkzeug.exceptions import HTTPException, NotFound
# 日志相关
import logging
from flask.logging import default_handler
from logging.config import dictConfig


# ===================================================================
# 日志的配置应该尽早

class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None
        return super().format(record)

dictConfig({
    'version': 1,
    'formatters': {
        'werkzeug': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        },
        'app': {
            # 访问了自定义的formatter，注意这里引入的路径一定要是全路径
            'class': 'demo1.RequestFormatter',
            'format': '[%(asctime)s] %(levelname)s %(remote_addr)s %(url)s: %(message)s',
        }
    },
    'handlers': {
        'werkzeug': {
            'class': 'logging.StreamHandler',
            'formatter': 'werkzeug'
        },
        'app': {
            'class': 'logging.StreamHandler',
            'formatter': 'app'
        }
    },
    'loggers': {
        # 常见的logger有 app本身（即app name）
        # werkzeug
        # sqlalchemy
        'demo1': {
            'handlers': ['app'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['werkzeug']
    }
})
# app.logger.removeHandler(default_handler)
# app.logger.addHandler()


app = Flask(__name__)
# 生成一个好的秘钥： python -c 'import secrets; print(secrets.token_hex())'
app.secret_key = 'test'


# ===================================================================
# http://127.0.0.1:5000
@app.route('/')
def index():
    app.logger.info('This is info log.')
    return 'index'

# http://127.0.0.1:5000/user/xiaoming
@app.route('/user/<username>')
def show_user_profile(username):
    return username

# http://127.0.0.1:5000/post/1
# string, int, float, path, uuid
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post ID: {post_id}'

# ===================================================================
# http://127.0.0.1:5000/login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # request.form['username']
        # request.files['file']
        return 'POST'
    if request.method == 'GET':
        return 'GET'

# http://127.0.0.1:5000/login1
# 也可以直接定义 @app.get 和 @app.post
@app.get('/login1')
def login1_get():
    return 'GET'
@app.post('/login1')
def login1_post():
    return 'POST'

# ===================================================================
# http://127.0.0.1:5000/hello
# http://127.0.0.1:5000/hello/xiaoming
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)

# ===================================================================
# http://127.0.0.1:5000/search?key=value
@app.route('/search')
def search():
    return request.args.get('key', 'search key is?')

# http://127.0.0.1:5000/post_form
@app.route('/post_form', methods=['GET', 'POST'])
def post_form():
    if request.method == 'GET':
        return render_template('post_form.html')
    else:
        # 注意绑定（获取）到的是表单的 name 字段，而不是 id
        return request.form['form_filed1']

# ===================================================================
# http://127.0.0.1:5000/set_cookie
@app.route('/set_cookie')
def set_cookie():
    resp = make_response('set_cookie')
    resp.set_cookie('name1', 'value1')
    return resp
# http://127.0.0.1:5000/get_cookie
@app.route('/get_cookie')
def get_cookies():
    return request.cookies

# ===================================================================
# 提前设置 secret_key
# http://127.0.0.1:5000/set_session
@app.route('/set_session')
def set_session():
    session['username'] = 'xiaoming'
    return 'set session'
# http://127.0.0.1:5000/get_session
@app.route('/get_session')
def get_session():
    if 'username' in session:
        return session['username']
    else:
        return 'username not in session'
# http://127.0.0.1:5000/pop_session
@app.route('/pop_session')
def pop_session():
    session.pop('username', None)
    return 'pop session'

# ===================================================================
# http://127.0.0.1:5000/redirect
@app.route('/redirect')
def redirect_demo():
    return redirect(url_for('index'))

# ===================================================================
# http://127.0.0.1:5000/abort
@app.route('/abort')
def abort_demo():
    # 会返回默认的 401 页面，即如下信息
    # Unauthorized
    # The server could not verify that you are authorized to access the URL requested. You either supplied the wrong credentials (e.g. a bad password), or your browser doesn't understand how to supply the credentials required.
    abort(401)

# ===================================================================
# 可以定义自己的异常处理回调
@app.errorhandler(401)
def error_401(error):
    # 应当由 (response, status) 、(response, headers) 或者 (response, status, headers) 组成
    # 后面的401代码，可以不设定，那么默认返回的是200
    # 这里设定了401后，前端抓包可以看见401错误，否则无法看见401错误
    return render_template('401.html'), 401
    # 也可以通过下面的方式进行包装
    # resp = make_response(render_template('error.html'), 404)
    # resp.headers['X-Something'] = 'A value'
    # return resp
# http://127.0.0.1:5000/401
@app.route('/401')
def test_userdefine_401():
    abort(401)

# 另外一种异常注册方式
# http://127.0.0.1:5000/404
def error_404(error):
    return render_template('404.html')
# 这里NotFound也可以直接用404数字替代
app.register_error_handler(NotFound, error_404)
@app.route('/404')
def test_userdefine_404():
    abort(404)

# 也可以自定义个异常
# TODO: 这个暂时没跑起来，有异常
class InsufficientStorage(HTTPException):
    code = 507
    description = 'Not enough storage space.'
def error_507(error):
    return render_template('507.html')
app.register_error_handler(InsufficientStorage, error_507)
# http://127.0.0.1:5000/507
@app.route('/507')
def test_userdefine_507():
    abort(507)

# TODO: 这个暂时没跑起来，有异常
# 定义一个http通用异常处理
@app.errorhandler(HTTPException)
def handel_httpexception(e: HTTPException):
    print('handel_httpexception')
    resp = e.get_response()
    resp.data = {
        "code": e.code,
        "name": e.name,
        "desc": e.description
    }
    resp.content_type = 'application/json'
    return resp
# http://127.0.0.1:5000/402
@app.route('/402')
def test_userdefine_402():
    abort(402)

# 定义一个python通用异常处理
@app.errorhandler(Exception)
def handel_exception(e: Exception):
    if isinstance(e, HTTPException):
        return e
    return render_template('500_generic.html', e=e), 500
# http://127.0.0.1:5000/division_zero_error
@app.route('/division_zero_error')
def division_zero_error():
    return 1 / 0

# ===================================================================
with app.test_request_context():
    print(url_for('index'))
    print(url_for('show_user_profile', username='John Doe'))
    # TODO: app.get app.post 情况下 url_for 应该如何获取？
    print(url_for('login1_get'))
    print(url_for('static', filename='style.css'))


with app.test_request_context('/login', method='POST'):
    print(f'Request method is: {request.method}')
    




