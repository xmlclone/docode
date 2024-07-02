import logging

from typing import Dict, Union
from flask import request
from flask.views import MethodView
from sqlalchemy import select

from ..wrap_response import make_response, ResponseStatus
from ..dao.base import Dao
from ..exception import AddObjectError, DeleteObjectError


logger = logging.getLogger(__name__)


class BaseView(MethodView):
    init_every_request = False
    dao: Dao


class BaseItem(BaseView):
    def get(self, id):
        return make_response(data=self.dao.get(id))
    
    def delete(self, id):
        if self.dao.delete(id):
            return make_response()
        else:
            return make_response(exception=DeleteObjectError(data=id))


class BaseGroup(BaseView):
    def get(self):
        return make_response(data=self.dao.get())

    def post(self):
        request_data = request.json
        logger.debug(f"{request_data=}")
        if self.dao.add(request_data):
            return make_response()
        else:
            return make_response(exception=AddObjectError(data=request_data))