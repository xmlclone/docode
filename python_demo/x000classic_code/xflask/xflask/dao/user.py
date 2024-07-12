import logging

from sqlalchemy import select

from .base import Dao
from ..model import db, UserDB


logger = logging.getLogger(__name__)


class UserDao(Dao):
    def __init__(self):
        self.model = UserDB

    def get_with_full_name(self, full_name: str, allow_deleted=True):
        stmt = select(self.model).where(self.model.full_name==full_name)
        if not allow_deleted:
            stmt = stmt.filter_by(deleted=False)
        item = db.session.scalars(stmt).first()
        logger.debug(f"{full_name=}, {allow_deleted=}, {item=}")
        return item