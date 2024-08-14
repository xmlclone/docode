"""
1. mapped_column参数: https://docs.sqlalchemy.org/en/20/orm/mapping_api.html#sqlalchemy.orm.mapped_column
2. 几个default相关参数: https://docs.sqlalchemy.org/en/20/faq/ormconfiguration.html#what-are-default-default-factory-and-insert-default-and-what-should-i-use
"""

import datetime

from sqlalchemy import create_engine, select, insert, update
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Table, Column, String, Integer
from sqlalchemy.schema import CreateTable


DB_URI = "sqlite+pysqlite:///:memory:"
ECHO = False
ECHO = True
engine = create_engine(
    DB_URI, 
    echo=ECHO,  # 输出 sqlalchemy 日志
)


class Base(DeclarativeBase):
    pass


def default_func():
    return datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S.%f")


class Demo(Base):
    __tablename__ = 'demo'

    id: Mapped[int] = mapped_column(primary_key=True)

    demo: Mapped[str] = mapped_column(
        # True 表示是表的 primary key, 默认 False
        primary_key=False,

        # 表示此字段是否允许 NULL
        # 如果未指定此参数，并且字典有注解，使用注解的 NULL 和 NOT NULL (mapped_column 的参数 nullable 如果指定了则优先级高于 Mapped)
        # 如果未指定此参数，默认是 True ，即允许 NULL
        # 但如果指定了 primary_key=True ， 则此参数默认为 False
        nullable=True,

        # 如果指定为 True ，则表示此列可以延迟加载，当此字段的数据量较大时建议使用，以便于节约时间和内存
        deferred=False,

        # default 参数可以使用固定值，也可以指定一个可调用对象，在插入新行但是没有提供此参数时会使用到default参数
        # default='demo',
        default=default_func,
        # 区别后续补充
        # insert_default=2,
        # default_factory=3,
    )

    name: Mapped[str]


Base.metadata.create_all(engine)


with engine.connect() as conn:
    conn.execute(
        insert(Demo).values([{"name": "lin1"}, {"name": "lin2"}])
    )
    conn.commit()
    result = conn.execute(select(Demo)).all()
    print(result)
    print('-' * 100)

    conn.execute(
        update(Demo).where(Demo.id == 1).values(name="lin3")
    )
    conn.commit()
    result = conn.execute(select(Demo)).all()
    print(result)
    print('-' * 100)