# 定义一个元类
class A(type):
    # 其实这里的参数 (name, bases, dct) 和 demo0的直接调用type方法的参数一致
    # 另外，这里如果不重新__new__，会自动调用type.__new__
    def __new__(cls, name, bases, dct):
        # cls=<class '__main__.A'>, name='B', bases=(), dct={'__module__': '__main__', '__qualname__': 'B'}
        # cls=<class '__main__.A'>, name='C', bases=(), dct={'__module__': '__main__', '__qualname__': 'C', 'a': 1, '__init__': <function C.__init__ at 0x000002EF6453C5E0>, 'f1': <function C.f1 at 0x000002EF6453C670>}
        # cls=<class '__main__.A'>, name='D', bases=(<class '__main__.C'>,), dct={'__module__': '__main__', '__qualname__': 'D', 'b': 2, 'f2': <function D.f2 at 0x000002BBE0F1C700>}
        print(f"{cls=}, {name=}, {bases=}, {dct=}")
        return type.__new__(cls, name, bases, dct)


# 使用元类(顶行就会执行，故不需要其它代码的调用，上面的__new__就会被执行)
class B(metaclass=A):
    ...
    # 上面的__new__打印下面内容
    # cls=<class '__main__.A'>, name='B', bases=(), dct={'__module__': '__main__', '__qualname__': 'B'}


class C(metaclass=A):
    # 上面的__new__打印下面内容
    # cls=<class '__main__.A'>, name='C', bases=(), dct={'__module__': '__main__', '__qualname__': 'C', 'a': 1, '__init__': <function C.__init__ at 0x000002EF6453C5E0>, 'f1': <function C.f1 at 0x000002EF6453C670>}
    a = 1

    def __init__(self) -> None:
        self.x = 1

    def f1(self, p1, p2):
        ...


class D(C):
    # 上面的__new__打印下面内容
    # cls=<class '__main__.A'>, name='D', bases=(<class '__main__.C'>,), dct={'__module__': '__main__', '__qualname__': 'D', 'b': 2, 'f2': <function D.f2 at 0x000002BBE0F1C700>}
    b = 2

    def f2(self):
        ...

