'''
http://www.gevent.org/
'''

from gevent import monkey; monkey.patch_all()

import gevent
import logging

from gevent import socket
from gevent.pool import Group
from gevent.event import Event


logging.basicConfig(format="%(asctime)s[%(lineno)d]: %(message)s", level=logging.DEBUG)


def cb1(url):
    logging.debug(f"start {url=}")
    gevent.sleep(1)
    logging.debug(f"end {url=}")
    return url

greenlet = gevent.spawn(cb1, "https://www.test.com")
greenlet.join()
logging.debug(f"{greenlet.value}")


urls = ["https://www.baidu.com", "https://www.gevent.org"]
jobs = [gevent.spawn(cb1, url) for url in urls]
gevent.joinall(jobs, timeout=5)
for job in jobs:
    # job.value获取job的返回值
    logging.debug(job.value)
logging.debug('=' * 100)


# 异常回调
def link_exception_cb1(greenlet: gevent.Greenlet):
    logging.debug(f"{greenlet.exc_info=}")

# 出现异常并不会导致程序结束
greenlet = gevent.spawn(lambda: 1/0)
greenlet.link_exception(link_exception_cb1)
greenlet.join()
# 异常后返回值为None
logging.debug(f"{greenlet.value=}")


# 正常结束时，通过link_value可以获取值
def link_value_cb1(greenlet: gevent.Greenlet):
    logging.debug(f"{greenlet.value=}")
greenlet = gevent.spawn(lambda: 1/2)
greenlet.link_value(link_value_cb1)
greenlet.join()
logging.debug(f"{greenlet.value=}")
logging.debug('=' * 100)


# Group
group = Group()
g1 = group.spawn(cb1, 'https://www.baidu.com')
g2 = group.spawn(cb1, 'https://www.test.com')
group.join()
logging.debug(f"{g1.value=}, {g2.value=}")
logging.debug('=' * 100)


# Event
event = Event()
def cb1():
    logging.debug("cb1 start and wait.")
    # 等待其它greenlet调用set设置flag为True,调用一次即可,所有wait的greenlet都会接收到
    # 设置timeout表示等待的最长时间
    event.wait(timeout=3)
    logging.debug("cb1 end.")

def cb2():
    logging.debug("cb2 start and wait.")
    event.wait()
    logging.debug("cb2 end.")

def cb3():
    logging.debug("cb3 start and sleep4.")
    gevent.sleep(4)
    event.set()
    logging.debug("cb3 end.")

group = Group()
g1 = group.spawn(cb1)
g2 = group.spawn(cb2)
g3 = group.spawn(cb3)
group.join()
logging.debug('=' * 100)