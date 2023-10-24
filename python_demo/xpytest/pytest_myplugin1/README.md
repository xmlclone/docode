# 说明

编写自己的plugin，配合pyproject.toml配置文件使用

1. 插件并非一定要求`pytest_`开头，主要是用于识别这是一个`pytest`插件
2. `pyproject.toml`里面的`classifiers`也类似，并非一定需要