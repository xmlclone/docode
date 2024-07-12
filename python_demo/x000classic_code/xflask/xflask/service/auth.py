import functools
import logging

from flask import g, session

from ..exception import NeedLogin, AdminRequired
from ..dao import UserDao
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
    def wrap(*args, **kwargs):
        if not is_logged():
            raise NeedLogin()
        return view(*args, **kwargs)
    return wrap


def admin_required(view):
    @functools.wraps(view)
    def wrap(*args, **kwargs):
        if not is_logged():
            raise NeedLogin()
        if not is_admin():
            raise AdminRequired()
        return view(*args, **kwargs)
    return wrap


def is_logged():
    logger.debug(f"{g.user=}")
    return False if g.user is None else True


def is_admin():
    logger.debug(f"{g.user=}, {g.user.role=}")
    return True if is_logged() and (g.user.role == UserRole.admin) else False