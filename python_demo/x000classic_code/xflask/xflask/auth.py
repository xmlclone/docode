import functools
import logging

from flask import g, redirect, Flask, request, session
from werkzeug.exceptions import Forbidden

from .wrap_response import make_response
from .exception import LoginFailed


logger = logging.getLogger(__name__)


def init_app(app: Flask):
    app.add_url_rule('/login', 'login', login, methods=['POST'])
    app.add_url_rule('/logout', 'logout', logout, methods=['POST'])
    app.before_request(load_user)


def load_user():
    user = session.get('user')
    if user is None:
        g.user = None
    else:
        g.user = user
    logger.debug(f"{user=}")


def login():
    if not request.json:
        raise LoginFailed()
    username = request.json.get('username', None)
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
    def wrapped_view(**kwargs):
        if g.user is None:
            raise Forbidden()
        return view(**kwargs)
    return wrapped_view