import asyncio
from collections import deque

q = deque( range (1, 101))

async def popRight(queue):
    for i in range(10):
        await asyncio.sleep(3)
        print(queue.pop())

async def popLeft(queue):
    for i in range(10):
        await asyncio.sleep(1)
        print(queue.popleft())

async def popBothSide ():
    task1 = asyncio.create_task(popRight(q))
    task2 = asyncio.create_task(popLeft(q))

    await task1
    await task2

asyncio.run(popBothSide())


