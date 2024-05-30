from sqlalchemy import create_engine, inspect
from sqlalchemy import MetaData
from sqlalchemy import ForeignKey
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


DB_URI = "sqlite+pysqlite:///:memory:"
ECHO = False
engine = create_engine(
    DB_URI, 
    echo=ECHO,  # 输出 sqlalchemy 日志
)


metadata_obj = MetaData()


user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String),
)


# user_table.c 其实表示的就是 Column 对象，c.name 就是访问的 数据表 user_account 的 name 列
# user_account.name, Column('name', String(length=30), table=<user_account>)
print("{!s}, {!r}".format(user_table.c.name, user_table.c.name))
# user_account.fullname, Column('fullname', String(), table=<user_account>)
print("{!s}, {!r}".format(user_table.c.fullname, user_table.c.fullname))
# ['id', 'name', 'fullname']
print(user_table.c.keys())


address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_account.id"), nullable=False),
    Column("email_address", String, nullable=False),
)


# 创建表
# 会自动创建所有和 metadata_obj 关联的表
metadata_obj.create_all(engine)


# ::: metadata
# 基于ORM对象定义的时候，DeclarativeBase 对象自动帮我们创建了一个类属性 metadata
# 即 DeclarativeBase.metadata 就是一个上面定义过的 MetaData() 对象
# 这样我们就可以直接定义基于对象的表
# ::: registry
class Base(DeclarativeBase):
    ...


# ::: __table__
# 每个类，比如 User ，其实会根据类的定义生成对应的 Table 对象，就是 __table__ 这个属性
# 这个 User 的 __table__ 属性和上面定义的 user_table 可以看成是等价的
class User(Base):
    __tablename__ = "user_account"

    # mapped_column 会生成 Column 对象，比如 id 可以看成等价于上面 user_table 的 Column("id", Integer, primary_key=True) 参数
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    addresses: Mapped[List["Address"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id = mapped_column(ForeignKey("user_account.id"))
    user: Mapped[User] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"
    

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# 可以直接访问类的 __table__
# 下面三者都是 Table 对象
print("{!r}".format(user_table))
print("{!r}".format(User.__table__))
print("{!r}".format(inspect(User).local_table))