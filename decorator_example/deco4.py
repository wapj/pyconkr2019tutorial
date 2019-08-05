import functools

# 파라메터가 있는 데커레이터를 위한 템플릿
def decorator_with_param(param):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 전처리
            result = func(*args, **kwargs)
            # 후처리
            return result

        return wrapper

    return decorator
