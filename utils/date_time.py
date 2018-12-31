import time

epoch_seconds = time.time()
start_time = time.perf_counter()

print('time in seconds from begining coutint - 1.1.1970',epoch_seconds)

print('Current Time is',time.ctime(epoch_seconds))

import datetime

time.sleep(2)

dt = datetime.datetime.today()
print('Current time with datatime module',dt)
print(dt.day,dt.month,dt.year, dt.hour,dt.minute)
end_time = time.perf_counter()

print('take',end_time-start_time,'seconds')