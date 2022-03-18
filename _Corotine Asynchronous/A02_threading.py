import threading
import time

def job():
    for i in range(5):
        print('child thread', i)
        time.sleep(1)

t = threading.Thread( target= job )

#執行子執行緒
t.start()

#主執行續繼續自己的工作
for i in range(3):
    print('main thread', i)
    time.sleep(1)

#等待t這個子執行緒結束
t.join

print('done')