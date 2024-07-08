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

    def get_with_full_name(self, full_name):
        stmt = select(self.db_model).where(self.db_model.full_name==full_name)
        item = db.session.scalars(stmt).first()
        return item