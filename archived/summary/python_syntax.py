"""
模块字符串

__init__.py
"""

import os
import logging
from pathlib import Path
from functools import partial as func_partial

logging.basicConfig(format="%(lineno)d    %(message)s", level=logging.INFO)


__all__ = []


# 单行注释
"""
多行注释
多行注释
"""


a = 1
logging.info(isinstance(a, int))
b = True
c = False


s1 = 'abc'
s2 = "def"
s3 = '''xyz'''
s4 = """mnq"""
# 不支持字符串和数值通过+连接
# p("字符串长度: " + len(s4))
logging.info("字符串长度: %d" % len(s4))
logging.info(f"字符串长度: {len(s4)}")
logging.info("字符串长度: {}".format(len(s4)))
len_s4 = len(s4)
logging.info(f"字符串长度: {len_s4=}")


list1 = []
list2 = list()
list1.append(1)
list1.append(2)
list1.append(3)
list2.append(10)
logging.info(f"{list1=}")
logging.info(f"{list2=}")
# extend影响list1
list1.extend(list2)
logging.info(f"{list1=}")
# +方式不影响原始list
list3 = list1 + list2
logging.info(f"{list3=}")
list1.insert(0, -1)
logging.info(f"{list1=}")
# pop是弹出最后的一个元素
pop_from_list1_val = list1.pop()
logging.info(f"{list1=}, {pop_from_list1_val=}")
# remove会移除第一个匹配的元素
list1.remove(-1)
logging.info(f"{list1=}")


dict1 = {}
dict2 = dict()


tuple1 = (0,)
tuple2 = tuple()


for i in list1:
    logging.info(f"test for, {i=}")
for idx, val in enumerate(list1):
    logging.info(f"test for enumerate, {idx=}, {val=}")
for i in range(1, 10):
    logging.info(f"test for break else: {i=}")
    if i > 3:
        # 如果是break出来的，下面的else是不会被执行的，当for循环正常结束，才会执行else分支； while循环类似
        break
else:
    logging.info("for else.")


# False, None, "", 0 和 空列表、字典、元组都属于假
a = True
b = False
c = 1
d = None
e = ""
f = 0
if (a and c) or (not f):
    logging.info('if1')
elif not d:
    logging.info('elif1')
else:
    logging.info('else1')


max_loop = 10
loop = 0
# python没有++ --，可以通过 += 和 -=代替
while loop < max_loop:
    logging.info(f"while loop: {loop}")
    loop += 1


def f1(a, b=2):
    logging.info(f"f1 param: {a=}, {b=}")

def f2(a: int, *, b: int) -> None:
    logging.info(f"f2 param: {a=}, {b=}")

def f3(a, /, b):
    logging.info(f"f3 param: {a=}, {b=}")

def f4(a, *args, **kwargs):
    logging.info(f"f4 param: {a=}, {args=}, {kwargs=}")

f1(1)
f1(1, 3)
# f2的定义方式，*后面的参数，必须使用关键字的方式传递
# f3的/方式已经过时，建议不在使用
f2(1, b=2)
f3(1, 2)
f4(1, 2, 3, 4, x=5, y=6)


class C1:
    a: int = 1

    def __init__(self, x, y, z) -> None:
        self.b = 1
        self.x = x
        self.y = y
        self.z = z

    def get_b(self):
        logging.info(f"running c1 get_b: {self.a=}")
    
    @classmethod
    def c1_cls_method(cls):
        logging.info(f"running c1 class method: {cls=}, {cls.a=}")

    @staticmethod
    def c1_sta_method():
        logging.info(f"running c1 static method: {C1.a=}")
        
# python支持多继承，
class C2(C1, object):
    ...
