# 说明

更详细内容请参考: [pdemo](https://github.com/xmlclone/pdemo)

虽然本文在setuptools下，但本文不仅限于`setuptools`，本文包含了一般python的打包、分发、构建、测试等，比如包含了`tox`、`mypy`等。

另外可以参考[xpoetry](https://github.com/xmlclone/docode/tree/main/python_demo/xpoetry)的构建方式

# 安装

```shell
pip install --upgrade setuptools
pip install --upgrade build

# 本文安装的版本: 
# setuptools==68.2.2
# build==1.0.3
```

# 目录结构说明

默认情况下，需要打包的工程需要放置到一个目录下，这个目录下创建配置文件，比如`pyproject.toml`、`MANIFEST.in`等文件，参考demo0的目录结构。

# 配置

[setuptools](https://setuptools.pypa.io/en/latest/)支持`pyproject.toml`、`setup.cfg`和`setup.py`几种方式，目前推荐使用`pyproject.toml`的方式，本文也以此为例进行说明，详细的请参考`pyproject.toml`文件内的注释。

```shell
# 配置完成后，使用下面命令进行打包
# 命令执行完成后，会在dist目录下生成whl和tar.gz文件
# 这两个文件就可以通过 pip install 进行安装了，此时会安装到site-packages下，项目代码就可以像引用其它模块一样进行引用了
python -m build .

# 查看帮助
python -m build --help

# 只打包sdist，也就是tar.gz文件(默认打包为tar.gz和whl两个文件)
python -m build -s

# 只打包whl
python -m build -w

# 加快打包速度(不安装虚拟环境)
python -m build --no-isolation -s
```

> 为啥不建议使用`setup.py`，请参考: [Why you shouldn’t invoke setup.py directly](https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html)

# 自动版本识别

```shell
# 依赖于setuptools_scm，当然还有很多其它的插件可以使用
pip install setuptools_scm
```

> 项目目录下需要有版本工具的配置信息，比如git就需要有`.git`目录

```toml
[project]
# version = "0.0.1"  # Remove any existing version parameter.
dynamic = ["version"]

[tool.setuptools_scm]
version_file = "pkg/_version.py"
# write_to已经在新版本弃用，使用上面的version_file代替
write_to = "mypkg1/_version.py"
local_scheme = "no-local-version"
```

## 生成规则

1. 根据git的最新tag生成版本号

# 开发模式

```shell
# 如果已经安装到了site-packages下，先卸载
pip uninstall mypkg1
# 需要先python -m build后才可以使用，命令执行目录和python -m build在同一级，否则需要更改 .参数
# 不用重复使用下面命令，使用一次即可
# 但如果[project.scripts]有变更，也需要重新使用下面的命令
pip install -e .
```

# 发布包

## 发布到pypi

```shell
pip install twine
# 测试发布(需要提前在pypi注册账号) https://test.pypi.org
twine upload -r testpypi dist/*
# 正式发布 https://pypi.org/
twine upload dist/*

# 默认发布到pypi,可以通过参数发布到指定的repo
# 注意需要到pypi增加自己的api token,使用api token处理username和password
twine upload --repository-url https://xxx -u username -p password dist/*
```

> 注意: api token只会出现一次，后续无法获取，故需要及时保存，而且使用时的用户名一律为: `__token__`
> 另外：可以配置`$HOME/.pypirc`为如下配置，即可以不在命令行使用用户名和密码

```ini
[pypi]
  username = __token__
  password = pypi-xxxx
```

# tox

```shell
# 查看env列表
tox list

# 执行
tox
tox run

# 指定执行环境
tox run -e py310

# 如果命令行有{}替换符号，可以通过--的方式替换{}
tox run -e py310 -- -v
```

# make

如果在windows下执行，建议使用WSL，安装并启动

> windows下访问wsl目录，直接在资源管理器输入`\\wsl$`就可以查看；linux下访问windows，可以直接`cd /mnt`即可
> wsl里面，进入到指定目录后，如果想通过vscode编辑代码，可以通过`code .`命令启动vscode

`Makefile`里面定义了各项动作，比如要执行`tox`，只需要执行`make test`命令即可

# shields.io生成badges

参考demo0内部README.md文件和[shields.io官方链接](https://shields.io/badges/py-pi-python-version)

# 参考链接

1. [官方文档](https://setuptools.pypa.io/en/latest/)
2. [MANIFEST.in配置参考](https://packaging.python.org/en/latest/guides/using-manifest-in/#manifest-in-commands) or [there](https://setuptools.pypa.io/en/latest/userguide/miscellaneous.html)
3. [Why you shouldn’t invoke setup.py directly](https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html)
4. [pyproject.toml配置详解](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)
5. [twine](https://twine.readthedocs.io/en/stable/index.html)
6. [packaging-projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
7. [setuptools-scm](https://pypi.org/project/setuptools-scm/)
8. [setuptools-scm配置项](https://setuptools-scm.readthedocs.io/en/latest/config/)
9. [tox](https://tox.wiki/en/latest/index.html)
10. [shields.io](https://shields.io/badges/py-pi-python-version)