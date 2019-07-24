# async 가 어떻게 실행되고 결과값을 주는지 한번 볼까요?


async def greeting(name):
    return "hello " + name


coro = greeting("Andy")
coro.send(None)

# output
"""
Traceback (most recent call last):
  File "/Users/gyus/dev/python/pycon2019/async_example/async4.py", line 9, in <module>
    coro.send(None)
StopIteration: hello Andy
"""
