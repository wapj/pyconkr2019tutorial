def number_gen():
    yield from [10, 20, 30]


for n in number_gen():
    print(n)


# PEP 380 yield form 서브제너레이터로 위임을 위한 문법

# 2가지 사용법이 있는데 첫번째는 아래의 축약형
# for item in iterable:
#     yield item


def g(x):
    yield from range(x, 0, -1)
    yield from range(x)


print(list(g(5)))

arr1 = [1, 2, 3, 4, 5]
arr2 = "ABC"


def chain(iterators):
    for iter in iterators:
        yield from iter


print(list(chain([arr1, arr2])))


# 두번째는 서브제너레이터와 메인제너레이터를 연결하는 일을 할 수 있습니다.
# yield from sub_generator


def average():
    total = 0
    count = 0
    avg = None
    while True:
        next = yield
        if next is None:
            return (avg, count)

        count += 1
        total += next
        avg = total / count


# 대표 제너레이터
# 하위 제너레이터
# 호출자

group1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
group2 = [10, 10, 20, 30, 90]


def group_main_gen():
    while True:
        result = yield from average()
        print(result)


def main():
    for group in [group1, group2]:
        gen = group_main_gen()
        next(gen)
        for val in group:
            gen.send(val)
        gen.send(None)


main()

# 아래의 코드는 result = yield from EXPR 을 단순하게 표현한 것이다.
# throw(), close() 가 생략되어 있음


def yieldfrom():
    EXPR = lambda: ()
    _i = iter(EXPR)
    try:
        _y = next(_i)
    except StopIteration as e:
        r = e.value
    else:
        while 1:
            _s = yield _y
            try:
                _y = i.send(_s)
            except StopIteration as _e:
                r = _e.value
                break
    RESULT = r
