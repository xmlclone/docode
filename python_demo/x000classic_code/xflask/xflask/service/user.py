import logging

from werkzeug.security import check_password_hash

from .base import Service
from ..dao import UserDao
from ..model import UserPy


logger = logging.getLogger(__name__)


class UserService(Service):
    def __init__(self) -> None:
        self.dao: UserDao = UserDao()
        self.pymodel = UserPy

    def check_username_password(self, username: str, password):
        item = self.dao.get_with_full_name(username)
        if not item:
            return False
        if not check_password_hash(item.password, password):
            return False
        return item