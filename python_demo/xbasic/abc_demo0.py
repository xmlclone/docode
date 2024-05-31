import abc


class A(abc.ABC):
    def f1(self):
        print("f1")

    @abc.abstractmethod
    def f2(self):
        # 注意这里需要 raise 的内容，不要写成 NotImplemented 了
        raise NotImplementedError
    

class B(A):
    def f2(self):
        print("f2")


# 如果上面的B没有实现f2，会抛出下面的异常
# TypeError: Can't instantiate abstract class B without an implementation for abstract method 'f2'
b = B()
b.f1()
b.f2()