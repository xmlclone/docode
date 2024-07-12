import logging

from flask import request, session

from ..wrap_response import make_response
from ..exception import LoginFailed
from ..service import UserService


logger = logging.getLogger(__name__)


def login():
    if (not request.is_json) or (not request.json):
        raise LoginFailed(description='request data is error.')
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    logger.debug(f"{username=}, {password=}")
    if not username or not password:
        raise LoginFailed(description='username or password is none.')
    user = UserService().check_username_password(username, password)
    logger.debug(f"{user=}")
    if not user:
        raise LoginFailed(description='username or password error, or user is disabled.')
    session.clear()
    session['user'] = user.id
    logger.debug(f'login success: {username}')
    return make_response()


def logout():
    session.clear()
    return make_response()