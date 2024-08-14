import time
import functools


# =============================全部无参=============================
def print_func_elapsed1(func):
    def wrap():
        start = time.time()
        ret = func()
        print(f"{func.__name__} elapsed {time.time() - start}s.")
        return ret
    return wrap


@print_func_elapsed1
def t1():
    print("t1 start")
    time.sleep(2)
    print("t1 end")
    

# t1()


# =============================函数有参=============================
def print_func_elapsed2(func):
    def wrap(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        print(f"{func.__name__} elapsed {time.time() - start}s.")
        return ret
    return wrap


@print_func_elapsed2
def t2(a, b, c, d):
    print(f"t2 start, {a=}, {b=}, {c=}, {d=}")
    time.sleep(2)
    print("t2 end")
    

# t2(1, 2, d=3, c=4)


# =============================函数有参、装饰器有参=============================
def print_func_elapsed3(dp1=1, dp2=2):
    def _wrap(func):
        def wrap(*args, **kwargs):
            start = time.time()
            ret = func(*args, **kwargs)
            print(f"{func.__name__} elapsed {time.time() - start}s, with deco param: {dp1=}, {dp2=}.")
            return ret
        return wrap
    return _wrap


@print_func_elapsed3()
def t3(a, b, c, d):
    print(f"t3 start, {a=}, {b=}, {c=}, {d=}")
    time.sleep(2)
    print("t3 end")


@print_func_elapsed3(dp2=100)
def t4(a, b, c, d):
    print(f"t4 start, {a=}, {b=}, {c=}, {d=}")
    time.sleep(2)
    print("t4 end")
    

# t3(1, 2, d=3, c=4)
# t4(1, 2, d=3, c=4)


# =============================functools.wraps=============================
def print_func_elapsed4(dp1=1, dp2=2):
    def _wrap(func):
        # 注意应用位置和使用方式
        # 即访问的是原始函数，而不是包装后某些属性被改变的函数对象，比如函数的__name__等属性
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            start = time.time()
            ret = func(*args, **kwargs)
            print(f"{func.__name__} elapsed {time.time() - start}s, with deco param: {dp1=}, {dp2=}.")
            return ret
        return wrap
    return _wrap


@print_func_elapsed4(dp2=100)
def t5(a, b, c, d):
    print(f"t4 start, {a=}, {b=}, {c=}, {d=}")
    time.sleep(2)
    print("t4 end")


# 先看没有使用 functools.wraps 的情况
for attr in dir(t4):
    print(f"{attr}: {getattr(t4, attr)}")

print('=' * 100)

for attr in dir(t5):
    print(f"{attr}: {getattr(t5, attr)}")

print(t5.__name__)

# 下面仅举例需要特别关注的几个属性
"""
t4属性及值如下：
__annotations__: {}
__call__: <method-wrapper '__call__' of function object at 0x0000023FC132DAF0>
__class__: <class 'function'>
__closure__: (<cell at 0x0000023FC1361250: int object at 0x0000023FC0B76930>, <cell at 0x0000023FC1361220: int object at 0x0000023FC0BA55D0>, <cell at 0x0000023FC13611F0: function object at 0x0000023FC132DA60>)
__code__: <code object wrap at 0x0000023FC13643A0, file "D:\github\docode\python_demo\xbasic\deco_demo0.py", line 48>
__defaults__: None
__delattr__: <method-wrapper '__delattr__' of function object at 0x0000023FC132DAF0>
__dict__: {}
__dir__: <built-in method __dir__ of function object at 0x0000023FC132DAF0>
__doc__: None
__eq__: <method-wrapper '__eq__' of function object at 0x0000023FC132DAF0>
__format__: <built-in method __format__ of function object at 0x0000023FC132DAF0>
__ge__: <method-wrapper '__ge__' of function object at 0x0000023FC132DAF0>
__get__: <method-wrapper '__get__' of function object at 0x0000023FC132DAF0>
__getattribute__: <method-wrapper '__getattribute__' of function object at 0x0000023FC132DAF0>
__globals__: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000023FC0BD6D00>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'D:\\github\\docode\\python_demo\\xbasic\\deco_demo0.py', '__cached__': None, 'time': <module 'time' (built-in)>, 'functools': <module 'functools' from 'C:\\Users\\linlei\\Anaconda3\\lib\\functools.py'>, 'print_func_elapsed1': <function print_func_elapsed1 at 0x0000023FC0C1F040>, 't1': <function print_func_elapsed1.<locals>.wrap at 0x0000023FC132D5E0>, 'print_func_elapsed2': <function print_func_elapsed2 at 0x0000023FC132D670>, 't2': <function print_func_elapsed2.<locals>.wrap at 0x0000023FC132D790>, 'print_func_elapsed3': <function print_func_elapsed3 at 0x0000023FC132D820>, 't3': <function print_func_elapsed3.<locals>._wrap.<locals>.wrap at 0x0000023FC132D9D0>, 't4': <function print_func_elapsed3.<locals>._wrap.<locals>.wrap at 0x0000023FC132DAF0>, 'print_func_elapsed4': <function print_func_elapsed4 at 0x0000023FC132D8B0>, 't5': functools.partial(<function update_wrapper at 0x0000023FC12A29D0>, wrapped=<function print_func_elapsed4.<locals>._wrap.<locals>.wrap at 0x0000023FC132DCA0>, assigned=('__module__', '__name__', '__qualname__', '__doc__', '__annotations__'), updated=('__dict__',)), 'attr': '__globals__'}
__gt__: <method-wrapper '__gt__' of function object at 0x0000023FC132DAF0>
__hash__: <method-wrapper '__hash__' of function object at 0x0000023FC132DAF0>
__init__: <method-wrapper '__init__' of function object at 0x0000023FC132DAF0>
__init_subclass__: <built-in method __init_subclass__ of type object at 0x00007FFD46B8FC50>
__kwdefaults__: None
__le__: <method-wrapper '__le__' of function object at 0x0000023FC132DAF0>
__lt__: <method-wrapper '__lt__' of function object at 0x0000023FC132DAF0>
__module__: __main__
__name__: wrap  **********************
__ne__: <method-wrapper '__ne__' of function object at 0x0000023FC132DAF0>
__new__: <built-in method __new__ of type object at 0x00007FFD46B8FC50>
__qualname__: print_func_elapsed3.<locals>._wrap.<locals>.wrap **********************
__reduce__: <built-in method __reduce__ of function object at 0x0000023FC132DAF0>
__reduce_ex__: <built-in method __reduce_ex__ of function object at 0x0000023FC132DAF0>
__repr__: <method-wrapper '__repr__' of function object at 0x0000023FC132DAF0>
__setattr__: <method-wrapper '__setattr__' of function object at 0x0000023FC132DAF0>
__sizeof__: <built-in method __sizeof__ of function object at 0x0000023FC132DAF0>
__str__: <method-wrapper '__str__' of function object at 0x0000023FC132DAF0>
__subclasshook__: <built-in method __subclasshook__ of type object at 0x00007FFD46B8FC50>
"""

"""
t5属性及值如下：
__annotations__: {}
__call__: <method-wrapper '__call__' of function object at 0x000001FAF893DCA0>
__class__: <class 'function'>
__closure__: (<cell at 0x000001FAF89711C0: int object at 0x000001FAF8176930>, <cell at 0x000001FAF8971190: int object at 0x000001FAF81A55D0>, <cell at 0x000001FAF8971160: function object at 0x000001FAF893DC10>)
__code__: <code object wrap at 0x000001FAF89747C0, file "D:\github\docode\python_demo\xbasic\deco_demo0.py", line 78>
__defaults__: None
__delattr__: <method-wrapper '__delattr__' of function object at 0x000001FAF893DCA0>
__dict__: {'__wrapped__': <function t5 at 0x000001FAF893DC10>}
__dir__: <built-in method __dir__ of function object at 0x000001FAF893DCA0>
__doc__: None
__eq__: <method-wrapper '__eq__' of function object at 0x000001FAF893DCA0>
__format__: <built-in method __format__ of function object at 0x000001FAF893DCA0>
__ge__: <method-wrapper '__ge__' of function object at 0x000001FAF893DCA0>
__get__: <method-wrapper '__get__' of function object at 0x000001FAF893DCA0>
__getattribute__: <method-wrapper '__getattribute__' of function object at 0x000001FAF893DCA0>
__globals__: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001FAF81D6D00>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'D:\\github\\docode\\python_demo\\xbasic\\deco_demo0.py', '__cached__': None, 'time': <module 'time' (built-in)>, 'functools': <module 'functools' from 'C:\\Users\\linlei\\Anaconda3\\lib\\functools.py'>, 'print_func_elapsed1': <function print_func_elapsed1 at 0x000001FAF857F040>, 't1': <function print_func_elapsed1.<locals>.wrap at 0x000001FAF893D5E0>, 'print_func_elapsed2': <function print_func_elapsed2 at 0x000001FAF893D670>, 't2': <function print_func_elapsed2.<locals>.wrap at 0x000001FAF893D790>, 'print_func_elapsed3': <function print_func_elapsed3 at 0x000001FAF893D820>, 't3': <function print_func_elapsed3.<locals>._wrap.<locals>.wrap at 0x000001FAF893D9D0>, 't4': <function print_func_elapsed3.<locals>._wrap.<locals>.wrap at 0x000001FAF893DAF0>, 'print_func_elapsed4': <function print_func_elapsed4 at 0x000001FAF893D8B0>, 't5': <function t5 at 0x000001FAF893DCA0>, 'attr': '__globals__'}
__gt__: <method-wrapper '__gt__' of function object at 0x000001FAF893DCA0>
__hash__: <method-wrapper '__hash__' of function object at 0x000001FAF893DCA0>
__init__: <method-wrapper '__init__' of function object at 0x000001FAF893DCA0>
__init_subclass__: <built-in method __init_subclass__ of type object at 0x00007FFD46B8FC50>
__kwdefaults__: None
__le__: <method-wrapper '__le__' of function object at 0x000001FAF893DCA0>
__lt__: <method-wrapper '__lt__' of function object at 0x000001FAF893DCA0>
__module__: __main__
__name__: t5
__ne__: <method-wrapper '__ne__' of function object at 0x000001FAF893DCA0>
__new__: <built-in method __new__ of type object at 0x00007FFD46B8FC50>
__qualname__: t5 
__reduce__: <built-in method __reduce__ of function object at 0x000001FAF893DCA0>
__reduce_ex__: <built-in method __reduce_ex__ of function object at 0x000001FAF893DCA0>
__repr__: <method-wrapper '__repr__' of function object at 0x000001FAF893DCA0>
__setattr__: <method-wrapper '__setattr__' of function object at 0x000001FAF893DCA0>
__sizeof__: <built-in method __sizeof__ of function object at 0x000001FAF893DCA0>
__str__: <method-wrapper '__str__' of function object at 0x000001FAF893DCA0>
__subclasshook__: <built-in method __subclasshook__ of type object at 0x00007FFD46B8FC50>
__wrapped__: <function t5 at 0x000001FAF893DC10>
"""


