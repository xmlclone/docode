from flask import Flask
from flask import abort, render_template
from werkzeug.exceptions import HTTPException, NotFound, BadRequest

'''
flask --app demo1_exception_abort run --debug
'''


# 400-499 表示客户端请求数据或与之关联的错误
# 500-599 表示服务器或与之关联的错误
# werkzeug 已经定义了标准的异常类


app = Flask(__name__)


@app.route('/')
def index():
    return "Index page."

@app.route('/400')
def r_400():
    abort(400)

@app.route('/404')
def r_404():
    abort(404)

@app.route('/507')
def r_507():
    # abort(507) 这里也不能直接 abort() 一个非标准的 http code,只能通过raise的方式抛出异常
    raise UserDefineException()


# 自定义异常
class UserDefineException(HTTPException):
    code = 507
    description = 'Not enough storage space.'


# 注册方式一： 直接使用异常 code
@app.errorhandler(400)
def handler_400(e):
    return f"handler_400: {e}", 400

# 注册方式二: 使用 werkzeug 定义的标准异常类
@app.errorhandler(NotFound)
def handler_404(e):
    return render_template('404.html'), 404

# 注册方式三，并演示自定义异常的处理
def handler_507(e):
    return f"handler_507: {e}", 404
# 注意这里不能直接定义 app.register_error_handler(507) ,使用 code 的方式,必须要是标准的 http code ,否则只能是 HTTPException 的子类
app.register_error_handler(UserDefineException, handler_507)


