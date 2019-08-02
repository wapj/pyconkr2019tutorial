import functools


def title(symbol, len=20):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(symbol * len)
            result = func(*args, **kwargs)
            print(symbol * len)
            return result

        return wrapper

    return decorator


@title("*", 15)
def print_name(name):
    print(name)
    return name


@title("-", 10)
def print_company(company):
    print(company)
    return company


print_name("seungkyoo park")
print_company("kakaopage")
