from typing import cast
from flask import Flask, json, make_response, Response
from flask import abort
from werkzeug.exceptions import HTTPException, NotFound, BadRequest

'''
flask --app demo1_exception_common run --debug
'''


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

@app.route('/app_error')
def r_app_error():
    return str(1 / 0)


# 可以注册一个通用的异常处理,然后返回 json 给到客户端
@app.errorhandler(HTTPException)
def handle_http_exception(e: HTTPException):
    response = cast(Response, e.get_response())
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description
    })
    response.content_type = "application/json"
    return response


# 还可以处理程序里面非 http 的异常
@app.errorhandler(Exception)
def handle_exception(e: Exception):
    response = make_response()
    response.status_code = 200
    response.data = json.dumps({
        "code": 800,
        "name": e.__class__.__name__,
        "description": str(e)
    })
    response.content_type = "application/json"
    return response
