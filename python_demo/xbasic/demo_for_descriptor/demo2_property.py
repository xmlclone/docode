"""
我们通常使用的 @property 其实就是把一个方法映射为了一个描述符
"""

from typing import Callable, Any, Union


class A:
    def getX(self):
        return self._x

    def setX(self, value):
        self._x = value

    def delX(self):
        del self._x

    # 此时的x其实类似一个描述符
    x = property(getX, setX, delX, "I'm the 'x' property.")

a = A()
a.x = 10
print(a.x)
print('=' * 100)


class Property:
    def __init__(self, getf, setf: Union[Callable[['B', Any], None], None]=None, delf=None, doc=None) -> None:
        self.getf = getf
        self.setf: Callable[['B', Any], None] = setf # type: ignore
        self.delf = delf
        self.doc = doc

    def __get__(self, obj, objtype=None):
        return self.getf(obj)

    def __set__(self, obj, value):
        self.setf(obj, value)


class B:
    def getx(self):
        return self._x
    
    def setx(self, value):
        self._x = value
    
    # x就是一个描述符
    x = Property(getf=getx, setf=setx)

b = B()
b.x = 10
print(b.x)
print('=' * 100)