import logging

from flask import request
from flask.views import MethodView

from ..wrap_response import make_response
from ..service import UserService
from ..exception import AddObjectError, DeleteObjectError, RequestDataFormatError
from ..service.auth import login_required


logger = logging.getLogger(__name__)


class BaseController(MethodView):
    init_every_request = False
    service: UserService


class BaseControllerItem(BaseController):
    def get(self, id):
        return make_response(data=self.service.get(id))
    
    @login_required
    def delete(self, id):
        if self.service.delete(id):
            return make_response()
        return make_response(exception=DeleteObjectError(data=id))
        
    # @login_required
    # def post(self, id):
    #     if self.service.update(id, request.json):
    #         return make_response()
    #     return make_response(exception=UpdateObjectError(data=id))


class BaseControllerGroup(BaseController):
    def get(self):
        return make_response(data=self.service.get_all())

    # @login_required
    def post(self):
        request_data = request.json
        if not request_data:
            return make_response(exception=RequestDataFormatError())
        logger.debug(f"{request_data=}")
        if self.service.add(request_data):
            return make_response()
        return make_response(exception=AddObjectError(data=request_data))