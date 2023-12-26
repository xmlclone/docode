"""
pip install schedule

验证时间周期冲突，是否会同时执行
"""

import schedule
import logging
import time

logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)

def job(name):
    logging.info(f"{name}, start")
    time.sleep(5)
    logging.info(f"{name}, end")


def job2(name):
    logging.info(f"{name}, start")
    time.sleep(60)
    logging.info(f"{name}, end")


# 所有任务都固定一个时间点启动，并且每个任务都等待了一定时间
second = ":15"
# task = job
# 如果一个job占用的时间过长，已经到了下一个周期时间，也是按序执行
"""job2的测试结果
2023-12-15 10:56:15,000 job1, start
2023-12-15 10:57:15,000 job1, end
2023-12-15 10:57:15,000 job2, start
2023-12-15 10:58:15,003 job2, end
2023-12-15 10:58:15,003 job3, start
2023-12-15 10:59:15,009 job3, end
2023-12-15 10:59:15,009 job1, start
"""
task = job2

# 最终结果测试出来，并没有利用多线程之类的，一定会等前一个任务结束后，下一个任务才启动
"""job的测试结果
2023-12-15 10:54:15,000 job1, start
2023-12-15 10:54:20,001 job1, end
2023-12-15 10:54:20,001 job2, start
2023-12-15 10:54:25,002 job2, end
2023-12-15 10:54:25,002 job3, start
2023-12-15 10:54:30,003 job3, end
"""
schedule.every().minutes.at(second).do(task, 'job1')
schedule.every().minutes.at(second).do(task, 'job2')
schedule.every().minutes.at(second).do(task, 'job3')


while True:
    schedule.run_pending()