import logging

from collections import (
    namedtuple,
    deque,
    defaultdict,
    Counter,
    OrderedDict
)


logging.basicConfig(format="%(lineno)dline:  %(message)s", level=logging.INFO)


Point1 = namedtuple("Point1", ['x', 'y'])
p1 = Point1(x=1, y=2)
logging.info(f"{p1.x=}, {p1.y=}; {p1[0]=}, {p1[1]=}, {p1._asdict()}")
Point2 = namedtuple("Point2", "m, n")
p2 = Point2(11, 22)
logging.info(f"{p2.m=}, {p2.n=}; {p2[0]=}, {p2[1]=}")
# 不支持直接修改namedtuple的属性，只能通过_replace方法，并且也不是修改元素namedtuple
# 可以理解为，这就是一个tuple，不允许改变的
# p1.x = 100  # AttributeError
new_p1 = p1._replace(x=100)
logging.info(f"{new_p1.x=}")
# 默认值的设置
# x是需要设置的，y默认值1，z默认值2
Point3 = namedtuple("Point3", ['x', 'y', 'z'], defaults=[1, 2])
p3 = Point3(5)
logging.info(p3._asdict())


deque1 = deque()
deque1.append(1)
deque1.append(2)
deque1.append(3)
logging.info(f"{deque1=}")
deque1.appendleft(0)
logging.info(f"{deque1=}")
v = deque1.pop()
logging.info(f"{deque1=}, {v=}")
v = deque1.popleft()
logging.info(f"{deque1=}, {v=}")

