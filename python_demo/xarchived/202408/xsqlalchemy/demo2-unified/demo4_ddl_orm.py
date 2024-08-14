"""
1. ORM查询: https://docs.sqlalchemy.org/en/20/orm/queryguide/index.html
2. where的 AND 和 OR: https://docs.sqlalchemy.org/en/20/tutorial/data_select.html#the-where-clause
"""


import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy import String
from sqlalchemy import select, insert, update, delete, bindparam
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy.orm import mapped_column, Mapped

from typing import List, Sequence


DB_URI = "sqlite+pysqlite:///:memory:"
ECHO = False
ECHO = True
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


# insert *******
with Session(engine) as session:
    user1 = User(name="name1")
    user2 = User(name="name2")
    session.add(user1)
    session.add(user2)
    user3 = User(name="name1")
    user4 = User(name="name2")
    session.add_all([user3, user4])
    session.commit()


# select *******
with Session(engine) as session:

    """
    select where 表达式

    User.name == "name1"
    User.id > 1

    where().where() 表示 AND
    where(a_condition, b_condition) 也表示 AND

    # OR 和 AND
    from sqlalchemy import and_, or_
    select().where(
        and_(
            a,
            _or(b, c)
        )
    )
    表示 a AND (b OR c)

    # like
    select().where(User.name.like("%name"))
    # not
    select().wehre(~User.name.like("%name"))
    """


    """
    select filter 表达式
    where 里面 比较相等需要使用 "==", filter则直接使用"="

    select().filter_by(name="xxx", id=xx)  # 表示 AND
    """

    stmt = select(User).where(User.name == 'name1')
    for row in session.execute(stmt):
        # 获取到的是 User 对象, 注意和 core 的区别
        print(row)

    # 注意 execute 和 scalars 返回类型的不同
    # 建议使用 scalars
    result1: sqlalchemy.engine.result.ChunkedIteratorResult = session.execute(stmt) # type: ignore
    print(result1)
    result2: sqlalchemy.engine.result.ScalarResult = session.scalars(stmt)
    print(result2)

    # 获取一条数据
    result3 = session.scalars(stmt).first()
    print(result3)

    # 获取所有数据
    results: Sequence[User] = session.scalars(stmt).all()
    print(results)

    stmt = select(User)
    users = session.scalars(stmt)
    for user in users:
        print(user)

    users = session.scalars(
        select(User).where(
            User.name == "name1"
        ).order_by(  # order_by 可以 指定字段,并且可以通过字段的 desc() 进行降序排列, 默认是升序 asc()
            User.id.desc()
        )
    )
    for user in users:
        print(user.id)

    # count
    print('--------------- count ---------------')
    result = session.scalars(
        select(func.count(User.name)).select_from(User)
    )
    for ret in result:
        print(ret)

    # group by
    print('--------------- group by ---------------')
    stmt = select(User.name, func.count(User.name).label('count')).group_by(User.name)
    result = session.scalars(stmt)
    # 注意 下面 ret 只是一个字符串,即只把 User.name 选取出来了, count无法使用
    # 参考下面使用 session.execute 的方式
    for ret in result:
        print(ret)

    result = session.execute(stmt)
    # 此方式可以获取到 select 的所有内容
    for ret in result:
        print(ret, ret.name, ret.count)


# update *******
    

# delete  *******