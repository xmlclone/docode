"""
1. docs: https://docs.pydantic.dev/latest/concepts/models/
2. api: https://docs.pydantic.dev/latest/api/base_model/
"""


import json

from datetime import datetime
from typing import Tuple, List

from pydantic import BaseModel, PositiveInt


class Delivery(BaseModel):
    timestamp: datetime
    dimensions: Tuple[int, int]

m = Delivery(timestamp=datetime.now(), dimensions=(10, 20))
print(f"{m.timestamp=}, {m.dimensions=}")
print('-' * 100)


class User(BaseModel):
    id: int  
    name: str = 'John Doe'  
    signup_ts: datetime | None  
    tastes: dict[str, PositiveInt]  

external_data = {
    'id': 123,
    'signup_ts': '2019-06-01 12:22',  
    'tastes': {
        'wine': 9,
        b'cheese': 7,  # 类似的如果类型和模型定义不一致的，会自动转换为模型的数据类型
        'cabbage': '1',   # 比如这里的 cabbage 在模型定义时是 PositiveInt 类型，这里虽然传递的是字符串，但是会被转换为整型
    },
}

user = User(**external_data)
print(f"{user.tastes.get('cabbage')=}")
print(user.model_dump())  # 返回的是字典
print(user.model_dump_json()) 
print('-' * 100)


class T1Model(BaseModel):
    users: List[str]

t1 = T1Model(users=['lin', 'lai'])
print(t1.model_dump_json()) # 返回的是json格式字符串，注意此方法会节省空间，从而导致部分格式不一致，比如缺少一定的空格，可以通过下面的方式导出好看的json格式
print(json.dumps(t1.model_dump())) # 可以输出查看两者的不同
# {"users":["lin","lai"]}
# {"users": ["lin", "lai"]}
print('-' * 100)


# model_validate*** 方法演示
# model_validate 可以传递字典或模型
# 如果配置有 from_attributes=True ， 还可以传递 orm 对象(当然其它对象也行)
t1 = T1Model.model_validate({'users': ['lin', 'lai']})
print(t1)
t1 = T1Model.model_validate(t1)
print(t1)
# 传递 json 字符串，注意 json 字符串内需要用双引号
t1 = T1Model.model_validate_json('{"users": ["lin", "lai"]}')
print(t1)
print('-' * 100)
