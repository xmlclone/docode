import re
import json

from typing import Optional, cast, List
from enum import Enum
from datetime import datetime
from robot.result.model import TestCase as ResultTestCase
from robot.result.model import Keyword as ResultKeyword
from robot.version import VERSION
from robot.api import ExecutionResult
from robot.result.visitor import ResultVisitor
from pydantic.dataclasses import dataclass
from pydantic import BaseModel, field_validator


class Status(Enum):
    Failure = 'Failure'
    Success = 'Success'
    NotExecuted = 'NotExecuted'


@dataclass
class TestCase:
    suite: str
    name: str
    start_time: datetime
    end_time: datetime
    message: Optional[str] = ''
    status: Optional[Status] = Status.NotExecuted


class Response(BaseModel):
    url: str
    status: int
    body: str

    @field_validator('body')
    @classmethod
    def body_validator(cls, body) -> str:
        return json.dumps(json.loads(body))


# 本文演示版本为: RF 6.1.1
version_info = tuple((int(i) for i in VERSION.split('.')))


result = ExecutionResult('output-b.xml')
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


def parse_request_message(message: str) -> Response | None:
    """
    POST Response : url=https://jadeite.migu.cn/read_search/storeSearch
 status=200, reason=OK
 headers={'Server': 'nginx', 'Date': 'Wed, 05 Jun 2024 03:16:59 GMT', 'Content-Type': 'application/json;charset=UTF-8', 'Content-Length': '15', 'Connection': 'keep-alive', 'Vary': 'Access-Control-Request-Headers'}
 body={
        "code":800
}
    """
    match = re.search(r"url=(?P<url>\S+).*status=(?P<status>\d+).*body=(?P<body>.*)", message, re.S)
    if match:
        return Response.model_validate(match.groupdict())
    return None



def get_kw_tc(kw: ResultKeyword) -> ResultTestCase:
    _parent = kw.parent
    if isinstance(_parent, ResultTestCase):
        return _parent
    else:
        _parent = cast(ResultKeyword, _parent)
        return get_kw_tc(_parent)


class KeywordResultVisitor(ResultVisitor):
    def end_keyword(self, keyword: ResultKeyword):
        if keyword.kwname in Checked_KW:
            tc = get_kw_tc(keyword)
            for message in keyword.messages:
                if 'POST Response' in message.message:
                    response = parse_request_message(message.message)
                    if response:
                        tc.message = f"{tc.message} {response.body}"


class UserResultVisitor(ResultVisitor):
    def end_test(self, test: ResultTestCase):
        if test.failed:
            testcases.append(test)
            for body in test.body:
                if not isinstance(body, ResultKeyword):
                    continue
                if body.kwname in Checked_KW:
                    test.message = f"{test.message} {body.message}"
                else:
                    body.visit(KeywordResultVisitor())


result.visit(UserResultVisitor())

for tc in testcases:
    print(f"tc={tc.longname}, message={tc.message}")