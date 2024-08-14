from typing import List
from typing import Optional
from typing import Union

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy import text
from sqlalchemy import Connection
from sqlalchemy import Result
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session


ECHO = True
WAIT = False

def xinput(msg):
    if WAIT:
        input(msg)
    else:
        print(msg)


class Base(DeclarativeBase):
    pass


# https://docs.sqlalchemy.org/en/20/orm/quickstart.html
class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"
    

# 第一个参数是数据库连接URL，包括以下几个关键数据
# 包括dialect 也就是数据库类型
# 数据库DBAPI，可以省略
# 数据库连接地址
engine = create_engine("sqlite+pysqlite:///demo0.db", echo=ECHO)


# 创建表
Base.metadata.drop_all(engine) # 先删除
Base.metadata.create_all(engine)


# 创建对象
with Session(engine) as session:
    spongebob = User(
        name="spongebob",
        fullname="Spongebob Squarepants",
        addresses=[Address(email_address="spongebob@sqlalchemy.org")],
    )
    sandy = User(
        name="sandy",
        fullname="Sandy Cheeks",
        # sandy关联了两个地址
        addresses=[
            Address(email_address="sandy@sqlalchemy.org"),
            Address(email_address="sandy@squirrelpower.org"),
        ],
    )
    patrick = User(name="patrick", fullname="Patrick Star")
    session.add_all([spongebob, sandy, patrick])
    # with里面仍然只会调用close，不会主动调用commit，需要我们自行调用
    session.commit()


# 查询
session = Session(engine)
stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))
for user in session.scalars(stmt):
    print(user)


# join查询
stmt = (
    select(Address)
    .join(Address.user)
    .where(User.name == "sandy")
    .where(Address.email_address == "sandy@sqlalchemy.org")
)
sandy_address = session.scalars(stmt).one()
print(sandy_address)


# update
stmt = select(User).where(User.name == "patrick")
patrick = session.scalars(stmt).one()
patrick.addresses.append(Address(email_address="patrickstar@sqlalchemy.org"))
# sandy有两个地址，这里只更新了一个
sandy_address.email_address = "sandy_cheeks@sqlalchemy.org"
session.commit()


# delete
sandy: Union[User, None] = session.get(User, 2)
if sandy:
    sandy.addresses.remove(sandy_address)
xinput("removed")
# flush会在当前session里面体现并看见效果，而在其它session里面无法看见(即其它连接数据库的人看不见变动)
# commit会提交到数据库，所有人都可以看见效果
session.flush()
xinput("flushed")
session.delete(patrick)
xinput("deleted")
session.commit()
xinput("committed")


# ==============================================下面基本是ORM的底层原理==============================================================
# 注意engine是必须的 engine = create_engine("sqlite+pysqlite:///demo0.db", echo=ECHO)


# https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html#tutorial-working-with-transactions
# 直接使用Connection和Result对象
# engine.connect()也支持with，会自动调用close
conn: Connection = engine.connect()
# 有变更，也需要使用conn.commit()提交事务
# 但是如果使用 with engine.begin() 会自动commit
result: Result = conn.execute(text("select email_address, user_id from address"))
# print(result.all())
# 还可以通过元组的方式解析结果，比如 for email_address, user_id in result:
# 也可以通过索引的方式访问，比如 for row in result: email_address = row[0]
# 也可以通过属性的方式访问
for row in result:
    print(row.email_address, row.user_id)
conn.close()
# session也不仅仅是使用上面的session.scalars方式，还可以使用session.execute执行通过text包装后的语句
result: Result = session.execute(text("select email_address, user_id from address"))
for row in result:
    print(row.email_address, row.user_id)


# https://docs.sqlalchemy.org/en/20/tutorial/metadata.html#tutorial-working-with-metadata
metadata_obj = MetaData()
# 还记得上面通过继承 Base(DeclarativeBase) 类的ORM类吗？
user_table = Table(
    "user_account1",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String),
)
address_table = Table(
    "address1",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_account1.id"), nullable=False),
    Column("email_address", String, nullable=False),
)
# 访问Column相关属性，需要通过table.c这个实例去访问
# user_table.c.name=Column('name', String(length=30), table=<user_account1>)
# user_table.c.fullname=Column('fullname', String(), table=<user_account1>)
# user_table.c.keys()=['id', 'name', 'fullname']
# user_table.primary_key=PrimaryKeyConstraint(Column('id', Integer(), table=<user_account1>, primary_key=True, nullable=False))
print(f"{user_table.c.name=}\n{user_table.c.fullname=}\n{user_table.c.keys()=}\n{user_table.primary_key=}")
# 还记得上面通过Base.metadata进行的表操作吗？和这里的metadata_obj其实都是Metadata的实例
# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)
metadata_obj.drop_all(engine)
metadata_obj.create_all(engine)
# User.__table__其实就是一个Table的实例
print(f"{User.__table__=}\n{User.__tablename__=}")

session.close()