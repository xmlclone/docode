from robot.result.model import TestCase

class ClsListener(object):
    ROBOT_LISTENER_API_VERSION = 3
    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self

    def end_test(self, _, test: TestCase):
        ...