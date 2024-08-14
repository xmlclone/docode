"""
1. 列字段类型: https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#orm-declarative-mapped-column
2. Enum类型: https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#using-python-enum-or-pep-586-literal-types-in-the-type-map
3. JSON类型:
    https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#linking-specific-enum-enum-or-typing-literal-to-other-datatypes
    https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.JSON
"""


import datetime
import enum

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import BIGINT, Integer, NVARCHAR, String, TIMESTAMP, JSON, Column
from sqlalchemy.schema import CreateTable
from sqlalchemy import select
from typing import Optional, List, Annotated, Literal
# from typing_extensions import Annotated


DB_URI = "sqlite+pysqlite:///:memory:"
ECHO = False
engine = create_engine(
    DB_URI, 
    echo=ECHO,  # 输出 sqlalchemy 日志
)


# 新增类型，可以在 Mapped 标注里面使用 ***** 不是一定要在 type_annotation_map 定义了才能被使用,这里定义了就可以在 Mapped 里面应用
str_30 = Annotated[str, 30]
str_50 = Annotated[str, mapped_column(String(50), nullable=True)]
# 如果不在类的 type_annotation_map 增加各种限制，可以直接在外层增加
# 比如如果这里不使用 nullable = True ,那么在定义相关字段时是不能为空的, 即不能是 NULL
timestamp = Annotated[
    datetime.datetime,
    mapped_column(nullable=True),
]
# json格式1,需要配合 type_annotation_map 使用
my_literal = Literal["json"]

class Base(DeclarativeBase):
    # 可以自定义 Mapped 映射的类型
    # 这里把 str 映射为 String(40)
    # 那么下面使用 Mapped[str] 的字段都会默认成为 VARCHAR(40)
    # 但如果使用了 mapped_column(String(30)) 则仍然是 VARCHAR(30) , 比如下面Demo类的 data 默认就是 30, 而 nickname 仍然是 30
    type_annotation_map = {
        str: String(40),
        str_30: String(30),
        my_literal: JSON
    }

    """
    # 默认的映射如下，其中 types 是 from sqlalchemy import types
    # 即使用 Mapped 标注下无法使用以下 key 以外的类型，除非像上面一样定义了一个新的类型 str_30
    # 注意，新类型 str_30 和 timestamp 都是最上面的代码， type_annotation_map 只是增加了一定的约束，即 Mapped 标注的类型是类外面的类型，而不是 type_annotation_map 定义的类型

    from typing import Any
    from typing import Dict
    from typing import Type

    import datetime
    import decimal
    import uuid

    from sqlalchemy import types

    type_map: Dict[Type[Any], TypeEngine[Any]] = {
        bool: types.Boolean(),
        bytes: types.LargeBinary(),
        datetime.date: types.Date(),
        datetime.datetime: types.DateTime(),
        datetime.time: types.Time(),
        datetime.timedelta: types.Interval(),
        decimal.Decimal: types.Numeric(),
        float: types.Float(),
        int: types.Integer(),
        str: types.String(),
        uuid.UUID: types.Uuid(),

        enum.Enum: sqlalchemy.Enum(enum.Enum),
        typing.Literal: sqlalchemy.Enum(enum.Enum),
    }
    """


class Status(enum.Enum):
    success = 1
    fail = 0

Status1 = Literal["success", "fail"]


class Demo(Base):
    __tablename__ = 'demo'

    """ mapped_column 常用参数解释

    nullable 
    """

    # primary_key=True, therefore will be NOT NULL
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    # 没有 Optional[], 此字段不能为空
    # 不能为空表示sql语句必须传值，就算传空字符串''也行，但是不能传 None ，因为传 None 就和默认的不传一个意思了
    data: Mapped[str]
    # 有 Optional[], 没有其它限制，那么传啥都可以，或者直接不传都行
    data1: Mapped[Optional[str]]
    # 等同于 data
    data2: Mapped[Optional[str]] = mapped_column(nullable=False)
    # 等同于 data1, 即 mapped_column 的参数 nullable 优先级高于 Mapped
    data3: Mapped[str] = mapped_column(nullable=True)

    # 有 Optional[], 此字段可以为空
    additional_info: Mapped[Optional[str]]

    # 当然可以直接使用 mapped_column 映射(上面的方式相当于注解)
    # 注意此方式定义的字段默认是可以 NULL 的
    nickname = mapped_column(String(30))

    fullname: Mapped[str_30] = mapped_column(nullable=True)
    
    detail: Mapped[str_50]
    
    start_time: Mapped[timestamp]

    # enum对象
    # 会自动把 enum 的最长字段转换为对应的 数据库的类型,比如 sqlite 会被转换为 VARCHAR(7) ,因为 success 比 fail 长,而且长度是 7
    # 存储的就是对应的字符串,比如 success 和 fail ,而不是存的实际的值 1 或 0
    # 当然在构造数据的时候可以传 status 字段为非 Status 定义的值,并且也可以 add 到数据库,参考下面的 obj2 对象,但是无法直接取出来映射到对象里面(但可以通过下发sql语句取出来)
    status: Mapped[Status] = mapped_column(nullable=True)

    # 同理,可以使用 Literal ,在映射字段上和 Enum 特性基本一致
    # 也是 VARCHAR(7), 并且 可以增加不在 Literal 定义的内容,但是仍无法取出后映射到 ORM 对象上
    status1: Mapped[Status1] = mapped_column(nullable=True)
    # 更多 Enum 相关使用请参考: https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#using-python-enum-or-pep-586-literal-types-in-the-type-map

    # json_data: Mapped[JSON] , 存储json数据, 需要对应的数据库支持, 比如 sqlite 就支持 JSON
    json_data: Mapped[my_literal]
    # 另外一种 JSON 支持格式
    # 同时也表明可以在类定义里面混合使用 注解 Column mapped_column
    # 注意 Column 默认是可以 NULL的
    json_data2 = Column('json_data2', JSON)


# 打印创建表格的sql
"""
"""
print(CreateTable(Demo.__table__)) # type: ignore


Base.metadata.create_all(engine)
obj1 = Demo(data='', data1=None, data2='', status=Status.success, status1="fail", json_data={"k1": "true", "k2": "v2"}, json_data2={"k1": "true", "k2": "v2"})
# obj2 = Demo(data='', data1=None, data2='', status='abc', status1="abc")
with Session(engine) as session:
    session.add(obj1)
    # session.add(obj2)
    session.commit()
    ret = session.scalars(
        select(Demo).where(Demo.id == 1)
    ).one()
    # data 是空字符串, data1 和 data3 是 None , status 是 Status.success 这个对象, 可以通过 Enum.value 方式访问其值
    print(f"{ret.data=}, {ret.data1=}, {ret.data3=}, {ret.status=}, {ret.status.value=}, {ret.status1=}, {ret.json_data=}, {ret.json_data2=}")