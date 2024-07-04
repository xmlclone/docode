import logging

from typing import Dict, Union
from flask import request
from flask.views import MethodView
from sqlalchemy import select

from ..wrap_response import make_response
from ..constant import ResponseStatus
from ..dao.base import Dao
from ..exception import AddObjectError, DeleteObjectError, UpdateObjectError
from ..auth import login_required


logger = logging.getLogger(__name__)


class BaseView(MethodView):
    init_every_request = False
    dao: Dao


class BaseItem(BaseView):
    def get(self, id):
        return make_response(data=self.dao.get(id))
    
    @login_required
    def delete(self, id):
        if self.dao.delete(id):
            return make_response()
        return make_response(exception=DeleteObjectError(data=id))
        
    @login_required
    def post(self, id):
        if self.dao.update(id, request.json):
            return make_response()
        return make_response(exception=UpdateObjectError(data=id))


class BaseGroup(BaseView):
    def get(self):
        return make_response(data=self.dao.get())

    # @login_required
    def post(self):
        request_data = request.json
        logger.debug(f"{request_data=}")
        if self.dao.add(request_data):
            return make_response()
        return make_response(exception=AddObjectError(data=request_data))