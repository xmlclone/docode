from dataclasses import dataclass


# 自动添加了 __init__ __repr__ __str__
# 当然也可以通过参数指定一些行为， 比如 init=False 则不会自动增加 __init__ 
# https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
@dataclass
class User:
    name: str
    age: int


user1 = User("lin", 18)
print(f"{user1.name=}, {user1.age=}, {user1!r}, {user1!s}")