import asyncio


@asyncio.coroutine
def hello(msg):
    yield from asyncio.sleep(1)
    print(msg)


loop = asyncio.get_event_loop()
loop.run_until_complete(hello("안녕!"))
