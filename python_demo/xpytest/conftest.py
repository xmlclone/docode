import pytest


@pytest.fixture
def conftest_fix1():
    print("conftest_fix1")
    return {"conftest_fix1_key": "conftest_fix1_value"}


# 除了通过配置文件的marker配置外，还可以通过下面的方式增加marker
def pytest_configure(config: pytest.Config):
    config.addinivalue_line(
        "markers", "P1(name): mark test LEVEL to P1"
    )