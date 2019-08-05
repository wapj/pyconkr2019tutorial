import time
import functools

DEFAULT_FORMAT = "[ELAPSED_TIME : {elapsed_time:.8f}] {name} {_args} -> {result}"


def clock(format=DEFAULT_FORMAT):
    def decorator(func):
        @functools.wraps(func)
        def clocked(*args, **kwargs):
            before = time.perf_counter()
            result = func(*args, **kwargs)
            _args = ",".join(repr(arg) for arg in args)
            elapsed_time = time.perf_counter() - before
            name = func.__name__
            print(format.format(**locals()))
            return result

        return clocked

    return decorator


@clock()
def snooze(seconds):
    time.sleep(seconds)


@clock("[{name}] calls spend {elapsed_time:.8f} s")
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


print("*" * 40, "call snooze(.123)")
snooze(0.123)

print("*" * 40, "call factorial(10)")
print("10! = ", factorial(10))
