import time
import datetime



"""
常用:
%Y-%m-%d %H:%M:%S
%Y-%m-%d %H:%M:%S.%f


https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
https://docs.python.org/3/library/time.html#time.strftime
"""


# 默认使用的是当前时间，可以传递第二个参数为需要格式化的时间
# time.strftime 不支持 %f, time.strptime 支持
print(time.strftime("%Y-%m-%d %H:%M:%S"))


datetime_str = "2024-05-20 19:22:18.665423"
# 虽然支持%f，但是返回的结构体是不会有%f格式化的值的
# 返回 time. struce_time 对象
print(time.strptime(datetime_str, "%Y-%m-%d %H:%M:%S.%f"))


# 返回 datetime.datetime 对象
print(datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S.%f"))
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))