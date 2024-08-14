import typing


"""

typing.TYPE_CHECKING是Python中的一个特殊变量，通常用于类型提示。
它的作用是在类型提示时避免循环导入问题。当模块被解释器正常执行时，typing.TYPE_CHECKING为False，这样类型提示代码就不会被执行。
但是在执行类型检查时，例如使用mypy等工具进行静态类型检查时，typing.TYPE_CHECKING会被设置为True，这样类型提示代码就会被执行。
这种机制使得可以在类型提示中安全地引用当前模块的类型，而不会导致循环导入问题。


a.py 和 b.py 的逻辑下有相互引入，不管在什么情况下都是不允许的
但是我只想引入作为类型提示，比如下面的 b: "B"，那要怎么办呢？
可以增加 typing.TYPE_CHECKING，在执行类型检查时，比如 IDE 时，值是 True ，并配合 b: "B" 的应用方式，就可以得到解决
注意，一定要加双引号，否则会影响正常的执行



正例
# module_a.py
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from module_b import B

class A:
    def __init__(self, b: 'B'):
        self.b = b

# module_b.py
class B:
    def __init__(self, a: 'A'):
        self.a = a


反例
# module_a.py
from module_b import B

class A:
    def __init__(self, b: B):
        self.b = b

# module_b.py
from module_a import A

class B:
    def __init__(self, a: A):
        self.a = a
"""


if typing.TYPE_CHECKING:
    from b import B


class A:
    def __init__(self, b: "B"):
        self.b = b