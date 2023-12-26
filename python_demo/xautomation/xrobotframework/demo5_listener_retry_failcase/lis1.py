from robot.running.model import TestCase as Data
from robot.result.model import TestCase as Result
from robot.libraries.BuiltIn import BuiltIn

ROBOT_LISTENER_API_VERSION = 3


def end_test(data: Data, result: Result):
    if not result.passed:
        BuiltIn().run_keywords(data.body)