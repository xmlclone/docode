"""
pip install schedule
"""

import schedule
import logging

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


while True:
    schedule.run_pending()