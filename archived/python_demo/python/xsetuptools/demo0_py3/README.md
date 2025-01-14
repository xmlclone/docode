```sh
Python 3.12.0
build 0.10.0
setuptools 68.2.2
```

```sh
pip install --upgrade setuptools
pip install --upgrade build # 会自动安装 setuptools
```


```sh
python -m build .
python -m build --no-isolation

pip install -e .

# 版本号
git add -a 1.0.0 -m 1.0.0
```


1. [quickstart](https://setuptools.pypa.io/en/latest/userguide/quickstart.html)
2. [userguide](https://setuptools.pypa.io/en/latest/userguide/)
3. [pyproject.toml](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)
4. [setup.py](https://setuptools.pypa.io/en/latest/references/keywords.html)
5. [package-discovery-and-namespace-packages](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#package-discovery-and-namespace-packages)