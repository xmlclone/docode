from typing import Optional, Literal, Annotated, Self
from datetime import date, datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from pydantic import Field, model_validator

from .base import PyBase, DbBase


str_11 = Annotated[str, 11]
str_30 = Annotated[str, 30]
str_60 = Annotated[str, 60]
str_120 = Annotated[str, 120]


class UserDB(DbBase):
    __tablename__ = 'user'

    # https://docs.sqlalchemy.org/en/20/orm/mapping_api.html#sqlalchemy.orm.mapped_column
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str_30] = mapped_column(String(30), nullable=False)
    # nullable = False
    last_name: Mapped[str_30] = mapped_column(String(30), nullable=False)
    full_name: Mapped[str_60] = mapped_column(
        String(60),
        # mapped_column 的 nullable (在 primary_key 为 True 时默认 False, 其它情况默认 True) 优先级高于 Mapped 注解
        # Mapped 注解配合 Optional 表示此字段是否可以为 Null
        nullable=True
    )
    birthdate: Mapped[date]
    gender: Mapped[Literal['male', 'female']]
    # nullable = True
    phone: Mapped[Optional[str_11]] = mapped_column(String(11))
    address: Mapped[Optional[str_120]] = mapped_column(String(120))
    register_time: Mapped[datetime] = mapped_column(default=datetime.now)


class UserPy(PyBase):
    id: Optional[int] = Field(
        # https://docs.pydantic.dev/latest/concepts/fields/#exclude
        # 如果设置为 True, 在导出的时候(比如 UserPy.model_dump())时，此字段不会被导出
        # 这里设置为 True, 是因为在新增数据时如果指定了此值(具有默认值 0)的情况下，让数据库的 id 字段可以自增，否则指定了就没法自增了
        exclude=True,
        default=0
    )
    first_name: str_30
    last_name: str_30
    # 虽然设置为 Optional ，但是必须配合 Field 使用，否则在实例化时，此字段仍然会提示是必选的
    full_name: Optional[str_60] = Field(default=None)
    birthdate: date
    gender: Literal['male', 'female']
    phone: Optional[str_11] = Field(default=None)
    address: Optional[str_120] = Field(default=None)
    # 同样，这个字段只能让数据库自行处理，而不是用户传递，使用 exclude=True 后，就算用户传递了也无效，因为不会被导出
    register_time: Optional[datetime] = Field(exclude=True, default=None)

    @model_validator(mode='after')
    def get_full_name(self) -> Self:
        self.full_name = f"{self.first_name} {self.last_name}"
        return self

