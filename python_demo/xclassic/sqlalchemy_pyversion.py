import sys
import platform


print(f"{sys.version=}")
print(f"{sys.platform=}, {platform.machine()=}")
print(f"{platform.machine()=}")
# 判断是否是 64 位系统
is64bit = sys.maxsize > 2**32


# sys.version_info(major=3, minor=9, micro=7, releaselevel='final', serial=0)
print(sys.version_info)
# version_info 是 tuple 的子类，故可以使用下面的方式比较版本号，传递的元组应该符合 (major, minor, micro) 格式，其中 minor 和 micro 可以省略
print(sys.version_info >= (2, ))
print(sys.version_info >= (3, 12))
print(sys.version_info >= (3, 8))
print(sys.version_info >= (3, 9, 8))


"""
'CPython' (C implementation of Python),
'Jython' (Java implementation of Python),
'PyPy' (Python implementation of Python).
"""
print(platform.python_implementation())