import functools
import logging

from flask import g, redirect, Flask, request, session
from werkzeug.exceptions import Forbidden

from ..wrap_response import make_response
from ..exception import LoginFailed, NeedLogin
from ..dao import UserDao
from ..model import UserPy
from ..constant import UserRole


logger = logging.getLogger(__name__)


def login():
    if (not request.is_json) or (not request.json):
        raise LoginFailed(description='request data is error.')
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    logger.debug(f"{username=}, {password=}")
    if not username or not password:
        raise LoginFailed(description='username or password is none.')
    user = UserDao().check_username_password(username, password)
    if not user:
        raise LoginFailed(description='username or password error.')
    session.clear()
    session['user'] = user.id
    logger.debug(f'login success: {username}')
    return make_response()


def logout():
    session.clear()
    return make_response()