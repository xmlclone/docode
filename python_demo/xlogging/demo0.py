import logging.config
import os


LOG_PATH = os.getcwd()


# 其它地方可以直接通过下面代码使用
# import logging
# logger = logging.getLogger(__name__)
# logger.debug("some debug message")
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            # https://docs.python.org/3/library/logging.html#logrecord-attributes
            'format': '%(asctime)s %(levelname)s %(message)s',
        },
        'file': {
            'format': '%(asctime)s %(levelname)s %(name)s[%(lineno)d] %(message)s',
        },
        'pure': {
            'format': '%(message)s',
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
            'filename': os.path.join(LOG_PATH, 'ai.log'),
            'when': 'midnight',
            'backupCount': 7,
            'encoding': 'utf-8',
            'formatter': 'file',
            'level': 'DEBUG',
        },
        'pure_file': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_PATH, 'pure.log'),
            'encoding': 'utf-8',
            'formatter': 'file',
            'level': 'DEBUG',
            'mode': 'a',
        }
    },
    'loggers': {
        'MGTestGroupAIAnalysis': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'pure': {
            'handlers': ['pure_file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },

    # 如果某个库，有自己的执行命令行，比如robot，那么可以用上面的logger
    # 但如果某个库是被python -m 的方式执行的，那么logging.getLogger(__name__)获取到的就是__main__这个logger，无法使用上面的logger
    # 所以这里需要配置root的logger
    'root': {
        'handlers': ['console', 'file'],
        'level': 'DEBUG',
    },
})