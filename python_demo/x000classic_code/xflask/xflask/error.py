import logging
import json
import traceback

from typing import cast
from flask import Flask, Response, make_response
from werkzeug.exceptions import HTTPException
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError

from .wrap_response import make_response
from .constant import ResponseStatus
from .exception import UnkonwnError


logger = logging.getLogger(__name__)


def init_app(app: Flask):
    app.register_error_handler(HTTPException, handle_http_exception)
    app.register_error_handler(Exception, handle_exception)


# 也可以通过如下方式注册
# @app.errorhandler(HTTPException)
def handle_http_exception(e: HTTPException):
    logger.debug(f"{e.code=}, {e.name=}")
    return make_response(exception=e)
    # response = cast(Response, e.get_response())
    # response.data = json.dumps({
    #     "code": e.code,
    #     "name": e.name,
    #     "description": e.description
    # })
    # response.content_type = "application/json"
    # return response


# TODO: 某些异常信息告知用户不明显
def handle_exception(e: Exception):
    logger.debug(f"e={e.__class__.__name__}, detail={e}, {type(e)=}")
    # logger.debug(traceback.format_exc())
    # logger.debug(isinstance(e, IntegrityError))
    if isinstance(e, ValidationError):
        logger.debug(e.errors())
        return make_response(ResponseStatus.unkonwn, exception=UnkonwnError(), exception_message=e.errors())
    if isinstance(e, IntegrityError):
        # for a in dir(e):
        #     logger.debug(f"{a}: {getattr(e, a)}")
        return make_response(ResponseStatus.unkonwn, exception=UnkonwnError(), exception_message=str(e.orig))
    return make_response(ResponseStatus.unkonwn, exception=UnkonwnError())
    # response = make_response()
    # response.status_code = 200
    # response.data = json.dumps({
    #     "code": 800,
    #     "name": e.__class__.__name__,
    #     "description": str(e)
    # })
    # response.content_type = "application/json"
    # return response