import os
import traceback
import logging.config
import logging.handlers

from pathlib import Path
from flask import has_request_context, request


# cwd 获取的是当前工作区，避免日志存储到 lib 目录下
LOG_PATH = Path().cwd() / 'logs'
# 当然也可以使用下面的方法
# LOG_PATH = os.path.join(os.getcwd(), 'logs')
if not LOG_PATH.exists():
    os.makedirs(LOG_PATH, exist_ok=True)


# 自定义Formatter
class SelfDefFormatter(logging.Formatter):
    def format(self, record):
        # 比如给 flask 增加访问 url 和 remote_addr 属性
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None
        result = super().format(record)
        # 把多行的数据打印到一行
        # 比如：如果有异常，异常数据打印出来会很难看，可以自定义处理一次
        result = result.replace('\n', '|') 
        # if record.exc_text:
        return result
    

def config_logging(
    console_level='INFO',
    convert_newline=True,
):
    # https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'console': {
                # https://docs.python.org/3/library/logging.html#logrecord-attributes
                # asctime 默认格式化 %Y-%m-%d %H:%M:%S,uuu
                # 这里的 uuu 是经过库处理的，而不是可以直接通过 time.strftime 或 datetime.strftime 格式化的
                # 参考： https://github.com/python/cpython/blob/3.12/Lib/logging/__init__.py#L622  formatTime 方法
                'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
            },
            'file': {
                'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
            },
            'selfreq': {
                # 引用自定义格式化类
                # 注意这个类要指定全路径,就算在本文件定义了,也不能直接使用 SelfDefFormatter
                '()': 'logger.SelfDefFormatter',
                'format': '%(asctime)s %(remote_addr)s %(url)s %(levelname)s %(name)s[%(lineno)d] %(message)s',
            },
            'selfreq2': {
                '()': 'logger.SelfDefFormatter' if convert_newline else 'logging.Formatter',
                'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                # 可以自定义 asctime 格式
                'datefmt': "%Y-%m-%d %H:%M:%S"
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'selfreq2',
                'level': console_level,
            },
            'file': {
                # https://docs.python.org/3/library/logging.handlers.html#timedrotatingfilehandler
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': os.path.join(LOG_PATH, 'ccode.log'),
                'when': 'midnight',
                'backupCount': 7,
                'encoding': 'utf-8',
                'formatter': 'selfreq2',
                'level': 'DEBUG',
            },
            "access": {
                # https://docs.python.org/3/library/logging.handlers.html#rotatingfilehandler
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOG_PATH, 'access.log'),
                'maxBytes': 1024 * 1024 * 5, # 5MB 
                'backupCount': 10,
                'encoding': 'utf-8',
                'formatter': 'selfreq',
                'level': 'DEBUG',
            },
        },
        'loggers': {
            'ccode': {
                'handlers': ['file', 'console'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'ccode.xxx': {
                'handlers': ['file', 'console'],
                'level': 'DEBUG',
                'propagate': False,   # 如果设置为 True ，那么会触发父 logger ，也就是可能出现同一条消息打印多次的情况
            },
        },
        'root': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
    })


if __name__ == '__main__':
    config_logging()
    logger = logging.getLogger(__name__)
    logger.debug('This is debug.')
    logger.info('This has \n newline.')
    try:
        1 / 0
    except Exception as e:
        logger.error(e)
        logger.exception(traceback.format_exc())