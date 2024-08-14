import logging

from typing import Union, Sequence, Type, Dict, Any

from ..dao import UserDao
from ..model import UserPy
from ..model import UserDB
from ..utils.deco import catch_exc_return_false


logger = logging.getLogger(__name__)


class Service:
    dao: Union[UserDao, UserDao]
    pymodel: Type[UserPy]

    def get(self, id: int):
        item = self.dao.get(id=id)
        if not item:
            return None
        return self.pymodel.model_validate(item)
    
    def get_all(self) -> Sequence[UserPy]:
        pyobjs = [self.pymodel.model_validate(i) for i in self.dao.get_all()]
        return pyobjs

    @catch_exc_return_false
    def add(self, data: Dict[str, Any]):
        pyobj = self.pymodel.model_validate(data)
        item = UserDB(**pyobj.model_dump())
        self.dao.add(item)

    @catch_exc_return_false
    def delete(self, id, soft=True):
        self.dao.delete(id, soft)

    @catch_exc_return_false
    def update(self, id: int, data: Dict[str, Any]):
        pyobj = self.get(id)
        if not pyobj:
            return False
        pydict = pyobj.model_dump()
        pydict.update(data)
        logger.debug(f"{pydict=}")
        new_pyobj = self.pymodel.model_validate(pydict)
        update_attr: Dict[str, Any] = {}
        for key in data:
            update_attr[key] = getattr(new_pyobj, key)
        self.dao.update(id, update_attr)