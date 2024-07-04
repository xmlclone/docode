import functools
import logging

from flask import g, redirect, Flask, request, session
from werkzeug.exceptions import Forbidden

from .wrap_response import make_response
from .exception import LoginFailed, NeedLogin
from .dao import UserDao


logger = logging.getLogger(__name__)


def init_app(app: Flask):
    app.add_url_rule('/api/login', 'login', login, methods=['POST'])
    app.add_url_rule('/api/logout', 'logout', logout, methods=['POST'])
    app.before_request(load_user)


def load_user():
    logger.debug('befor_request: load_user.')
    user = session.get('user')
    logger.debug(f"{user=}")
    g.user = None if user is None else UserDao().get(user)
    logger.debug(f"{g.user=}")


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


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs):
        if g.user is None:
            raise NeedLogin()
        return view(*args, **kwargs)
    return wrapped_view