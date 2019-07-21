import asyncio
import time

# 파이썬을 만든 귀도반 로썸은
# tulip 프로젝트를(asyncio) 소개하는 슬라이드에서 아래와 같이 적어두었습니다.
# Tasks vs coroutines

# res = yield from some_coroutine()
# res = yield from Task(some_coroutine())

# 태스크로 실행할 때의 차이는 기다리지 않고 실행된다는 점입니다.
# 예제로 확인해봅시다.


@asyncio.coroutine
def hello(msg):
    yield from asyncio.sleep(1)
    yield from asyncio.sleep(1)
    yield from asyncio.sleep(1)
    print(msg)


start = time.perf_counter()
loop = asyncio.get_event_loop()
loop.run_until_complete(hello("안녕!"))
end = time.perf_counter()

print(f"elapsed time : {end - start}")
