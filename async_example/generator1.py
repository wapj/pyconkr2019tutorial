# Counter 클래스는 아래와 같이 제너레이터로 변경할 수 있습니다.
# yield 는 iterator 를 추상화 하기 위해 Python 2.2 에 추가되었습니다.


def gen_1_to_5():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


counter = gen_1_to_5()
print(type(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

# StopIteration 발생
# print(next(counter))

# 리스트로 바로 변경할 수 있습니다.
print(list(count_to(5)))
