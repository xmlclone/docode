"""
1. sqlalchemy.select insert等: https://docs.sqlalchemy.org/en/20/tutorial/data.html
2. where的 AND 和 OR: https://docs.sqlalchemy.org/en/20/tutorial/data_select.html#the-where-clause
"""


import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy import String
from sqlalchemy import select, insert, update, delete, bindparam
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy.orm import mapped_column, Mapped

from typing import List


DB_URI = "sqlite+pysqlite:///:memory:"
ECHO = False
engine = create_engine(
    DB_URI, 
    echo=ECHO,  # 输出 sqlalchemy 日志
)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(10))


Base.metadata.create_all(engine)
user_table = User.__table__


# insert  *******
stmt = insert(user_table).values(name="name") # type: ignore
print(stmt)
compiled = stmt.compile()
print(compiled)
print(compiled.params)

with engine.connect() as conn:
    result: sqlalchemy.engine.cursor.CursorResult = conn.execute(stmt) # type: ignore
    # inserted_primary_key 返回插入的 id , 注意是元组,且只有一条数据时有效
    # 比如下面插入了多条数据则无法获取此值
    print(result, result.inserted_primary_key)

    # 也可以一次性插入多条数据
    result: sqlalchemy.engine.cursor.CursorResult = conn.execute( # type: ignore
        insert(user_table), # type: ignore
        [
            {"name": "name1"},
            {"name": "name2"}
        ]
    )

    # 另外一种方式
    result: sqlalchemy.engine.cursor.CursorResult = conn.execute( # type: ignore
        insert(user_table).values( # type: ignore
            [
                {"name": "name1"},
                {"name": "name2"}
            ]
        ) 
    )
    conn.commit()


# select *******
# select的第一个参数可以是 Table 对象, 也可以是 ORM 对象
# 可以结合 demo4_ddl_orm.py 示例查看
stmt = select(user_table).where(user_table.c.name == "name")
with engine.connect() as conn:
    # conn.execute 在执行 select 后返回的是一个类似迭代器的对象
    # 迭代器的每个元素是元组,就算你只选择了一个列,仍然是元组
    for row in conn.execute(stmt):
        # 直接获取到的是值, 比如 (1, 'name'), 注意和orm的区别
        print(row)

    # execute 返回类型
    result: sqlalchemy.engine.cursor.CursorResult = conn.execute(stmt) # type: ignore
    print(result)

    # 选择部分列
    stmt = select(user_table.c.name)
    # 注意返回的迭代器的每个元素仍然是元组
    for row in conn.execute(stmt):
        print(row)

    # 选择部分列
    stmt = select(user_table.c.name, user_table.c.id)
    # 注意返回的迭代器的每个元素仍然是元组
    for row in conn.execute(stmt):
        print(row)
    
    # 只获取第一条数据, 注意返回值类型
    result: sqlalchemy.engine.row.Row = conn.execute(stmt).first() # type: ignore
    print(type(result), result.name) # type: ignore

    # 获取所有数据
    results: List[sqlalchemy.engine.row.Row] = conn.execute(stmt).all() # type: ignore
    print(type(results), type(results[0]))

# update *******
    

# delete  *******