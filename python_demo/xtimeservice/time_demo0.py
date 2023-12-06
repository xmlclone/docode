import time
from datetime import datetime


print(time.time())

# https://docs.python.org/3/library/time.html#time.strftime
# time.strftime不支持毫秒级别的输出，需要使用datetime模块，参考下文
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strptime("2023-10-27 11:18:43", "%Y-%m-%d %H:%M:%S"))


# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
# %f就是毫秒，但是会输出6位
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
# 只要3位
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])