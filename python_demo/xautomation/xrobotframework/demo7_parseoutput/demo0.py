from robot.api import ExecutionResult
from robot.result import TestCase, TestSuite
from robot.result.model import Body, Keyword


result = ExecutionResult("output2.xml")


# 递归获取suite的parent
def get_suite_parents(suite: TestSuite, include_self=True):
    if include_self:
        parents = [suite]
    else:
        parents = []
    if suite.parent:
        parents.extend(get_suite_parents(suite.parent))
    return parents


# 递归获取fail的keyword
def get_fail_keywords(keyword: list[Keyword]):
    keywords = []
    for kw in keyword:
        if not isinstance(kw, Keyword):
            continue
        if kw.status == "FAIL":
            keywords.append(kw)
        if kw.body:
            keywords.extend(get_fail_keywords(kw.body))
    return keywords


# 获取fail的keyword的fail message
def get_fail_keyword_fail_messages(fail_keywords: list[Keyword]):
    messages = []
    for kw in fail_keywords:
        for msg in kw.messages:
            if msg.level == "FAIL":
                messages.append(msg.message)
    return messages


class UserTestCase:
    def __init__(self, tc: TestCase, suite: TestSuite):
        self.tc = tc
        self.suite = suite
        self.status = tc.status
        self.message = tc.message
        self.name = tc.name
        if tc.name == "【消息管理】短信":
            fail_kws = get_fail_keywords(tc.body)
            print(get_fail_keyword_fail_messages(fail_kws))
            # for keyword in tc.body:
            #     print(keyword, keyword.body)
        # for keyword in tc.body:
            # print(tc.name)
                # print(keyword.messages)
            # for message in keyword.messages:
                # if message.level == "FAIL":
                    # print(message.message)

    @property
    def suite_name(self):
        return '-'.join(map(lambda s: str(s).replace(" ", ""), get_suite_parents(self.suite)[::-1]))

    def __str__(self):
        return self.name
    
    __repr__ = __str__


# 递归解析suite下面的case
def get_testcases(suite: TestSuite) -> list[UserTestCase]:
    results = []
    if suite.tests:
        for test in suite.tests:
            results.append(UserTestCase(test, suite))
    else:
        if suite.suites:
            for suite in suite.suites:
                results.extend(get_testcases(suite))
    return results


testcases = get_testcases(result.suite)
for test in testcases:
    # print(f"{test=}, {test.status=}, {test.suite_name=}, {test.message=}")
    ...