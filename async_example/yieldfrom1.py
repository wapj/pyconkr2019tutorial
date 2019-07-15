def yf():
    result = yield from range(10, 100, 10)
    print(result)
    return result
