import logging

from typing import Union, Dict, List
from sqlalchemy import select
from werkzeug.security import check_password_hash

from .base import Dao
from ..model.user import UserDB
from ..model.user import UserPy
from ..model import db


logger = logging.getLogger(__name__)


class UserDao(Dao):
    def __init__(self):
        super().__init__(UserDB, UserPy)
        self.db_model = UserDB
        self.py_model = UserPy

    def check_username_password(self, username: str, password):
        stmt = select(self.db_model).where(self.db_model.full_name==username)
        item = db.session.scalars(stmt).first()
        logger.debug(f'{item=}')
        if not item:
            return False
        if not check_password_hash(item.password, password):
            return False
        return item

    def update_password(self, id, password):
        ...