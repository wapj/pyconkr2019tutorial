# generator 는 iterator 를 만들어내는 함수라고 일단 생각합시다.
# 아래와 같이 바꿔봅시다.


def count_to(n):
    num = 1
    while num <= n:
        yield num
        num += 1


counter = count_to(5)
print(type(counter))
print(list(counter))
