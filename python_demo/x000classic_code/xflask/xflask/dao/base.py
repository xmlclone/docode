from email.policy import strict
import logging
import sqlalchemy

from typing import Union, Type, Dict, List, overload
from sqlalchemy import select, update

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
            item = self.db_model(**obj.model_dump(exclude_none=True))
            db.session.add(item)
            db.session.commit()
            return True
        return False

    def delete(self, id, soft=True):
        item = db.get_or_404(self.db_model, id)
        logger.debug(f"delete item: {item}")
        if not soft:
            db.session.delete(item)
        else:
            setattr(item, 'delete', True)
        db.session.commit()
        return True

    def update(self, id, request_data: Union[Dict, None]):
        item = db.get_or_404(self.db_model, id)
        logger.debug(f"update item: {item}, update data: {request_data}")
        obj = self.py_model.model_validate(item)
        if request_data:
            # model_copy 更新的数据，没有被转换，比如客户端传递的 date 会被转换为原始的 str ，而不是 date 对象
            # new_obj = obj.model_copy(update=request_data)
            # 故需要额外转义一次
            new_obj = self.py_model.model_validate(obj.model_copy(update=request_data).model_dump())
            # logger.debug(f"{obj=}, {new_obj=}")
            # logger.debug(f"{type(new_obj.birthdate)=}, {new_obj.birthdate=}")
            # logger.debug(f"{type(obj.birthdate)=}, {obj.birthdate=}")
            for key in request_data:
                val = getattr(new_obj, key)
                # logger.debug(f"{key=}, {val=}, {type(val)=}")
                setattr(item, key, val)
            db.session.commit()
            return True
        return False