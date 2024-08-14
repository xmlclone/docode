import functools


# 可以装饰一个类，并自动填充用于比较相关的魔术函数，此类的实例就可以进行正常的数学比较
# 但是其内部必须定义至少一个__lt__(), __le__(), __gt__(), or __ge__()
@functools.total_ordering
class Class1:
    def __lt__(self, other: "Class1"):
        ...


# functools.wraps 参考 deco_demo0.py