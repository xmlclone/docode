"""
演示 pydantic 递归类型时，把对应的类型转换为 sqlalchemy 的 JSON存储
"""


from typing import List, Optional
from datetime import datetime
from sqlalchemy import Column, JSON
from sqlalchemy.orm import mapped_column, Mapped
from pydantic import Field
from enum import Enum
from typing import Annotated, Optional
from datetime import datetime
from pydantic import field_serializer
from pydantic.dataclasses import dataclass
from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Session
from pydantic import BaseModel, ConfigDict


DB_ENGINE = create_engine("sqlite+pysqlite:///:memory:", echo=True)
SESSION = Session(DB_ENGINE)


class DB_BASE(DeclarativeBase):
    ...


class MD_BASE(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True,
    )


str_30 = Annotated[str, 30]
str_100 = Annotated[str, 100]


class ResultEnum(Enum):
    Failure = 'Failure'
    Success = 'Success'
    NotExecuted = 'NotExecuted'


@dataclass
class Step:
    id: int
    title: str_100
    start_time: datetime
    end_time: datetime
    result: ResultEnum
    error_message: Optional[str] = ''

    # 由于 Step 属于 ExcutionRecordModel 的一个属性 steps
    # 需要把 steps 转换为 ExcutionRecord 可以识别的 JSON格式
    # 如果不序列化 datetime 和 ResultEnun ，无法直接写入数据库
    # 故这里把上面两种类型的属性都序列化一次，相当于转换为 str
    # 此时就可以正常把 steps 作为 json 格式写入数据库
    # 从数据库读取数据后，不需要反序列化，会使用默认的反序列化操作为可识别的对象
    @field_serializer('start_time', 'end_time')
    def serializer_dt(self, dt: datetime, _info):
        return str(dt)
    
    @field_serializer('result')
    def serializer_result(self, result: ResultEnum, _info):
        return result.value


class ExcutionRecord(DB_BASE):
    __tablename__ = 'excution_record'

    id: Mapped[int] = mapped_column(primary_key=True)
    # 项目名
    project: Mapped[str_30]
    # 场景名
    scene: Mapped[str_100]
    # 测试步骤
    steps = Column('steps', JSON, nullable=False)
    # 场景启动时间
    start_time: Mapped[datetime]
    # 场景结束时间
    end_time: Mapped[datetime]
    # 结果
    result: Mapped[Optional[ResultEnum]] = mapped_column(default=ResultEnum.NotExecuted)
    # 错误消息
    error_message: Mapped[Optional[str]] = mapped_column(default='')


class ExcutionRecordModel(MD_BASE, extra='forbid'):
    id: Optional[int] = Field(exclude=True, default=0)
    project: str_30
    scene: str_100
    steps: List[Step]
    start_time: datetime
    end_time: datetime
    result: ResultEnum = Field(default=ResultEnum.NotExecuted)
    error_message: Optional[str] = ''



if __name__ == '__main__':
    step1 = Step(
        id=1,
        title='test-step',
        start_time=datetime.now(),
        end_time=datetime.now(),
        result=ResultEnum.Success,
    )

    m = ExcutionRecordModel(
        project='test-project',
        scene='test-scene',
        steps=[step1],
        start_time=datetime.now(),
        end_time=datetime.now(),
        result=ResultEnum.Success
    )
    print(m)

    o = ExcutionRecord(**m.model_dump())
    print(o)
    SESSION.add(o)
    SESSION.commit()

    result = SESSION.scalars(
        select(ExcutionRecord)
    ).one()
    print(result)

    m1: ExcutionRecordModel = ExcutionRecordModel.model_validate(result)
    print(m1)
    print(type(m1.steps[0].start_time))
