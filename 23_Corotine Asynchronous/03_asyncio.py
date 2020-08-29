import asyncio
import time #可看22_Date Datetime


def hello():
    time.sleep(1)

def run():
    for i in range(5):
        hello()
        print('同步Hello World:%s' % time.time())#從 1970/1/1 00:00:00 至今的秒數

async def hello2():
    asyncio.sleep(1)
    print('異步Hello World:%s' % time.time())

def run2():
    for i in range(5):
        loop.run_until_complete(hello2())

loop = asyncio.get_event_loop()

if __name__ =='__main__':
    run()
    run2()

    

