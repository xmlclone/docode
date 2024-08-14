import logging

from flask import request
from flask.views import MethodView
from werkzeug.exceptions import NotFound

from ..wrap_response import make_response
from ..service import UserService
from ..exception import AddObjectError, DeleteObjectError, RequestDataFormatError, UpdateObjectError
from ..service.auth import login_required, admin_required


logger = logging.getLogger(__name__)


class BaseController(MethodView):
    init_every_request = False
    service: UserService

    def valid_request_data(self):
        request_data = request.json
        if not request_data:
            raise RequestDataFormatError()
        logger.debug(f"{request_data=}")
        return request_data


class BaseControllerItem(BaseController):
    def get(self, id):
        item = self.service.get(id)
        if not item:
            raise NotFound()
        return make_response(data=item)
    
    @admin_required
    def delete(self, id):
        if self.service.delete(id):
            return make_response()
        raise DeleteObjectError(data=id)
        
    @login_required
    def post(self, id):
        request_data = self.valid_request_data()
        if self.service.update(id, request_data):
            return make_response()
        raise UpdateObjectError(data=id)


class BaseControllerGroup(BaseController):
    def get(self):
        return make_response(data=self.service.get_all())

    @admin_required
    def post(self):
        request_data = self.valid_request_data()
        if self.service.add(request_data):
            return make_response()
        raise AddObjectError(data=request_data)