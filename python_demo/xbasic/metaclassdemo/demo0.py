"""
*. 类也是一个对象，可以通过__new__创建类对象
"""


class A:
    a = 1

    def a_f(self, a1=1, a2=2):
        ...
# 下面的定义方式和上面的A是相同的
def b_f(self, a1=1, a2=2):
    print(f"{self=}")
B = type("B", (), dict(a=1, b_f=b_f))

a = A()
b = B()
# type(a)=<class '__main__.A'>, type(b)=<class '__main__.B'>
print(f"{type(a)=}, {type(b)=}")
b.b_f() # 部分IDE可能会报错，但是不影响执行




# *. 还可以通过type.__new__创建一个类对象，前提是这个类对象必须继承type
# 像上面的A就无法通过type.__new__创建
class D(type):
    ...
C = type.__new__(D, 'C', (), dict(x=1, b_f=b_f))
c = C()
c.b_f()



