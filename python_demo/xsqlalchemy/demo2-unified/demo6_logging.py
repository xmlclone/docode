"""
1. https://docs.sqlalchemy.org/en/20/core/engines.html#dbengine-logging
"""


# 使用的是python标准的logging模块


import logging


logging.getLogger('sqlalchemy')


""" 下面logger的不同功能

# 构造sql语句, logging.INFO 输出 SQL query
# logging.DEBUG 输出 SQL 和 Result
# 可以在 create_engine(echo=True) 表示 Info , create_engine(echo="debug") 表示 DEBUG
sqlalchemy.engine  


# 连接池相关日志，可以通过 create_engine 的 pool_echo 设置
sqlalchemy.pool

sqlalchemy.dialects
sqlalchemy.orm
"""

# 最简单的配置方式举例
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)