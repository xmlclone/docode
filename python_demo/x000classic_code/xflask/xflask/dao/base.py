import logging
import sqlalchemy

from typing import Union, Type, Dict, List, overload
from sqlalchemy import select

from ..model import db
from ..model.base import PyBase, DbBase


logger = logging.getLogger(__name__)


class Dao:
    def __init__(
        self,
        # 注意 Type[XXX] 和 XXX 的区别
        db_model: Type[DbBase],
        py_model: Type[PyBase]
    ):
        self.db_model = db_model
        self.py_model = py_model

    def get(
        self, 
        id: Union[int, None] = None
    ) -> Union[PyBase, List[PyBase]]:
        if id:
            item = db.get_or_404(self.db_model, id)
            return self.py_model.model_validate(item)
        else:
            stmt = select(self.db_model)
            # compiled = stmt.compile()
            # logger.debug(f"{stmt=}, {compiled=}, {compiled.params=}")
            items: sqlalchemy.engine.result.ScalarResult = db.session.scalars(stmt)
            logger.debug(f"{items=}")
            result = []
            for item in items:
                logger.debug(item)
                result.append(self.py_model.model_validate(item))
            logger.debug(f"{result=}")
            return result

    def add(
        self, 
        request_data: Union[Dict, None]
    ):
        if request_data:
            obj = self.py_model.model_validate(request_data)
            item = self.db_model(**obj.model_dump())
            db.session.add(item)
            db.session.commit()
            return True
        return False

    def delete(self, id):
        item = db.get_or_404(self.db_model, id)
        db.session.delete(item)
        db.session.commit()
        return True

    def update(self, id):
        ...