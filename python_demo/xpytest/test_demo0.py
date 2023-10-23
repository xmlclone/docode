import pytest


def add(a, b):
    return a + b


def test_1():
    assert add(1, 2) == 3


class TestClassDemo:
    class_attr = 0

    def test_2(self):
        self.class_attr = 1
        assert self.class_attr == 1

    def test_3(self):
        # fail，因为每个test都是单独的类实例，故self.class_attr = 0
        assert self.class_attr == 1

    def test_4(self):
        TestClassDemo.class_attr = 2
        assert TestClassDemo.class_attr == 2

    def test_5(self):
        # pass, 通过TestClassDemo.class_attr的方式设置属性，是类属性
        # 但是上面的test_2虽然通过self.class_attr为1，但只要不是通过TestClassDemo.方式设置的，仍然是0
        assert TestClassDemo.class_attr == 2


@pytest.fixture
def fix1():
    print("fix1")
    return {"fix1_key": "fix1_value"}

def test_2(fix1):
    assert fix1['fix1_key'] == 'fix1_value'