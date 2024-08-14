"""
pip install schedule
"""

import schedule
import logging
import time
from datetime import datetime, timedelta

logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)

def job(name):
    logging.info(name)

# 每隔2s执行一次
schedule.every(2).seconds.do(job, 'job1')
# 每隔2s-10s之间随机执行一次(不是2-10s执行结束)
schedule.every(2).to(10).seconds.do(job, 'job2')

schedule.every().seconds.do(job, 'job3')

# job表示上面设置了多少个schedule，并不影响循环执行
print(len(schedule.jobs))

# for j in schedule.jobs:
    # for a in dir(j):
    #     if not a.startswith('__'):
    #         try:
    #             print(a, getattr(j, a))
    #         except:
    #             pass
    # break
    # print(j.next_run)

g_next_run_time = None
def print_next_run():
    global g_next_run_time
    next_run_time = schedule.jobs[0].next_run
    for job in schedule.jobs:
        job_run_time = job.next_run
        if job_run_time < next_run_time:
            next_run_time = job_run_time
    if g_next_run_time != next_run_time:
        g_next_run_time = next_run_time
        print("下一个周期:", g_next_run_time)

while True:
    print_next_run()
    schedule.run_pending()