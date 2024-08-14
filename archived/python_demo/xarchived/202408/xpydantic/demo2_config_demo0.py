"""
1. ConfigDict: https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict
"""


from pydantic import BaseModel, ValidationError, ConfigDict, Field
from pydantic.dataclasses import dataclass


class TestModel1(BaseModel):
    # 定义模型的配置
    model_config = ConfigDict(
        str_max_length=10, str_min_length=5, # 限制字符串类型的长度
    )

    a: str

# 默认情况可以传递未定义的属性
t1 = TestModel1(a="lin992", b=20)  # type: ignore
print(t1)
print('-' * 100)

try:
    t1 = TestModel1(a="lin")
except ValidationError as e:
    print(e)
    print('-' * 100)

try:
    t1 = TestModel1(a="12345678901")
except ValidationError as e:
    print(e)
    print('-' * 100)


# extra: https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.extra
# 默认是 ignore ，即可以出现额外的属性，但是会被忽略
# forbid 是禁止出现额外的属性
# allow 是可以出现额外的属性，并且会成功转换成属性
class TestModel2(BaseModel, extra='forbid'):
    a: str

try:
    # 类可以增加额外的限制，传递 extra='forbid' 则不允许出现未定义的字段
    t2 = TestModel2(a="lin", b=20)  # type: ignore
except ValidationError as e:
    print(e)
    print('-' * 100)


# 也可以通过装饰器定义
config = ConfigDict(str_max_length=5)

@dataclass(config=config)
# 注意这里不在需要继承 BaseModel
class Model3:
    a: str

try:
    Model3(a='s123456')
except ValidationError as e:
    print(e)
    print('-' * 100)


class Model4(BaseModel):
    model_config = ConfigDict(
        # 默认 False ，即字段如果有别名，必须通过别名去配置模型；但是这里配置为 True 后，可以通过别名和变量名去设置属性
        # 注意：访问均只能通过变量名去访问
        populate_by_name=True,
        # 当初始化模型成功后，可以通过 m.x 的方式去修改属性，默认配置是 False ，如果属性的类型不正确不会出发异常
        # 当这里配置为 True 后，通过 m.x 方式去修改属性，如果类型不正确会抛出 ValidateionError
        validate_assignment=True,
        # 如果字段是 Enum 类型，默认 False 存储的是 Enum 对象
        # 如果设置为 True 后，会存储 Enum 的值，其实就是 Enum.value()
        use_enum_values=True,
        # 遍历对象的属性，并转换为本模型的属性，比如应用在ORM中
        from_attributes=True,
        # 
        loc_by_alias=True,
    )

    a: str = Field(alias='new_a')

m = Model4(a="C") # type: ignore
m1 = Model4(new_a='python')
# 均无法通过 new_a 访问属性，只能通过 a 去访问
print(m.a, m1.a) # type: ignore
print('-' * 100)