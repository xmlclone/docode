"""
select

https://docs.sqlalchemy.org/en/20/orm/queryguide/select.html
https://docs.sqlalchemy.org/en/20/tutorial/data_select.html#tutorial-selecting-data
"""

from typing import List
from typing import Optional

from sqlalchemy import insert
from sqlalchemy import update
from sqlalchemy import delete
from sqlalchemy import select
from sqlalchemy import bindparam
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import and_
from sqlalchemy import or_
from sqlalchemy import func

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session


ECHO = False
WAIT = True


def xinput(msg):
    if WAIT:
        input(msg)
    else:
        print(msg)


class Base(DeclarativeBase):
    pass


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


with Session(engine) as session:
    session.execute(
        insert(User),
        [
            {"name": "sandy", "fullname": "Sandy Cheeks"},
            {"name": "patrick", "fullname": "Patrick Star"},
            {"name": "spongebob", "fullname": "Spongebob Squarepants"}
        ]
    )
    session.commit()

    add1 = Address(email_address="sandy@sqlalchemy.org", user_id=1)
    add2 = Address(email_address="patrick@sqlalchemy.org", user_id=2)
    add3 = Address(email_address="spongebob@sqlalchemy.org", user_id=3)
    add4 = Address(email_address="sandy@squirrelpower.org", user_id=1)
    session.add_all([add1, add2, add3, add4])
    session.commit()


with Session(engine) as session:
    # 最基础的一个查询
    user = session.get(User, 1)
    print(f"{user=}\n")


    result = session.execute(
        select(User).where(User.name == "sandy")
    )
    # result.one scalar first all scalars
    # result.one 和 result.scalar 使用后，都会导致result对象关闭(即不能再次使用)
    # result.one 和 result.scalar 都返回一个对象
    # result.all 返回一个列表，使用后，还可以使用result
    # result.scalar 对应有一个 result.scalars
    # print(f"{result.one()=}")
    # print(f"{result.all()=}")
    # 当然result可以直接被遍历，并且每行可以使用 索引[0] 对象. 字典['User'] 等几种方式进行数据访问
    print(f"{result.scalar()=}\n")


    result = session.execute(
        select(User).order_by(User.name)
    )
    for user in result.scalars():
        print(user)
    print('\n')


    result = session.execute(
        select(User, Address).join(User.addresses).order_by(User.id, Address.id)
    )
    for row in result:
        print(f"{row=} {row.User=} {row.Address=}")
    print('\n')


    result = session.execute(
        select(User.name)
    )
    for row in result:
        print(f"{row=} {row.name=}")
    print('\n')


    # 下面直接查看sql语句演示即可，不对返回值进行说明
    # where表达式里面常用的 == > < 就不在演示 
    # in
    print(select(User).where(User.name.in_(['sandy', 'patrick'])), end='\n\n')
    # and
    print(select(User).where(User.name == "sandy").where(User.id == 1), end='\n\n')
    # 下面也是and
    print(select(User).where(User.name == "sandy", User.id == 1), end='\n\n')
    # or
    print(select(User).where(or_(User.name == "sandy", User.id == 2)), end='\n\n')
    # and or
    print(select(User).where(
        and_(
            or_(User.id == 1, User.name == "sandy"),
            User.fullname == "Sandy Cheeks"
        )
    ), end='\n\n')
    
    # 除了where，还可以使用filter
    print(select(User).filter_by(name="sandy", id=1), end='\n\n')

    # 另外 sqlalchemy.func 模块包含一些sql函数，比如count
    print(select(User, func.count()), end='\n\n')
    print(select(func.count()).select_from(User), end='\n\n')

    # 使用label可以给count列重命名
    print(
        select(User, func.count(User.id).label("count")).group_by(User.id),
        end='\n\n'
    )

    # count不传参，则表示使用 *
    print(
        select(User, func.count().label("count")).group_by(User.id).having(User.id > 1),
        end='\n\n'
    )