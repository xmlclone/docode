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
python -m build
```

> 为啥不建议使用`setup.py`，请参考: [Why you shouldn’t invoke setup.py directly](https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html)

# 开发模式

```shell
# 如果已经安装到了site-packages下，先卸载
pip uninstall mypkg1
# 需要先python -m build后才可以使用，命令执行目录和python -m build在同一级，否则需要更改 .参数
# 不用重复使用下面命令，使用一次即可
pip install -e .
```

# 参考链接

1. [官方文档](https://setuptools.pypa.io/en/latest/)
2. [MANIFEST.in配置参考](https://packaging.python.org/en/latest/guides/using-manifest-in/#manifest-in-commands)
3. [Why you shouldn’t invoke setup.py directly](https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html)
4. [pyproject.toml配置详解](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)