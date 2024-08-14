# 演示环境

> 项目实际应用情况可参考: [migrate-playwright-pytest](https://github.com/xmlclone/migrate-playwright-pytest)

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

# 指定某个目录下的具体用例
pytest testcases/demo.py::test_2

# 根据marker执行(@pytest.mark.p0)
pytest -m p0

# 查看所有fixtures
pytest --fixtures

# 查看所有markers
pytest --markers

# 查看有多少用例
pytest --collect-only

# 查看plugin注册情况
pytest --trace-config
```

# 编写自己的插件(plugin)

1. 创建插件包，比如本例的`pytest_muplugin1`
2. 配置`pyproject.toml`，参考具体的配置文件
3. 打包`python -m build`
4. 安装`pip install -e .`
5. 通过`pytest --trace-config`查看插件注册情况，使用`pytest --fixtures`查看fixture信息
6. 代码文件`test_demo0.py`直接引用我们的插件fixture: `myplugin1_fix1`

> `pytest --trace-config`信息如下:

![](../../docs/imgs/pytest1.png)

> `pytest --fixtures`信息如下:

![](../../docs/imgs/pytest2.png)

# 常用插件

## pytest-html

```shell
# 安装
pip install pytest-html

# 使用
pytest --html report.html #注意不要和-s一起使用，否则看不见详细信息
# 上面方式会单独生成样式表(css)，不利于邮件发送，下面把所有元素集中到一个html文件内
pytest --html report.html --self-contained-html
```

# 参考链接

1. [官方文档](https://docs.pytest.org/en/7.4.x/)
2. [fixture](https://docs.pytest.org/en/7.4.x/reference/fixtures.html#fixtures)
3. [marker](https://docs.pytest.org/en/7.4.x/how-to/mark.html#mark)
4. [api](https://docs.pytest.org/en/7.4.x/reference/index.html#reference)