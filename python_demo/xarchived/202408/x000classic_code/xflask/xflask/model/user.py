import logging

from typing import Optional, Literal, Self, Union
from datetime import date, datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Column, JSON
from pydantic import Field, model_validator, field_validator
from pydantic.dataclasses import dataclass
from werkzeug.security import generate_password_hash

from .base import PyBase, DbBase
from ..constant import UserRole
from ..type import str_11, str_30, str_60, str_120, str_240


logger = logging.getLogger(__name__)


@dataclass
class NameDict:
    first_name: str_30
    last_name: str_30


class UserPy(PyBase):
    # id: Optional[int] = Field(
    #     # https://docs.pydantic.dev/latest/concepts/fields/#exclude
    #     # 如果设置为 True, 在导出的时候(比如 UserPy.model_dump())时，此字段不会被导出
    #     # 这里设置为 True, 是因为在新增数据时如果指定了此值(具有默认值 0)的情况下，让数据库的 id 字段可以自增，否则指定了就没法自增了
    #     exclude=True,
    #     default=0
    # )
    # 注意，这里如果设置了 exclude=True, 虽然解决了 id 无法设置的情况，但导出或响应的数据也会不包含此数据
    # 故这里可以给定默认值，在 model_dump 时指定参数 exclude_none=None 来避免此情况
    # 这样，即可以在 UserPy 转 UserDB 时某些值(比如 id 和 register_time)让 UserDB 自行处理
    # 又可以在导出 UserPy 数据时得到 id 和 register_time 返回给用户
    first_name: str_30
    last_name: str_30
    # 虽然设置为 Optional ，但是必须配合 Field 使用，否则在实例化时，此字段仍然会提示是必选的
    full_name: Optional[str_60] = Field(default=None)
    password: Optional[str_240] = Field(default=None)
    birthdate: date
    gender: Literal['male', 'female']
    phone: Optional[str_11] = Field(default=None)
    address: Optional[str_120] = Field(default=None)
    email: Optional[str_30] = Field(default=None)
    # 同样，这个字段只能让数据库自行处理，而不是用户传递，使用 exclude=True 后，就算用户传递了也无效，因为不会被导出
    # register_time: Optional[datetime] = Field(exclude=True, default=None)
    register_time: Optional[datetime] = None
    name_dict: Optional[NameDict] = None
    role: Optional[UserRole] = Field(default=UserRole.user)

    @model_validator(mode='after')
    def get_full_name(self) -> Self:
        self.full_name = f"{self.first_name}{self.last_name}"
        self.name_dict = NameDict(self.first_name, self.last_name)
        return self
    
    @field_validator('birthdate')
    def validator_birthdate(cls, value: Union[date, str]) -> date:
        # logger.debug(f"{value=}, {type(value)=}")
        if isinstance(value, date):
            return value
        return datetime.strptime(value, "%Y-%m-%d")
    
    @field_validator('password')
    def validator_password(cls, value: str) -> str:
        return generate_password_hash(value)


class UserDB(DbBase):
    __tablename__ = 'user'

    # https://docs.sqlalchemy.org/en/20/orm/mapping_api.html#sqlalchemy.orm.mapped_column
    first_name: Mapped[str_30] = mapped_column(String(30), nullable=False)
    # nullable = False
    last_name: Mapped[str_30] = mapped_column(String(30), nullable=False)
    full_name: Mapped[str_60] = mapped_column(
        String(60),
        # mapped_column 的 nullable (在 primary_key 为 True 时默认 False, 其它情况默认 True) 优先级高于 Mapped 注解
        # Mapped 注解配合 Optional 表示此字段是否可以为 Null
        nullable=True,
        unique=True,
    )
    password: Mapped[str_120] = mapped_column(String(240), nullable=False)
    birthdate: Mapped[date]
    gender: Mapped[Literal['male', 'female']]
    # nullable = True
    phone: Mapped[Optional[str_11]] = mapped_column(String(11))
    email: Mapped[Optional[str_30]] = mapped_column(String(30))
    address: Mapped[Optional[str_120]] = mapped_column(String(120))
    register_time: Mapped[datetime] = mapped_column(default=datetime.now)
    # JSON格式类型字段
    name_dict = Column('name_dict', JSON, nullable=True)
    role: Mapped[UserRole] = mapped_column(default=UserRole.user)

    def __str__(self) -> str:
        return f"{self.full_name}({self.role}-{self.deleted})"
    
    __repr__ = __str__

