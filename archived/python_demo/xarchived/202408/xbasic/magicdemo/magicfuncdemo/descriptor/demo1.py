"""
结合
object.__getattribute__(self, name)  无条件调用
object.__getattr__(self, name)  默认的访问引发了 AttributeError 时被调用

只有 __getattribute__ 会影响描述器，因为这个是无条件调用
__getattr__ 并不影响描述器
"""


class A1:
    def __getattribute__(self, name):
        print("A1::__getattribute__")
        return name

    def __getattr__(self, name):
        print("A1::__getattr__")
        return name
    
    def __init__(self) -> None:
        self.a = 1

a1 = A1()
print(a1.a)  # 无条件访问 __getattribute__ ，故返回 a 而不是 1


class A2:
    def __getattribute__(self, name):
        print("A1::__getattribute__")
        raise AttributeError

    def __getattr__(self, name):
        print("A1::__getattr__")
        return "__getattr__"
    
    def __init__(self) -> None:
        self.a = 1

a2 = A2()
print(a2.a)  # 无条件访问 __getattribute__ ，但抛出了异常，会访问 __getattr__，故返回 __getattr__ 而不是 1
print('-' * 100)


class D2:
    def __get__(self, instance, owner=None):
        print(f"D2 __get__ called, {instance=}, {owner=}")
        return "d2"
    
class D3:
    def __get__(self, instance, owner=None):
        print(f"D3 __get__ called, {instance=}, {owner=}")
        return "d3"

    def __set__(self, instance, value):
        print(f"D3 __set__ called, {instance=}, {value=}")

class A3:
    d2 = D2()
    d3 = D3()

    # def __getattribute__(self, name):
        # print("A1::__getattribute__")
        # 如果有，不管是啥(包括描述器)都会无条件访问这里
        # return "__getattribute__"
        # raise AttributeError

    def __getattr__(self, name):
        # 此方法并不影响 描述器，故不会访问此处
        print("A1::__getattr__")
        return "__getattr__"
        # raise AttributeError
    
    def __init__(self) -> None:
        self.a = 1

a3 = A3()
print(a3.d2, a3.d3)