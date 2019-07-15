# 코루틴으로 이동편균 구하기
# @coroutine 으로 코루틴 기동시키기
# 결과값을 받아보기
import functools


def coroutine(func):
    @functools.wraps(func)
    def wraped(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return wraped


@coroutine
def averager():
    sum = 0.0
    count = 0
    average = None
    while True:
        n = yield average
        if n is None:
            break
        sum += n
        count += 1
        average = sum / count
    return (count, average)


coro_avg = averager()
print(coro_avg.send(10))
print(coro_avg.send(20))
print(coro_avg.send(30))
# stop Iteration 이 발생! 하지만 결과값이 들어있다!
try:
    print(coro_avg.send(None))
except StopIteration as exc:
    result = exc.value

print(result)
