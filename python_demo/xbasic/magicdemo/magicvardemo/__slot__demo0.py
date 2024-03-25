"""
*. 阻止创建__dict__和__weakref__, 除非__slot__显示创建__dict__或__weakref__
*. 是类变量，值可以是字符串、可迭代对象、字符串序列，影响的是类的实例的属性赋值
*. 相较于__dict__可以节省空间, 并且可以提高属性查找速度

*. 简而言之，如果有__dict__，则可以在实例上随意定义属性；如果没有，则需要使用在__slots__内定义的属性
*. 子类会继承父类定义的__slots__
*. 子类如果不显示定义__slots__，则子类的实例__dict__会被自动创建
*. 父类如果没有定义__slots__，则所有子类、子孙类...均会自动生成__dict__，不管子孙的父类是否定义了__slots__


https://docs.python.org/zh-cn/3/reference/datamodel.html#slots
"""


class A:
    z = 3
    __slots__ = ['m']

    def __init__(self) -> None:
        self.m = 11
        # self.n = 12   # *. 无法使用和定义未在__slots__列出的实例变量

o = A()
print(o.m)
# print(o.n) # 无法使用和定义未在__slots__列出的实例变量
print(o.z)
# print(o.__dict__) # *. 定义__slots__后，不会主动创建__dict__，故无法访问



class B(A):
    ...

o = B()
# *. 继承类除非显示使用了__slots__，否则会自动创建__dict__，那么也就可以使用未在父类的__slots__定义的变量
o.n = 12
print(o.n)
print(o.__dict__)



class C(A):
    __slots__ = ['k']

o = C()
# *. 子类显示定义了__slots__，故子类不会再主动创建__dict__，那么未在__slots__中列出的变量无法使用
# *. 注意子类会继承父类的__slots__定义，故m这个变量也是可以使用的
# o.n = 12
o.k = 13
o.m = 14
# print(o.__dict__)



# *. 继承自一个没有__slots__的类，不管内部是否定义了__slots__，都会有__dict__
class D:
    ...

class E(D):
    __slots__ = ['x']

o = E()
# 虽然E定义了__slots__，但是它的父类D并没有__slots__，故会自动生成__dict__
print(o.__dict__)
o.x = 1
o.y = 2

# *. 父类E虽然有__slots__，但是往上的D仍然是没有__slots__的，__dict__仍然是可以访问的
# *. 故第一个父类会影响下面所有的子类
class F(E):
    __slots__ = ['y']

o = F()
print(o.__dict__)