import logging

from collections import (
    namedtuple,
    deque,
    defaultdict,
    Counter,
    OrderedDict
)


logging.basicConfig(format="%(lineno)dline:  %(message)s", level=logging.INFO)


print('=' * 100)
print('namedtuple示例')
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
print('=' * 100)


print('deque示例')
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

def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    logging.info(iterables) # ('ABC', 'D', 'EF')
    iterators = deque(map(iter, iterables)) # ['ABC', 'D', 'EF'] 但是注意，这里的三个元素，每个都已经是一个迭代器
    # print(list(iterators))
    while iterators:
        try:
            while True:
                # iterators[0]就是deque的第一个元素(一共3个元素，每个都是迭代器)
                # next就是每次返回deque第一个元素的第一个值
                yield next(iterators[0])
                # 然后把iterators往前移动
                iterators.rotate(-1)
        except StopIteration:
            # Remove an exhausted iterator.
            # 当deque的某个元素(一共3个元素)无法迭代的时候，就把它从左边弹出去，因为前面已经往前移动了
            iterators.popleft()

# roundrobin1('ABC', 'D', 'EF')
print(list(roundrobin('ABC', 'D', 'EF')))
print('=' * 100)