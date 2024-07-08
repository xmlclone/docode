from typing import Optional
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import BaseModel, ConfigDict


class Base(DeclarativeBase):
  pass
db = SQLAlchemy(model_class=Base)


class DbBase(db.Model):
  #  https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/customizing/#abstract-models-and-mixins
   __abstract__ = True

   id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
   delete: Mapped[bool] = mapped_column(default=False)


class PyBase(BaseModel, extra='forbid'): # https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.extra
    # extra 默认是 ignore
    # extra 也可以配置在下面的 ConfigDict 里面
    model_config = ConfigDict(
        #  https://docs.pydantic.dev/latest/concepts/models/#arbitrary-class-instances
        # https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.from_attributes
        from_attributes=True,
        # arbitrary_types_allowed=True, # https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.arbitrary_types_allowed
    )

    id: Optional[int] = None
    delete: Optional[bool] = False



