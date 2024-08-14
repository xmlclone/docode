"""
1. 列延迟加载: https://docs.sqlalchemy.org/en/20/orm/queryguide/columns.html#orm-queryguide-column-deferral
2. mapped_column参数: https://docs.sqlalchemy.org/en/20/orm/mapping_api.html#sqlalchemy.orm.mapped_column
"""


from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Table, Column, String, Integer
from sqlalchemy.schema import CreateTable


DB_URI = "sqlite+pysqlite:///:memory:"
ECHO = False
engine = create_engine(
    DB_URI, 
    echo=ECHO,  # 输出 sqlalchemy 日志
)


class Base(DeclarativeBase):
    pass


class Demo(Base):
    __tablename__ = 'demo'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(
        # 第一个参数可以自定义列名称,否则列名自动映射为变量名
        # 在使用对象进行操作的时候,仍然使用变量名进行操作, 比如 demo.name 而不是 demo.user_name
        "user_name",

        # 类型参数, 可以是第一个参数或这里的第二个参数 
        String(10), 
        
        # nullable 默认值导致此字段生成 NOT NULL
        # False None 均会生成 NOT NULL
        nullable=None,

        # 指定 True 后, 对应列的数据可以延迟加载(使用时才加载),以便节约时间和内存(一般针对此列数据量较大时可以使用)
        deferred=True,
    )


# 可以直接在类里面通过设置 __table__ 一个 Table 对象的方式
# 对于查询后的对象,仍然可以通过 Demo1.id Demo1.name 等方式访问
demo1_table = Table(
    'demo1',
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(10))
)

class Demo1(Base):
    __table__ = demo1_table

    # 当然也可以直接使用下面的方式
    """
    __table__ =  Table(xxx)
    """


print(CreateTable(Demo.__table__)) # type: ignore


Base.metadata.create_all(engine)
with Session(engine) as session:
    demo1 = Demo1(name="demo1-name1")
    session.add(demo1)
    session.commit()
    ret = session.scalars(
        select(Demo1)
    ).one()
    print(ret.name) # type: ignore