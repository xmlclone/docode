# https://docs.python.org/zh-cn/3/reference/datamodel.html#descriptors
# https://docs.python.org/zh-cn/3/howto/descriptor.html

"""
1. 只要有__get__(self, instance, owner=None)、__set__(self, instance, value)、__delete__(self, instance)任意一个的类，就叫描述符
2. 描述符的类必须是类的属性(或叫类变量)才生效；如果只定义为实例变量，则只会当成普通类实例对待(即无法通过.描述符直接访问到__get__ __set__等)；
   如果实例和类的属性同名的情况下，还需要参考下面的第4点
3. 只定义了__get__的是非资料/数据描述符，类和实例的属性如果同名，则以实例的属性为准，比如下面的D
4. 任何定义了__set__或__delete__的(即两者其一、或都定义，有没有__get__无所谓)，就叫资料/数据描述符，类或实例的属性同名，都会访问到描述符上面
   比如下面的C
   总结一点就是: 数据描述符会覆盖实例的字典，非数据描述符会被实例的字典覆盖
5. 定义了 __getattribute__ ，则无条件访问 __getattribute__
   定义了 __getattribute__ ，并且定义了 __getattr__ ，如果 __getattribute__ 异常，则无条件访问 __getattr__
   未定义 __getattribute__ ，但定义了 __getattr__ ， 则描述符优先于 __getattr__
   描述器是通过 __getattribute__ 实现，故尽量不要在描述器里面重写此方法，除非你特别了解它们的原理
"""


# ============================demo0 __set_name__引入============================
from typing import Any


class A:
    def __set_name__(self, owner, name):
        # owner是B这个类(注意不是实例)，name是实例化A时候的名称，比如下面B类里面的a或者x
        # 要注意和__set__ __get__的参数的区分
        print(f'__set_name__ called: owner={owner}, name={name}')

class B:
    a = A()
    x = A()
# 不用实例化B，上面的a = A()会自动调用，并且调用A的__set_name__
# b = B()
print('=' * 100)


# ============================demo1 数据/非数据描述符区别============================
class C:
    # 数据描述符
    def __set__(self, instance, value):
        # instance 是具体类的实例，比如下面的E的实例e
        print(f"C:SET {instance=} {value=}")

    def __get__(self, instance, owner=None):
        # instance 是具体类的实例，比如下面的E的实例e
        # owner 是具体的类，比如下面的E这个类
        print(f'c:get {instance=} {owner=}')
        return f'c:get {instance=} {owner=}'

class D:
    # 非数据描述符
    def __get__(self, instance, owner=None):
        print("D:GET")

class E:
    c = C()
    d = D() # 下面通过self.d定义后，对实例来说，这个d基本就无效了

    def __init__(self):
        self.c = 1  # 访问到C
        self.d = 2  # 无法访问D

class E1:
    c = C()
    
    def __init__(self):
        self.d = D() # 实例定义的变量，也就成为了一个普通的实例，无法通过.的访问直接访问到__get__或__set__，下面的c1也类似
        self.c1 = C() # 故必须要先成为类的属性，实例如果有同名的属性，要看是资料描述符还是非资料描述符

e = E()
e.c = 11  # 仍然访问C
e.d = 22  # 仍然无法访问D
print(e.c, e.d)
e1 = E1()
print(e1.c, e1.d, e1.c1)
print('=' * 100)


# ============================demo2 演示几个get函数的优先级============================
class F:
    def __set__(self, instance, value):
        print("F:SET")

    def __get__(self, instance, owner=None):
        print("F:GET")

class G:
    # __get__需要作为某个类的属性才可能被调用，所以和 __getattr__ __getattribute__并不在本例探讨范围内
    f = F()

    def __init__(self) -> None:
        self.x = 1

    def __getattr__(self, __name: str):
        print("G:getattr")

    def __getattribute__(self, __name: str) -> Any:
        print("G:getattribute")

class H:
    f = F()

    def __init__(self) -> None:
        self.x = 1

    def __getattr__(self, __name: str):
        print("H:getattr")

    def __getattribute__(self, __name: str) -> Any:
        print("H:getattribute")
        raise AttributeError()
    
class I:
    f = F()

    def __init__(self) -> None:
        self.x = 1

    def __getattr__(self, __name: str):
        print("I:getattr")
        raise AttributeError()

    def __getattribute__(self, __name: str) -> Any:
        print("I:getattribute")
        raise AttributeError()
    
class J:
    f = F()

    def __init__(self) -> None:
        self.x = 1

    def __getattr__(self, __name: str):
        print("J:getattr")
        raise AttributeError()
    
class K:
    f = F()

    def __init__(self) -> None:
        self.x = 1

    def __getattr__(self, __name: str):
        print("K:getattr")

g = G()
h = H()
i = I()
j = J()
k = K()

# 全访问的__getattribute__，即有__getattribute__时会被无条件访问
print(f'{g.f=}, {g.x=}, {g.y=}\n')
# 首先全访问的__getattribute__，但__getattribute__抛异常，则会无条件访问__getattr__
print(f'{h.f=}, {h.x=}, {h.y=}\n')
# 首先全访问的__getattribute__，但__getattribute__抛异常，则会无条件访问__getattr__，但__getattr__仍然抛出异常，则无法访问任何实例属性(虽然 f x都被定义了，但仍然会抛出异常)
# print(f'{i.f=}, {i.x=}, {i.y=}\n')
# f描述符的优先级，在没有__getattribute__的情况下，高于__getattr__，故下面的j.f会访问到描述符的__get__
# 如果有__getattribute__并且还有__getattr__的情况下，那么__getattr__会高于f描述符
# j.y 会访问__getattr__会抛出异常
print(f'{j.f=}, {j.x=}\n')
# 和J类似，只不过__getattr__没有抛出异常，k.y可以正常访问
print(f'{k.f=}, {k.x=}, {k.y=}\n')
print('=' * 100)