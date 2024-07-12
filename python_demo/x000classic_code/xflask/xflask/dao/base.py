import logging
import sqlalchemy

from typing import Union, Type, Sequence, Dict, Any
from sqlalchemy import select

from ..model import db
from ..model import UserDB


logger = logging.getLogger(__name__)


class Dao:
    # 注意 Type[XXX] 和 XXX 的区别
    model: Union[Type[UserDB], Type[UserDB]]

    def get(self, id: int, allow_deleted=True) -> Union[None, UserDB]:
        stmt = select(self.model).filter_by(id=id)
        if not allow_deleted:
            stmt = stmt.filter_by(deleted=False)
        item = db.session.scalars(stmt).first()
        return item
        
    def get_all(self, allow_deleted=True) -> Union[Sequence[UserDB], Sequence[UserDB]]:
        stmt = select(self.model)
        if not allow_deleted:
            stmt = stmt.filter_by(deleted=False)
        items: sqlalchemy.engine.result.ScalarResult = db.session.scalars(stmt)
        return items.all()

    def add(self, item: Union[UserDB, UserDB]):
        db.session.add(item)
        db.session.commit()

    def delete(self, id: int, soft: bool=True):
        item = db.get_or_404(self.model, id)
        logger.debug(f"delete item: {item}")
        if not soft:
            db.session.delete(item)
        else:
            setattr(item, 'deleted', True)
        db.session.commit()

    def update(self, id: int, kwargs: Dict[str, Any]):
        item = self.get(id)
        for key, val in kwargs.items():
            setattr(item, key, val)
        db.session.commit()
        