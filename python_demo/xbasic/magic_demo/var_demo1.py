"""This is module doc.

TODO: 如何根据一个函数或类获取到它所属文件的全路径？


文件/模块级别的
    __name__  可能有__main__和模块名的名称
    __file__  文件全路径
    __doc__
    __annotations__ dict 文件/模块级别的全局标注，比如下面的 `G_VAR1`

函数级别的
    __globals__
    __closure__
    __doc__
    __name__
    __qualname__
    __module__
    __defaults__ tuple
    __code__
    __dict__
    __annotations__   dict 形参的标注
    __kwdefaults__ dict
    __type_params__ 3.12引入

    __self__
    __func__
    __name__
    __module__

类级别的
    __name__
    __module__
    __dict__
    __bases__ tuple 基类
    __doc__
    __annotations__ dict 类变量注解
    __type_params__

"""

import m1_for_test
from m1_for_test import m1_f1

G_VAR1: int = 1

print('=' * 100)

# ========================文件级别的
print("文件级别的")
# 默认被执行的文件的__name__是__main__，而引入的模块就是文件名
# m1_for_test.py也打印了__name__，如果不是被直接执行，那么打印的也是文件名，而不是__main__
# 这也就是为啥常用 if __name__ == __main__ 进行判断的原因了
print(f"{__name__=}\n{__file__=}\n{__doc__=}\n{__annotations__=}\n{m1_for_test.__name__=}")
print('=' * 100)


# ========================函数级别的
print("函数级别的")
def f1(a: int, b, c=0, *args, **kwargs) -> int:
    """This is f1 doc"""
    d = a + b + c
    return d

# b=2不是必须指定默认值，即f2(a, *, b)定义方式也可以，只不过为了演示__kwdefaults__，所以增加了默认值
def f2(a, *, b=2):
    return a + b


class A:
    def af1(self, a, b, c=0, *args, **kwargs):
        """This is af1 doc"""
        d = a + b + c
        return d
    
    @property
    def ap1(self):
        return 1
    
    @classmethod
    def acm1(cls):
        return 1

    @staticmethod
    def asm1():
        return 1
    
print(f"{f1.__globals__=}\n{f1.__closure__}")
print(f"{f1.__doc__=}\n{f1.__name__=}\n{f1.__qualname__=}\n{f1.__module__=}\n{f1.__defaults__=}")
# __type_params__ 3.12版本引入
# __kwdefaults__ 是 对应的f2函数，并且f2函数 * 后面的变量必须有默认值才会在这里体现，否则仍然是None
print(f"{f1.__code__=}\n{f1.__dict__=}\n{f1.__annotations__=}\n{f2.__kwdefaults__=}\n{f1.__type_params__=}")

a = A()
f = a.af1
# f.__func__ 和 A.af1 其实是同一个对象，只不过通过实例调用方法时，会通过描述符把实例默认传递给这个方法的第一个参数，即self
print(f"{f.__self__=}\n{f.__func__=}\n{A.af1=}\n{f.__name__=}\n{f.__module__=}\n")
print(f"{m1_f1.__module__=}")
print('=' * 100)


# ========================类级别的
print("类级别的")
class B(A):
    b: int = 1
    def __init__(self) -> None:
        self.x: int = 2

print(f"{B.__name__=}\n{B.__module__=}\n{B.__dict__=}\n{B.__bases__=}\n{B.__doc__=}\n{B.__annotations__=}\n{B.__type_params__=}")

