from typing import List
from typing import Optional

from sqlalchemy import insert
from sqlalchemy import update
from sqlalchemy import delete
from sqlalchemy import bindparam
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session


"""
DDL
"""


ECHO = True
WAIT = True


def xinput(msg):
    if WAIT:
        input(msg)
    else:
        print(msg)


class Base(DeclarativeBase):
    pass


# https://docs.sqlalchemy.org/en/20/tutorial/data.html#working-with-data

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
    

engine = create_engine("sqlite+pysqlite:///demo0.db", echo=ECHO)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# 注意使用Base对象 和 Table对象的使用方式，都支持的
# 注意Session和engine.connect()也就是Connection对象的使用方式，都支持的
with Session(engine) as session:
    # insert 1
    # 注意这里的insert接收的参数，还可以是Table对象，参考demo0里面的Table对象
    stmt = insert(User).values(name="spongebob", fullname="Spongebob Squarepants")
    # 记得demo0里面使用text(sql)执行原始sql语句吗？
    result = session.execute(stmt)
    print(f"{result.inserted_primary_key=}")

    # insert 2
    user = User(name="lin", fullname="linlei")
    session.add(user)
    
    # insert 3 还有session.add_all()，这里未做示例代码，可以参考demo0

    # 一次性insert多个内容，类似于add_all
    session.execute(
        insert(User),
        [
            {"name": "sandy", "fullname": "Sandy Cheeks"},
            {"name": "patrick", "fullname": "Patrick Star"},
        ]
    )
    session.commit()

    
with Session(engine) as session:
    # update
    # 同理，这里update接收的参数，也可以是Table对象，只不过update的条件就不是User.name，而是table_name.c.name
    stmt = update(User).where(User.name == "patrick").values(fullname="Patrick the Star")
    session.execute(stmt)
    session.commit()
    xinput("updated1")

    # 一次性更新多条内容
    # stmt = update(User).where(User.name == bindparam("oldname")).values(name=bindparam("newname"))
    # session.execute(
    #     stmt,
    #     [
    #         {"oldname": "jack", "newname": "ed"},
    #         {"oldname": "wendy", "newname": "mary"},
    #         {"oldname": "jim", "newname": "jake"},
    #     ],
    # )
    # session.commit()
    # xinput("updated2")