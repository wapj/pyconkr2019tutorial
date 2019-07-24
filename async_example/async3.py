import asyncio

# 3.6부터는 사실상 yield from 을 사용하지 않아도 됩니다.
# yield from 은 우리 기억에만 남겨둡시다.
# yield from 으로 했던것들을 asyncio 로 변경해봅시다.
import time


async def hello_delay(delay, say):
    await asyncio.sleep(delay)
    print(say)


async def main():
    task1 = asyncio.create_task(hello_delay(1, "안녕"))
    task2 = asyncio.create_task(hello_delay(1, "async 의 세계로 온것을"))
    task3 = asyncio.create_task(hello_delay(1, "환영해"))

    await task1
    await task2
    await task3


start = time.perf_counter()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
end = time.perf_counter()

print(f"elapsed time : {end - start}")
