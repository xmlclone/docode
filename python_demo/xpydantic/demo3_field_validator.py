"""
1. validator: https://docs.pydantic.dev/latest/concepts/validators/
2. field_validator: https://docs.pydantic.dev/latest/concepts/validators/#field-validators
"""


from typing import Optional, Self
from pydantic import BaseModel, field_validator, model_validator


class User(BaseModel):
    name: str
    # short_name: str
    # full_name: str
    age: int
    short_name: Optional[str] = ''

    @field_validator('age')
    @classmethod
    def age_must_valid(cls, age: int) -> int:
        if age < 0:
            return 0
        return age
    
    # 可以修改/设置对象 self 的某些属性
    @model_validator(mode='after')
    def convert_2shortname(self) -> Self:
        self.short_name = self.name
        return self
    

user1 = User(name='lin', age=-1)
print(user1)