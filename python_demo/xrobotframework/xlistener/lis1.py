from robot.running.model import TestCase as Data
from robot.result.model import TestCase as Result


ROBOT_LISTENER_API_VERSION = 3


def end_test(data: Data, result: Result):
    if not result.passed:
        print(f"发送邮件或短信逻辑: 失败用例名称: {result.name}")