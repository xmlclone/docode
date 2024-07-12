import logging
import sqlalchemy

from typing import Union, Type, Sequence
from sqlalchemy import select

from ..model import db
from ..model import UserDB


logger = logging.getLogger(__name__)


class Dao:
    # 注意 Type[XXX] 和 XXX 的区别
    model: Union[Type[UserDB], Type[UserDB]]

    def get(self, id: int) -> Union[UserDB, UserDB]:
        item = db.get_or_404(self.model, id)
        return item
        
    def get_all(self) -> Union[Sequence[UserDB], Sequence[UserDB]]:
        stmt = select(self.model)
        items: sqlalchemy.engine.result.ScalarResult = db.session.scalars(stmt)
        return items.all()

    def add(self, item: Union[UserDB, UserDB]):
        db.session.add(item)
        db.session.commit()

    def delete(self, id, soft=True):
        item = db.get_or_404(self.model, id)
        logger.debug(f"delete item: {item}")
        if not soft:
            db.session.delete(item)
        else:
            setattr(item, 'deleted', True)
        db.session.commit()