"""
本例演示 类属性和实例属性同名情况
"""


class D1:
    def __get__(self, instance, owner=None):
        print(f"D1 __get__ called, {instance=}, {owner=}")
        return "d1"
    
class D2:
    def __get__(self, instance, owner=None):
        print(f"D2 __get__ called, {instance=}, {owner=}")
        return "d2"

    def __set__(self, instance, value):
        print(f"D2 __set__ called, {instance=}, {value=}")


class T1:
    # 初始化的时候，并不会调用 __set__ 
    d1 = D1()
    print(1)
    # 如果这里不定义d2，而是在__init__里面定义的d2，那么d2也只能算是一个普通属性而不是描述器(即所有的前提都是需要为类属性，只不过实例属性可以再次覆盖定义)
    d2 = D2()
    print(2)

    def __init__(self) -> None:
        # 由于这里使用 self.d1，和 self.d2
        # d1是非数据描述器，d2是数据描述器
        # 故d1就是当成一个普通属性变量 d2会是一个描述器变量
        # 故d1不会调用D1的__set__ 而d2会调用D2的__set__
        # **** 仍然可以这样去理解，D1 和 D2 咋们都一视同仁，都认为是描述器，在设置属性时，都想要去调用 __set__，但是你d1没有提供啊，怎么办呢？python就自动给你转换为普通变量了~
        self.d1 = D1()
        print(3)
        self.d2 = D2()
        print(4)


t1 = T1()
# 注意，下面的 d1 任何输出都没有，是因为上面的 __init__ 里面self.d1已经把你这个d1转换为普通变量了
# **** 但是，如果是这里先访问 t1.d1 那么，仍然认为 d1 是一个描述器，会访问到 D1 的 __get__
# 仍然可以这样理解，所有的只要是定义为了属性的 d1 d2 我都先默认为描述器，该访问其 __get__ __set__
# 一旦需要没有的，则会转换为普通变量，并且影响后续的访问
print(5)
t1.d1
t1.d1 = 1 # type: ignore   这里IDE一般会报错，但是不影响你写这个代码和执行
t1.d1
print(6)
# d2 的 __get__ __set__都会成功访问
t1.d2
t1.d2 = 2
t1.d2

"""
1
2
3
D2 __set__ called, instance=<__main__.T1 object at 0x0000020DEBE2F920>, value=<__main__.D2 object at 0x0000020DEBE2F980>
4
5
6
D2 __get__ called, instance=<__main__.T1 object at 0x0000020DEBE2F920>, owner=<class '__main__.T1'>
D2 __set__ called, instance=<__main__.T1 object at 0x0000020DEBE2F920>, value=2
D2 __get__ called, instance=<__main__.T1 object at 0x0000020DEBE2F920>, owner=<class '__main__.T1'>
"""