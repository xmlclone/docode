import logging

from typing import Union, Sequence, Type, Dict

from ..dao import UserDao
from ..model import UserPy
from ..model import UserDB
from ..utils.deco import catch_exc_return_false


logger = logging.getLogger(__name__)


class Service:
    dao: Union[UserDao, UserDao]
    pymodel: Type[UserPy]

    def get(self, id):
        item = self.dao.get(id=id)
        return self.pymodel.model_validate(item)
    
    def get_all(self) -> Sequence[UserPy]:
        results = [self.pymodel.model_validate(i) for i in self.dao.get_all()]
        return results

    @catch_exc_return_false
    def add(self, item: Dict):
        obj = UserDB(**self.pymodel.model_validate(item).model_dump())
        self.dao.add(obj)

    @catch_exc_return_false
    def delete(self, id, soft=True):
        self.dao.delete(id, soft)