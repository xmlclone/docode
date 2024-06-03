from typing import TypeVar

from collections.abc import (
    Sequence as abcSequence
)


# 泛型 T ，可以直接使用，而不用提前定义
# 其实在定义函数 def first[T] 的时候，被自动定义了 T = TypeVar('T')
def first[T](l: abcSequence[T]) -> T:
    return l[0]


# 等同于下面的方式，这里为了和 T 区分使用了 S
S = TypeVar('S')
def first2[S](l: abcSequence[S]) -> S:
    return l[0]


# 为了演示不用提前定义，我们这里使用 D 来表示
def first3[D](l: abcSequence[D]) -> D:
    return l[0]


# 类同理，都需要在定义具体命名的后面增加 [T] 即可自动绑定为 TypeVar
class C1[D]:
    ...


# 还可以绑定约束类型，此时泛型 D 就只能是 str 类型
class C2[D: str]:
    ...

# 还可以绑定多个，它们之间是 或 的关系
class C3[D: (str, bytes)]:
    ...

# 函数类似
def f1[D, str]():
    ...


# TypeVar 显示定义
T = TypeVar('T')  # 任何类型都可以
S = TypeVar('S', bound=str) # 只能是 str 或其子类
S1 = TypeVar('S1', bound=str|bytes) # 只能是 str及其子类 或 bytes 及其子类
A = TypeVar('A', str, bytes) # 只能是 str 或 bytes
