import logging
import logging.config


'''简化版的日志配置
import logging

# 输出到控制台
logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.DEBUG)
# 输出到文件
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s')

logging.debug("test")
'''

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)s %(name)s[%(lineno)d]:  %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'level': 'DEBUG',
        },
    },
    'loggers': {
        'mrtc': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
})


# __name__不仅可以在模块(也就是文件级别)，还是用到类级别
logger = logging.getLogger(__name__)