"""
1. validator: https://docs.pydantic.dev/latest/concepts/validators/
2. field_validator: https://docs.pydantic.dev/latest/concepts/validators/#field-validators
"""


from pydantic import BaseModel, field_validator


class User(BaseModel):
    name: str
    # short_name: str
    # full_name: str
    age: int

    @field_validator('age')
    @classmethod
    def age_must_valid(cls, age: int) -> int:
        if age < 0:
            return 0
        return age
    

user1 = User(name='lin', age=-1)
print(user1)