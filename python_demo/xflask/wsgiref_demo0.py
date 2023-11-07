# 本文参考: http://wsgi.tutorial.codepoint.net/intro

import typing
from wsgiref.simple_server import make_server


HttpStatus = str
HeaderName = HeaderValue = str
HttpHeaders = typing.List[typing.Tuple[HeaderName, HeaderValue]]
ResponseBody = typing.List[str]


'''
问题:

1. cookies session如何处理
2. environ可以获取到完整的url吗
3. 如何获取请求体，form表单
'''


# 这个相当于我们的应用程序，应用程序符合一定的规则就可以和服务器(from wsgiref.simple_server import make_server)进行交互
# 需要两个位置参数
def application(
    # 第一个参数是一个字典类型
    # 一些常用的属性
    # REQUEST_METHOD: GET
    # QUERY_STRING: url里面的查询参数，即url ?后所有字符，并没有进行解析
    # REMOTE_ADDR: 127.0.0.1
    # PATH_INFO: url路径，不包含前面的域名等
    # HTTP_HOST: 127.0.0.1:8051
    # HTTP_COOKIE: tc=tcv; c1=v1; c2=v2
    # SERVER_PORT: 8051
    # wsgi.url_scheme: http
    environ: typing.Dict[str, str],
    # 第二个参数是一个函数
    # 此函数接收两个参数
    # 第一个参数是http状态码和消息
    # 第二个参数是http响应头
    start_response: typing.Callable[[HttpStatus, HttpHeaders], typing.Any]
) -> ResponseBody:
    # response_body = 'Hello, world!'
    response_body = [f'<p>{k}: {v}</p>' for k, v in environ.items()]
    response_body = ' '.join(response_body)
    status = '200 OK'

    # 额外的响应信息
    extra_response = 'Start*****************************'
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body) + len(extra_response))),
        ('Set-Cookie', 'c1=v1'),
        # 可以设置内容有path,domain,expire,max-age(这个是秒为单位),secure(True表示后续只能通过https发送),httponly(true表示只能传输使用，不能通过Js获取，可有效放置XSS)
        # expire和max-age设置1个即可，其实设置了max-age也会转换为expire，expire需要符合一定格式: Tue, 11 Oct 2022 02:17:56 GMT
        ('Set-Cookie', 'c2=v2;path=/abc;max-age=100'),
    ]
    start_response(status, response_headers)
    # extra_response一样会在同一个响应中展现
    return [extra_response.encode(), response_body.encode(), ]


# 这个相当于是服务器(一个简单的http服务器实现)
httpd = make_server(
    'localhost',
    8051,
    application
)
# 只能处理一次请求，处理后自动结束
httpd.handle_request()