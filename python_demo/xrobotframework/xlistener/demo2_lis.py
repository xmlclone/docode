# robot --listener demo2_lis -P . demo2.robot

import re
import json

from typing import Optional, cast, List
from robot.running.model import TestCase as RunningTestCase
from robot.running.model import Keyword as RunningKeyword
from robot.result.model import TestCase as ResultTestCase
from robot.result.model import Keyword as ResultKeyword
from robot.result.model import Message as ResultMessage
from robot.result.visitor import ResultVisitor
from pydantic.dataclasses import dataclass
from pydantic import BaseModel, field_validator


class Response(BaseModel):
    url: str
    status: int
    body: str

    @field_validator('body')
    @classmethod
    def body_validator(cls, body: str) -> str:
        try:
            return json.dumps(json.loads(body))
        except:
            return body
    

Checked_KW = [
    'Post Request',
    'Get Request',
    'PATCH Request',
    'PUT Request',
    'DELETE Request',
    'HEAD Request',
    'OPTIONS Request',
    'PUT On Session',
    'OPTIONS On Session',
    'HEAD On Session',
    'DELETE On Session',
    'PATCH On Session',
    'POST On Session',
    'Get On Session',
]
testcases: List[ResultTestCase] = []


class demo2_lis:
    ROBOT_LISTENER_API_VERSION = 3
    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self
        self.response: List[Response] = list()

    def log_message(self, _message: ResultMessage):
        message = """
    POST Response : url=https://jadeite.migu.cn/read_search/storeSearch
 status=200, reason=OK
 headers={'Server': 'nginx', 'Date': 'Wed, 05 Jun 2024 03:16:59 GMT', 'Content-Type': 'application/json;charset=UTF-8', 'Content-Length': '15', 'Connection': 'keep-alive', 'Vary': 'Access-Control-Request-Headers'}
 body={
        "code":800
}
    """
        match = re.search(r"url=(?P<url>\S+).*status=(?P<status>\d+).*body=(?P<body>.*)", message, re.S)
        if match:
            self.response.append(Response.model_validate(match.groupdict()))

    def end_test(self, data: RunningTestCase, result: ResultTestCase):
        if result.failed:
            message = result.message
            if self.response:
                for response in self.response:
                    message = f"{message}, {response.url} response: {response.body}"
                self.response = list()
            print(message)