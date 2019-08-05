import time
import functools


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        before = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_time = time.perf_counter() - before
        arg_str = ",".join(repr(arg) for arg in args)
        if kwargs:
            print("kwargs : ", **kwargs)
        print(f"{elapsed_time:.8f} {func.__name__} {arg_str} {result}")
        return result

    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


print("*" * 40, "call snooze(.123)")
print("func snooze :", snooze)
snooze(0.123)

print("*" * 40, "call factorial(10)")
print("func factorial :", factorial)
print("10! = ", factorial(10))
