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

# fixture可以成为另外一个fixture的参数
@pytest.fixture
def fix2(fix1):
    print("fix2")
    return fix1

@pytest.fixture(autouse=True)
def fix3():
    print("fix3")
    return {"fix3_key": "fix3_value"}

@pytest.fixture(scope="function", autouse=True)
def fix4():
    print("fix4 start")
    yield
    print("fix4 end.")


# pytest test_demo0.py::test_2 -s
# 上面的执行顺序，fix3 -> fix4 start -> fix1 -> fix2 -> fix4 end
# 也就是autouse的根据定义顺序执行，然后是参数顺序执行
# 还可以直接引用conftest.py里面的fixture，比如下面的conftest_fix1
def test_2(fix1, fix2, conftest_fix1):
    # fix1也就是一个fixture，可以作为test或其它fixture的参数，获取的是其返回值或yield内容
    # 可以有多个fixture
    assert fix1['fix1_key'] == 'fix1_value'
    assert fix2['fix1_key'] == 'fix1_value'
    # 注意，autouse表示会自动应用，但是如果想像上面fix1和fix2的方式使用，仍然需要通过参数传递
    # 无法在test里面直接使用fix3(fix4类似)，因为这里直接使用fix3其实就是一个函数，而不是fixture
    print(fix3)
    # 报错，因为fix3是一个function，而不是其返回值
    # assert fix3['fix3_key'] == 'fix3_value'
    assert conftest_fix1['conftest_fix1_key'] == 'conftest_fix1_value'


# pytest -m P0 -s
# 在pyproject.toml下配置了marker，并可以应用到testcase上，通过命令行-m参数选择执行的用例
@pytest.mark.P0
# 可以增加多个marker，下面的P1 marker是通过conftest.py里面的hook函数注册的
# 上面的P0 marker是注册在pyproject.toml配置文件的
@pytest.mark.P1("w")
def test_3():
    print('test 3, P0 level')