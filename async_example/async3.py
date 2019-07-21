import asyncio

# 순차적으로는 해봤으니 동시에 해보자.


@asyncio.coroutine
def hello_delay(delay, say):
    yield from asyncio.sleep(delay)
    print(say)


async def main():
    task1 = asyncio.create_task(hello_delay(1, "hello"))
    task2 = asyncio.create_task(hello_delay(1, "world"))
    task3 = asyncio.create_task(hello_delay(1, "banana"))

    await task1
    await task2
    await task3


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
