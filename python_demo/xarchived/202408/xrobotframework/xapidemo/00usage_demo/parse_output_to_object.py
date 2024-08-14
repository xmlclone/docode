from typing import List, Optional, Union
from enum import Enum
from datetime import datetime
from robot.model import Keyword as _Keyword, TestCase as _TestCase, TestSuite as _TestSuite
from robot.result.model import TestCase as ResultTestCase
from robot.result.model import TestSuite as ResultTestSuite
from robot.result.model import Keyword as ResultKeyword
# from robot.model import For, If, Try, While, Return, Continue, Break, Error, TryBranch, IfBranch
# from robot.running.model import UserKeyword
# from robot.result import ForIteration, WhileIteration
from robot.version import VERSION
from robot.api import ExecutionResult, SuiteVisitor
from robot.result.visitor import ResultVisitor
from pydantic.dataclasses import dataclass


class Status(Enum):
    Failure = 'Failure'
    Success = 'Success'
    NotExecuted = 'NotExecuted'

@dataclass
class Keyword:
    name: str
    start_time: datetime
    end_time: datetime
    params: Optional[List[str]] = None
    returns: Optional[List[str]] = None
    status: Optional[Status] = Status.NotExecuted

@dataclass
class TestCase:
    suite: str
    name: str
    start_time: datetime
    end_time: datetime
    keywords: List[Keyword]
    status: Optional[Status] = Status.NotExecuted


# 本文演示版本为: RF 6.1.1
version_info = tuple((int(i) for i in VERSION.split('.')))


result = ExecutionResult('output-b.xml')


# 递归遍历，其实可以通过对象的 longname 获取
# def iter_kw_parent(kw: Union[_TestSuite, _TestCase, For, If, IfBranch, Try, TryBranch, While, _Keyword, Return, Continue, Break, Error, UserKeyword, ForIteration, WhileIteration]):
# def iter_kw_parent(kw):
#     _parent = kw.parent
#     if _parent:
#         return f"{iter_kw_parent(_parent)}.{kw.name}"
#     else:
#         return kw.name


# def iter_tc_parent(tc: Union[ResultTestCase, ResultTestSuite]):
#     _parent = tc.parent
#     if _parent:
#         return f"{iter_tc_parent(_parent)}.{tc.name}"
#     else:
#         return tc.name



class MySuiteVisitor(SuiteVisitor):
    def end_keyword(self, keyword: _Keyword):
        print(keyword)
        return super().end_keyword(keyword)


class KeywordResultVisitor(ResultVisitor):
    def end_keyword(self, keyword: ResultKeyword):
        # ret = iter_kw_parent(keyword)
        print(f"{keyword.kwname=}")
        print(f"{keyword.status=}")
        print(f"{keyword.message=}")
        for m in keyword.messages:
            print(m)
        # print(f"{keyword.messages=}")
        # print(f"end keyword: {keyword}, {keyword.parent=}")
        return super().end_keyword(keyword)


# ResultVisitor 其实是 SuiteVisitor 的一个子类
class UserResultVisitor(ResultVisitor):
    # def start_test(self, test: _TestCase) -> bool | None:
    #     print(f"start test: {test}")
    #     return super().start_test(test)
    
    def end_test(self, test: ResultTestCase):
        # ret = iter_tc_parent(test)
        # print(ret)
        # print(f"end test: {test}, {test._parent=}")
        # 'body', 'body_class', 'config', 'copy', 'critical', 'deepcopy', 'doc', 
        # 'elapsed_time', 'elapsedtime', 'end_time', 'endtime', 'failed', 'fixture_class', 
        # 'from_dict', 'from_json', 'has_setup', 'has_teardown', 'id', 'keywords', 'lineno', 
        # 'longname', 'message', 'name', 'not_run', 'parent', 'passed', 'repr_args', 'setup', 
        # 'skipped', 'source', 'start_time', 'starttime', 'status', 'tags', 'teardown', 'timeout', 'to_dict', 'to_json', 'visit'
        # print(dir(test))
        # if test.name.startswith('001-电子书-'):
        if test.name.startswith('015-书名-'):
            print(test)
            # print(f"{test.status=}, {type(test.status)=}")   # PASS FAIL   字符串格式
            # print(test.keywords) RF 4.0开始建议使用body
            # print(f"{test.body=}")
            # print(f"{test.message=}")  # 一般失败才会有值，但是也可以通过编程或其它手段给pass的用例设置message
            # print(f"{test.longname=}")  # 包含了测试集的名称，故没必要自己去迭代获取
            # print(test.to_dict())
            # print('-' * 100)

            for kw in test.body:
                if isinstance(kw, ResultKeyword):
                    # 'args', 'assign', 'body', 'body_class', 'children', 'config', 'copy', 'deepcopy', 'doc', 
                    # 'elapsed_time', 'elapsedtime', 'end_time', 'endtime', 'failed', 'from_dict', 'from_json', 
                    # 'has_teardown', 'id', 'keywords', 'kwname', 'libname', 'message', 'messages', 'name', 'not_run', 
                    # 'parent', 'passed', 'repr_args', 'skipped', 'sourcename', 'start_time', 'starttime', 'status', 'tags', 
                    # 'teardown', 'timeout', 'to_dict', 'to_json', 'type', 'visit'
                    # print(dir(kw))
                    # print(kw)
                    # print(f"{kw.status=}")
                    # print(f"{kw.message=}")
                    # print(f"{kw.messages=}")
                    # ResultVisitor 其实是 SuiteVisitor 的一个子类，故可以传自己
                    kw.visit(KeywordResultVisitor())
                    print('-' * 100)
                    # print(f"{}")

            print('-' * 100)
        return super().end_test(test)

    # def visit_test(self, test: "_TestCase"):
    #     print(f"visit test: {test}")
    #     return super().visit_test(test)
    
    # def start_keyword(self, keyword: _Keyword) -> bool | None:
    #     print(f"start keyword: {keyword}")
    #     return super().start_keyword(keyword)
    
    # def end_keyword(self, keyword: _Keyword):
    #     # ret = iter_kw_parent(keyword)
    #     print(keyword)
    #     # print(f"end keyword: {keyword}, {keyword.parent=}")
    #     return super().end_keyword(keyword)

    # def visit_keyword(self, keyword: "_Keyword"):
    #     ret = iter_kw_parent(keyword)
    #     print(ret)
    #     # print(f"visit keyword: {keyword}")
    #     return super().visit_keyword(keyword)


result.visit(UserResultVisitor())