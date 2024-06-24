"""
https://docs.python.org/zh-cn/3/reference/datamodel.html#traceback-objects
"""


import traceback
from types import TracebackType


def funca():
    1 / 0


def funcb():
    funca()


def funcc():
    funcb()


def funcx(e):
    print(dir(e))
    print('-' * 100)
    print(type(e)) # class 'ZeroDivisionError'
    print('-' * 100)
    print(e) # division by zero
    print('-' * 100)
    print(e.__traceback__) # traceback object
    print('-' * 100)
    print(f"{traceback.format_exc()=}") # 可以打印全部异常路径
    print('-' * 100)

    trace_obj: TracebackType = e.__traceback__
    print(f"{traceback.format_tb(trace_obj)=}")
    print('-' * 100)
    # 第一个 tb_lineno 只会显示到 funcd() 里面调用 funcc() 引发异常的行
    print(f"{trace_obj.tb_frame=}, {trace_obj.tb_lineno=}, {trace_obj.tb_lasti=}, {trace_obj.tb_next=}")
    print('-' * 100)

    while trace_obj.tb_next:
        trace_obj = trace_obj.tb_next
        print(f"{trace_obj.tb_frame=}, {trace_obj.tb_lineno=}, {trace_obj.tb_lasti=}, {trace_obj.tb_next=}")
        print('-' * 100)


def funcd():
    try:
        funcc()
    except Exception as e:
        funcx(e)




funcd()