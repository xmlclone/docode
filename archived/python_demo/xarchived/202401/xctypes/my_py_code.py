import ctypes

# 加载动态库
mylib = ctypes.cdll.LoadLibrary("./libmy_c_code.so")

# 定义参数和返回值类型
mylib.add.argtypes = [ctypes.c_int, ctypes.c_int]
mylib.add.restype = ctypes.c_int

# 调用函数
ret = mylib.add(1, 2)
print(f"{ret=}")