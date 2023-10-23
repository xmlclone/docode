# 演示环境

```shell
conda create -n vdocode python=3.12
pytest==7.4.2
```

# 基础命令

```shell
# 最简单的执行
pytest

# 静默模式
pytest -q

# 输出print内容
pytest -s

# 执行某个文件
pytest test_ue.py

# 执行某个目录下的测试文件
pytest testing/

# 根据匹配执行，不区分大小写，可以匹配目录、文件、类、函数名，还可以使用 and or not等
pytest -k "MyTest and not myfunction"

# 指定指定某个具体的id
pytest test.py::testclass::testmethod

# 根据marker执行(@pytest.mark.p0)
pytest -m p0

# 查看所有fixtures
pytest --fixtures

# 查看所有markers
pytest --markers

# 查看有多少用例
pytest --collect-only
```


# 参考链接

1. [官方文档](https://docs.pytest.org/en/7.4.x/)