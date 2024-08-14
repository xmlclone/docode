import pytest
import logging


logger = logging.getLogger(__name__)


@pytest.fixture
def conftest_fix1():
    print("conftest_fix1")
    return {"conftest_fix1_key": "conftest_fix1_value"}


# 除了通过配置文件的marker配置外，还可以通过下面的方式增加marker
def pytest_configure(config: pytest.Config):
    config.addinivalue_line(
        "markers", "P1(name): mark test LEVEL to P1"
    )


# 增加自定义命令行参数
# pytest --help可以查看新增的命令行帮助
# pytest test_demo0.py::test_1 --opt1=1 --opt1=2 --opt2 --opt3="test" --opt4=1 --opt5=2
def pytest_addoption(parser: pytest.Parser, pluginmanager: pytest.PytestPluginManager):
    group = parser.getgroup("mygroup", "My group")
    group.addoption("--opt1", action="append", default=[])
    group.addoption("--opt2", action="store_true", default=False)
    group.addoption("--opt3", action="store", default=None)
    group.addoption("--opt4", type=int, default=0)
    group.addoption("--opt5", type=int, default=1, choices=[1, 2, 3, 4])

# 获取自定义命令行参数，pytestconfig是一个内置的fixture
@pytest.fixture(autouse=True)
def conftest_fix2(pytestconfig: pytest.Config):
    logger.info(f'{pytestconfig.getoption("opt1")=}')
    logger.info(f'{pytestconfig.getoption("opt2")=}')
    logger.info(f'{pytestconfig.getoption("opt3")=}')
    logger.info(f'{pytestconfig.getoption("opt4")=}')
    logger.info(f'{pytestconfig.getoption("opt5")=}')
    # 另外一种访问方式
    logger.info(f'{pytestconfig.option.opt1=}')