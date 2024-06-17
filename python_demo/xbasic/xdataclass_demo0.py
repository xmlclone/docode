from typing import Optional, List
from datetime import datetime
from dataclasses import dataclass, field, fields, asdict, astuple
# python 3.10 增加 KW_ONLY
from dataclasses import KW_ONLY


# 自动添加了 __init__ __repr__ __str__
# 当然也可以通过参数指定一些行为， 比如 init=False 则不会自动增加 __init__ 
# https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
@dataclass
class User:
    name: str
    age: int

user1 = User("lin", 18)
print(f"{user1.name=}, {user1.age=}, {user1!r}, {user1!s}")


# dataclass 可以具有参数
@dataclass()
class User2:
    # 也可以使用 field 方法指定属性的某些特性
    user: User
    name: Optional[str] = field(default=None)
    age: int = field(default_factory=lambda : 0)

user2 = User2(user=user1)
# asdict(user2)={'user': {'name': 'lin', 'age': 18}, 'name': None, 'age': 0}, astuple(user2)=(('lin', 18), None, 0)
# 即 asdict astuple 可以自动的递归处理
print(f"{user2=}, {asdict(user2)=}, {astuple(user2)=}")

# fields 会返回由 Field 对象组成的列表
# Field 不应该被自己定义或初始化(即通常情况不应该主动使用 Filed 类)
print('-' * 100)
print(f"{fields(user2)=}")
print('-' * 100)


# 如果使用 init=False 则不会自动生成 __init__
# 如果类本身定义了 __init__ ， 此参数会被忽略(不管是 True 还是 False)
@dataclass(init=False)
class User3:
    name: str
    age: int

    def __init__(self) -> None:
        self.name = 'lin'
        self.age = 18

user3 = User3()
print(user3)


@dataclass
class User4:
    name: str
    age: int

    # 初始化后处理
    def __post_init__(self):
        self.age = 18

    # 等价于下面的代码
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    #     self.__post_init__()

user4 = User4(name='lin', age=0)
print(user4)


@dataclass
class User5:
    name: str
    # 可以不自动在 __init__ 中使用
    age: int = field(init=False)

    # 此时可以配合 __post_init__ 应用
    def __post_init__(self):
        self.age = 18

user5 = User5('lin')
print(user5)


# 默认情况下，生成的 __init__ 的参数会根据定义的顺序去访问属性
# 但如果指定了 kw_only 则会生成一个类似 __init__(self, age: int, *, name: str) 的方法，即 name 必须通过 kw 的方式去初始化值
@dataclass
class User6:
    name: str = field(kw_only=True)
    age: int

user6 = User6(10, name='lin')


@dataclass
class User7:
    name: str
    # 同理，我们可以设定一个如下的代码，则后续定义的所有属性都需要通过 kw 的方式去初始化
    _: KW_ONLY
    age: int
    birthday: datetime

# 在继承中，会从父类的定义开始往下初始化
# 但如果子类有重写父类属性，则以子类为准
# 并且 kw 会影响初始化参数的顺序
    
# 现在可以理解 filed 的 default_factory 参数，它是一个不带参数的可调用对象
# 其实也就是在 __init__ 中被调用了
@dataclass
class User8:
    name: str
    lagus: List[str] = field(default_factory=list)

    # 默认 __init__ 等价于下面代码
    def __init__(self, name: str, lagus: List[str]=list()):
        self.name = name
        self.lagus = lagus

user8 = User8('lin')
user8.lagus.append('python')
user8.lagus.append('java')
print(user8)


# 如果某个字段被排除在 init 之外，则等价的代码如下
@dataclass
class User9:
    name: str
    lagus: List[str] = field(init=False, default_factory=list)

    # 默认 __init__ 等价于下面代码
    def __init__(self, name: str):
        self.name = name
        self.lagus = list()

user9 = User9('lin')
user9.lagus.append('python')
user9.lagus.append('java')
print(user9)

