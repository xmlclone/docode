import schedule
import time


count = 0

def task(name):
    print(name)


stoped = False
def stop():
    global stoped
    if count == 10:
        print("clear all task.")
        schedule.clear()
        stoped = True

for i in range(10):
    schedule.every().second.do(task, f"job{i}")

schedule.every().second.do(stop)

while True:
    time.sleep(1)
    schedule.run_pending()
    count += 1
    print('wait...')
    if stoped:
        break

print('end.')