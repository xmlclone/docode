import os
import logging
import logging.config
from flask import Flask


def setup_logger(app: Flask):
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'console': {
                'format': '%(asctime)s - %(levelname)s - %(message)s',
            },
            'file': {
                'format': '%(asctime)s - %(levelname)s - %(name)s[%(lineno)d] - %(message)s',
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'console',
                'level': 'INFO',
            },
            'file': {
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': os.path.join(app.instance_path, 'demo1.log'),
                'when': 'midnight',
                'backupCount': 7,
                'encoding': 'utf-8',
                'formatter': 'file',
                'level': 'DEBUG',
            },
        },
        'loggers': {
            'demo1': {
                # 'handlers': ['console'],
                'handlers': ['console', 'file'],
                'level': 'DEBUG',
                'propagate': False,
            },
        }
    })