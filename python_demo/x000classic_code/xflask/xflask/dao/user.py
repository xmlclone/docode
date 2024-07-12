import logging

from sqlalchemy import select

from .base import Dao
from ..model import db, UserDB


logger = logging.getLogger(__name__)


class UserDao(Dao):
    def __init__(self):
        self.model = UserDB

    def get_with_full_name(self, full_name):
        stmt = select(self.model).where(self.model.full_name==full_name)
        item = db.session.scalars(stmt).first()
        return item