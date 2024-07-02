import json
import logging

from typing import Literal, Union, Optional, Self, Dict, List, Any, cast
from enum import Enum
from flask import make_response as flask_make_response
from pydantic import BaseModel, Field, model_validator, field_validator
from werkzeug.exceptions import HTTPException

from .model import UserPy
from .model.base import PyBase


logger = logging.getLogger(__name__)


class ResponseStatus(Enum):
    success = 0
    fail = 1
    unkonwn = 2


class ResponsePy(BaseModel):
    code: Optional[int] = Field(default=0)
    status: ResponseStatus
    # 默认情况下不能使用父类，否则 dump 出来的数据是空的
    # 但是可以配合 serialize_as_any 和 SerializeAsAny 使用则可以
    # https://docs.pydantic.dev/latest/concepts/serialization/#serializing-with-duck-typing
    data: Union[List[PyBase], PyBase, str, None, Dict]

    @model_validator(mode='after')
    def get_code(self) -> Self:
        self.code = self.status.value
        self.status = self.status.name # type: ignore
        return self
    
    # @model_validator(mode='after')
    # def get_status(self) -> Self:
    #     self.status = self.status.name
    #     return self
    
    # @field_validator('status', mode='plain')
    # @classmethod
    # def convert_status(cls, value: ResponseStatus) -> str:
    #     return value.name


def make_response(status=ResponseStatus.success, data=None, exception: HTTPException | None=None, exception_message=None):
    if exception:
        # 如果有异常，应该防止用户传递错误的 status 和 data
        if status == ResponseStatus.success:
            status = ResponseStatus.fail
        data = exception_message or exception.description
    resp_py = ResponsePy(status=status, data=data)
    # logger.debug(f"{resp_py=}")
    # logger.debug(f"{resp_py.data[0].model_dump_json()=}")
    resp = flask_make_response()
    resp.content_type = 'application/json'
    resp.status = 200
    # logger.debug(f"{resp_py.model_dump_json()=}, {resp_py.model_dump()=}")
    resp.data = resp_py.model_dump_json(serialize_as_any=True)
    logger.debug(f"{resp.data=}")
    return resp