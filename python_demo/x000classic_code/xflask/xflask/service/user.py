import logging

from typing import Dict
from flask import request
from flask.views import MethodView
from sqlalchemy import select
from werkzeug.security import check_password_hash

from .base import Base
from ..wrap_response import make_response
from ..constant import ResponseStatus
from ..dao import UserDao
from ..exception import AddObjectError


logger = logging.getLogger(__name__)


class User(Base):
    def __init__(self) -> None:
        self.dao: UserDao = UserDao()

    def check_username_password(self, username: str, password):
        item = self.dao.get_with_full_name(username)
        if not item:
            return False
        if not check_password_hash(item.password, password):
            return False
        return item