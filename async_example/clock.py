import asyncio
import itertools
import time


async def seconds():
    while True:
        for i in range(60):
            print(i)
            await asyncio.sleep(1)


async def minute():
    for i in range(1, 10):
        await asyncio.sleep(60)
        print(i, "min")


async def main():
    await asyncio.gather(seconds(), minute())


asyncio.run(main())
