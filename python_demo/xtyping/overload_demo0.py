from typing import overload


@overload
def add(a: int, b: int) -> int:
    print(1)
    return a + b

@overload
def add(a: int, b: float) -> float:
    print(2)
    return a + b

# 注意，一定要定义一个不带 overload 的原始函数，并且不能在 @overload 之前定义
# 并且真正的调用都是发生在这里的，即上面的print(1)和print(2)根本不会被执行
# 真正的逻辑在这里，上面的仅仅是给静态检查提供帮助的，里面写在多的******逻辑都不管用。。。。
def add(a, b):
    print(3)
    return a + b


add(1, 2)
add(1, 2.0)