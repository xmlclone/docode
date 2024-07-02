import logging

from flask import Flask

from .base import db
# 这里必须要引入对应的 db.Model 的子类，命令: flask --app xflask test-init-db 才可以成功创建和删除表
# https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/models/#defining-models
from .user import UserDB, UserPy


__all__ = [
    'db',
    'init_app',
    'UserDB',
    'UserPy'
]


logger = logging.getLogger(__name__)

def init_app(app: Flask):
   logger.debug("model init app.")
   db.init_app(app)