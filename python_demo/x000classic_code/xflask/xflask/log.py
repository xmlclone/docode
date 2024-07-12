import os
import logging
import logging.config

from flask import has_request_context, request


class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None
        return super().format(record)


def config_logger():
    CWD_PATH = os.getcwd()
    LOG_PATH = os.path.join(CWD_PATH, 'logs')
    try:
        os.makedirs(LOG_PATH)
    except:
        pass
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'console': {
                '()': 'xflask.log.RequestFormatter', # 注意这个类要指定全路径,就算在本文件定义了,也不能直接使用 RequestFormatter
                'format': '%(asctime)s %(remote_addr)s %(url)s %(levelname)s %(name)s[%(lineno)d] %(message)s',
            },
            'file': {
                '()': 'xflask.log.RequestFormatter', # 注意这个类要指定全路径,就算在本文件定义了,也不能直接使用 RequestFormatter
                'format': '%(asctime)s %(remote_addr)s %(url)s %(levelname)s %(name)s.%(funcName)s[%(lineno)d] %(message)s',
            },
            'pure': {
                'format': '%(asctime)s %(levelname)s %(name)s[%(lineno)d] %(message)s',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'console',
                # 'level': 'INFO',
                'level': 'DEBUG',
            },
            # 'xflask': {
            #     'class': 'logging.handlers.TimedRotatingFileHandler',
            #     'filename': os.path.join(LOG_PATH, 'xflask.log'),
            #     'when': 'midnight',
            #     'backupCount': 7,
            #     'encoding': 'utf-8',
            #     'formatter': 'file',
            #     'level': 'DEBUG',
            # },
            'xflask': {
                'class': 'logging.FileHandler',
                'filename': os.path.join(LOG_PATH, 'xflask.log'),
                'mode': 'w',
                'encoding': 'utf-8',
                'formatter': 'file',
                'level': 'DEBUG',
            },
            'root': {
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': os.path.join(LOG_PATH, 'root.log'),
                'when': 'midnight',
                'backupCount': 7,
                'encoding': 'utf-8',
                'formatter': 'file',
                'level': 'DEBUG',
            },
            'waitress': {
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': os.path.join(LOG_PATH, 'waitress.log'),
                'when': 'midnight',
                'backupCount': 7,
                'encoding': 'utf-8',
                'formatter': 'file',
                'level': 'DEBUG',
            },
            # 'sqlalchemy': {
            #     'class': 'logging.handlers.TimedRotatingFileHandler',
            #     'filename': os.path.join(LOG_PATH, 'sqlalchemy.log'),
            #     'when': 'midnight',
            #     'backupCount': 7,
            #     'encoding': 'utf-8',
            #     'formatter': 'pure',
            #     'level': 'DEBUG',
            # },
            'sqlalchemy': {
                'class': 'logging.FileHandler',
                'filename': os.path.join(LOG_PATH, 'sqlalchemy.log'),
                'mode': 'w',
                'encoding': 'utf-8',
                'formatter': 'file',
                'level': 'DEBUG',
            },
            'werkzeug': {
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': os.path.join(LOG_PATH, 'werkzeug.log'),
                'when': 'midnight',
                'backupCount': 7,
                'encoding': 'utf-8',
                'formatter': 'pure',
                'level': 'DEBUG',
            },
        },
        'loggers': {
            'xflask': {
                'handlers': ['xflask', 'console'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'waitress': {
                'handlers': ['waitress', 'console'],
                'level': 'DEBUG',
                'propagate': False,
            },
            # sqlalchemy 这个 logger 会输出其它额外信息，但一般用不到，主要还是看 engine
            'sqlalchemy.engine': {
                'handlers': ['sqlalchemy'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'werkzeug': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': False,
            },
        },
        'root': {
            'handlers': ['console', 'root'],
            'level': 'DEBUG',
        },
    })