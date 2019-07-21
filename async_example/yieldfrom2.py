# PEP380 에 나온 서브 제너레이터에 위임하기 구문에 대한 것도 알아봅시다.
# 메인 제너레이터, 서브 제너레이터, 호출자 3가지에 대해서 알아야합니다.
#
# 호출자
# - 대표 제너레이터를 호출하는 코드 주로 메인함수.
# 메인 제너레이터
# - yield from <coroutine> 표현식이 있는 함수.
# 서브 제너레이터
# - yield from <coroutine> 에서 coroutine 역활을 담당하고 있음

# 서브제너레이터
def averager():
    print("averager")
    avg = 0.0
    total = 0
    count = 0
    while True:
        val = yield
        print("위임제너레이터에서 넘어온 값", val)
        if val is None:
            return avg, count
        total += val
        count += 1
        avg = total / count


# 메인 제너레이터
def deligating_gen(results):
    while True:
        result = yield from averager()
        results.append(result)


# 호출자
def main():
    ages = [21, 29, 33, 39]
    weights = [48, 63, 71, 68]
    iterables = [ages, weights]
    results = []
    for iter in iterables:
        gen = deligating_gen(results)
        next(gen)
        print(gen)
        for val in iter:
            print("main in val :", val)
            gen.send(val)
        gen.send(None)
    print("<최종 결과>", results)


main()
