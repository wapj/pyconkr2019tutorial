# StopIteration 에서 값을 받아봅시다.


async def greeting(name):
    return "hello " + name


def run(coro):
    try:
        coro.send(None)
    except StopIteration as e:
        return e.value


result = run(greeting("파이콘kr 2019"))

print(result)
