# module.py

__all__ = ['foo', 'bar']

def foo():
    print("This is the foo function")

def bar():
    print("This is the bar function")

def baz():
    print("This is the baz function")


# 仅仅影响 from module import * 的行为，只会导入 __all__ 定义的对象
# 而 import 和 from import 语句不受影响