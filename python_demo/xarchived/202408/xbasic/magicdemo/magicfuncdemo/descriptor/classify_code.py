"""
描述器的几个应用场景
"""


# 字段类型验证、字段值验证


class TypedAndNotNull:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, _):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if not value:
            raise ValueError(f"{self.name} must be a non-value.")
        if not isinstance(value, self.expected_type):
            raise TypeError(f"{self.name} must be of type {self.expected_type}")
        instance.__dict__[self.name] = value

class Person:
    name = TypedAndNotNull('name', str)
    age = TypedAndNotNull('age', int)

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name=}, {self.age=}"

p1 = Person('lin', 18)
print(p1)
# p1.age = '19' # TypeError
# p1.name = '' # ValueError


# 延迟计算，作为装饰器修饰
class LazyProperty:
    def __init__(self, func) -> None:
        self.func = func
        self.name = func.__name__

    def __get__(self, instance, _):
        if instance is None:
            return self
        value = self.func(instance)
        setattr(instance, self.name, value)
        return value
    
class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

    # 注意，类方法，其实就是类的一个属性，故类方法也可以成为一个描述器
    @LazyProperty
    def area(self):
        return self.radius * 3.14159 * 2
    
circle = Circle(10)
print(circle.area)

