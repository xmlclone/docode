import logging

from typing import Dict
from flask import request
from flask.views import MethodView

from .base import BaseItem, BaseGroup
from ..wrap_response import make_response
from ..constant import ResponseStatus
from ..dao import UserDao
from ..exception import AddObjectError


logger = logging.getLogger(__name__)


class UserItem(BaseItem):
    def __init__(self):
        self.dao = UserDao()


class UserGroup(BaseGroup):
    def __init__(self):
        self.dao = UserDao()