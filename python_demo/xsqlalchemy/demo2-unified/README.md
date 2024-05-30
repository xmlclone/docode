# URI

1. 支持的数据库: https://docs.sqlalchemy.org/en/20/dialects/index.html

## sqlite

```sh
# python默认的sqlite库: https://docs.sqlalchemy.org/en/20/dialects/sqlite.html#dialect-sqlite-pysqlite-connect
sqlite+pysqlite:///file_path
# relative path
e = create_engine('sqlite:///path/to/database.db')
# absolute path
e = create_engine('sqlite:////path/to/database.db')
# absolute path on Windows
e = create_engine('sqlite:///C:\\path\\to\\database.db')
# in-memory database
e = create_engine('sqlite://:memory:')
# also in-memory database
e2 = create_engine('sqlite://')

# 其它: https://docs.sqlalchemy.org/en/20/dialects/sqlite.html
```

## pgsql

```sh
# https://docs.sqlalchemy.org/en/20/dialects/postgresql.html#dialect-postgresql-psycopg2-connect
postgresql+psycopg2://user:password@host:port/dbname

# https://docs.sqlalchemy.org/en/20/dialects/postgresql.html#dialect-postgresql-psycopg-connect
postgresql+psycopg://user:password@host:port/dbname

# 其它: https://docs.sqlalchemy.org/en/20/dialects/postgresql.html
```

## example

```python
from sqlalchemy import create_engine


DB_URI = "sqlite+pysqlite:///:memory:"
ECHO = False
engine = create_engine(
    DB_URI, 
    echo=ECHO,  # 输出 sqlalchemy 日志
)
```

# core and orm

`Connection.execute()` in Core and `Session.execute()` in ORM