import functools
import logging

from flask import g, redirect, Flask, request, session
from werkzeug.exceptions import Forbidden

from .wrap_response import make_response
from .exception import LoginFailed, NeedLogin


logger = logging.getLogger(__name__)


def init_app(app: Flask):
    app.add_url_rule('/login', 'login', login, methods=['POST'])
    app.add_url_rule('/logout', 'logout', logout, methods=['POST'])
    app.before_request(load_user)


def load_user():
    logger.debug('befor_request: load_user.')
    user = session.get('user')
    g.user = None if user is None else user
    logger.debug(f"{g.user=}")


def login():
    if (not request.is_json) or (not request.json):
        raise LoginFailed()
    username = request.json.get('username', None)
    logger.debug(f"{username=}")
    if not username:
        raise LoginFailed()
    session.clear()
    session['user'] = username
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