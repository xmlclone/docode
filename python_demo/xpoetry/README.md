1. 首页: https://pypi.org/project/poetry/0.8.0a4/
2. pyproject.toml配置: https://python-poetry.org/docs/pyproject/
3. 依赖: https://python-poetry.org/docs/dependency-specification/

```sh
pip install poetry

poetry new demo0
poetry install
poetry build
poetry publish

# 默认从0.1.0版本开始
# 没有操作之前，都会覆盖0.1.0，即没有使用 poetry version 之前，会保持之前配置的版本号
# 即 [tool.poetry] 下的 version 配置项会随此配置改变
# [tool.poetry] 下的 version 可以配置为 "git"，则会自动读取git tag生成版本
poetry version <version>
```