import requests
import time
import asyncio

#此範例為舊的寫法

"""
url = 'https://www.google.com.tw/'

start_time = time.time()

def send_req(url):

    t = time.time()
    print("Send a request at",t-start_time,"seconds.")

    res = requests.get(url)

    t = time.time()
    print("Receive a response at",t-start_time,"seconds.")

for i in range(10):
    send_req(url)
"""

#上面的程式碼對google的入口網站做了十次的request，
#然後對發送request和接收response的時間做了紀錄。
#從收到response到發送request的時間間隔非常短，
#而反之，發送request到收到response的時間卻長很多

url = 'https://www.google.com.tw/'
loop = asyncio.get_event_loop()

start_time = time.time()

async def send_req(url):
    t = time.time()
    print("Send a request at",t-start_time,"seconds.")

    res = await loop.run_in_executor(None,requests.get,url)

    t = time.time()
    print("Receive a response at",t-start_time,"seconds.")

tasks = []

for i in range(10):
    task = loop.create_task(send_req(url))
    tasks.append(task)

loop.run_until_complete(asyncio.wait(tasks))

#測試結果: 原本的程式要0.64秒 異步的只要0.094秒