"""
flask 的日志就是 app.logger, 使用的是标准的 python logging 模块
比如: app.logger.info("xxx")

如果要配置日志,就应该尽早配置
"""

import os
import logging.handlers
import logging.config

from flask import Flask, has_request_context, request
from flask.logging import default_handler

logfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'demo.log')
print(logfile)


# 注入请求信息
class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None
        return super().format(record)
    

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(asctime)s %(levelname)s %(message)s',
        },
        'file': {
            '()': 'demo2_logger.RequestFormatter', # 注意这个类要指定全路径,就算在本文件定义了,也不能直接使用 RequestFormatter
            'format': '%(asctime)s %(remote_addr)s %(url)s %(levelname)s %(name)s[%(lineno)d] %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
            'level': 'INFO',
        },
        'file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': logfile,
            'when': 'midnight',
            'backupCount': 7,
            'encoding': 'utf-8',
            'formatter': 'file',
            'level': 'DEBUG',
        },
    },
    'loggers': {
        'demo2_logger': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'DEBUG',
    },
})

# logger的名称就是 app.name
# 比如本例就是 demo2_logger
# 还有一个 werkzeug logger
# 其它的,比如 sqlalchemy 等
app = Flask(__name__)


# 还可以移除默认的配置
app.logger.removeHandler(default_handler)


@app.route('/')
def index():
    app.logger.error(f"index: {app.name}")
    return "Index"