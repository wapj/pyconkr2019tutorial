import asyncio

# 순차적으로는 해봤으니 동시에 실행시켜봅시다.
import time


@asyncio.coroutine
def hello_delay(delay, say):
    yield from asyncio.sleep(delay)
    print(say)


def main():
    task1 = asyncio.create_task(hello_delay(1, "hello"))
    task2 = asyncio.create_task(hello_delay(1, "world"))
    task3 = asyncio.create_task(hello_delay(1, "banana"))

    yield from task1
    yield from task2
    yield from task3


start = time.perf_counter()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
end = time.perf_counter()

print(f"elapsed time : {end - start}")
