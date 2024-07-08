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


def load_user():
    logger.debug('befor_request: load_user.')
    user = session.get('user')
    logger.debug(f"{user=}")
    if user:
        try: user = UserDao().get(user)
        except: user = None
    else:
        user = None
    g.user = user
    logger.debug(f"{g.user=}")


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs):
        if g.user is None:
            raise NeedLogin()
        return view(*args, **kwargs)
    return wrapped_view


def is_admin(user: UserPy):
    if not user:
        return False
    if user.role == UserRole.admin:
        return True
    return False


def login_user_is_admin():
    user: UserPy = g.user
    return is_admin(user)