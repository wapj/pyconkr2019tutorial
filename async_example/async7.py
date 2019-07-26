import asyncio
import itertools

"""뺑글이 만들기"""


async def spin(msg):
    for char in itertools.cycle("|/-\\"):
        status = char + " " + msg
        print(status, flush=True, end="\r")
        try:
            await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            break
    print(" " * len(status), end="\r")


async def runner():
    spinner = asyncio.create_task(spin("wait for it~"))
    print("spinner ", spinner)
    await asyncio.sleep(3)
    spinner.cancel()  # 스레드 버전은 Task 를 중단할 수 없지만, async await 는 가능하다.
    print("Legendary~~~! ")


result = asyncio.run(runner())

# asyncio.create_task(coro)
# 코루틴을 Task 로 감싸고 Task 객체를 리턴합니다.

# asyncio.create_task(coro)
# 코루틴을 Task 로 감싸고 Task 객체를 리턴합니다.

"""


이제 조금 더 쓸만한 예제를 만들어 봅시다.
[aiohttp](https://github.com/aio-libs/aiohttp) 패키지가 필요합니다.

`pip install aiohttp` 로 설치해줍시다.

"http://pycon.gyus.me/test.txt" 파일이 있습니다. 요녀석을 읽는 스크립트를 작성해 봅시다.

"""
