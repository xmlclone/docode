class D1:
    """
    1. 只要定义了下面任何一个方法的类，就是 描述器
    2. 只有 __get__ 的叫 非资料描述器/非数据描述器
    3. 定义了 __set__ 或 __delete__ 的任何一个则叫 资料描述器/数据描述器

    描述器必须是类的属性才能有效(这是必要前提)

    默认情况下，a.x 的访问顺序是: a.__dict__['x']   type(a).__dict__['x']  type(a)的上级基类
    但如果某个值是一个描述器对象，即a.x是一个描述器对象，则会影响调用行为(上面的顺序仍然不会变)
    """

    def __get__(self, instance, owner=None):
        ...

    def __set__(self, instance, value):
        ...

    def __delete__(self, instance):
        ...

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


class A1:
    gd2 = D2()
    gd3 = D3()

    def __init__(self) -> None:
        self.d2 = D2()
        self.d3 = D3()

a1 = A1()
# D2 __get__ called, instance=<__main__.A1 object at 0x000001F189BF89E0>, owner=<class '__main__.A1'>
# D3 __get__ called, instance=<__main__.A1 object at 0x000001F189BF89E0>, owner=<class '__main__.A1'>
# a1.gd2='d2', a1.gd3='d3'
# 表明只有 类属性 描述器才会生效，而 实例属性 不生效，只是普通的访问而已
print(f"{a1.gd2=}, {a1.gd3=}")
print('-' * 100)
# a1.d2=<__main__.D2 object at 0x000001F189BF87D0>, a1.d3=<__main__.D3 object at 0x000001F189BF8A70>
print(f"{a1.d2=}, {a1.d3=}")
print('-' * 100)

# D3 __set__ called, instance=<__main__.A1 object at 0x000001F189BF89E0>, value=31
# 这里只有 D3 __set__ 生效，而且大部分 IDE 会对除了 a1.gd3 以外的几个设置代码报错
# 即 D2() 是一个非资料描述器，对它进行设置不会调用 __set__
# 而 D3() 是资料描述器，会调用 __set__
# **** 可以这样想： 你都没有提供 __set__ ，python 就不知道如何去调用描述器来设置值，那只好强制转变为普通变量了
a1.gd2 = 21   # type:ignore gd2的值会被改变为21
a1.gd3 = 31   # 其实只有这个才是真正有效的
print('-' * 100)
# 下面两个设置属性并没有调用 __set__
a1.d2 = 41 # type:ignore
a1.d3 = 51 # type:ignore
print(f"{a1.gd2=}, {a1.gd3=}")
print('-' * 100)
print(f"{a1.d2=}, {a1.d3=}")
print('-' * 100)

"""
上面的输出如下：


D2 __get__ called, instance=<__main__.A1 object at 0x000001F189BF89E0>, owner=<class '__main__.A1'>
D3 __get__ called, instance=<__main__.A1 object at 0x000001F189BF89E0>, owner=<class '__main__.A1'>
a1.gd2='d2', a1.gd3='d3'
----------------------------------------------------------------------------------------------------
a1.d2=<__main__.D2 object at 0x000001F189BF87D0>, a1.d3=<__main__.D3 object at 0x000001F189BF8A70>
----------------------------------------------------------------------------------------------------
D3 __set__ called, instance=<__main__.A1 object at 0x000001F189BF89E0>, value=31
----------------------------------------------------------------------------------------------------
D3 __get__ called, instance=<__main__.A1 object at 0x000001F189BF89E0>, owner=<class '__main__.A1'>
a1.gd2=21, a1.gd3='d3'
----------------------------------------------------------------------------------------------------
a1.d2=41, a1.d3=51
----------------------------------------------------------------------------------------------------
"""