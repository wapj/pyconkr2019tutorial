# iter 함수를 사용해서 iterator 로 만드려면 iterable 이어야 합니다.
# 그림에서 봤던대로 iterable 은 __iter__() 메서드를 구현해주면 됩니다
# for loop 에서 사용할 수 있게 iterator 가 되려면 __next__() 함수도 구현해주어야 합니다.
# 루프를 돌때마다 1씩 증가하고 5까지만 세어주는
# Counter5 클래스를 만들고 __iter__(), __next__() 함수를 구현해 줍시다.
# __next__ 에서 리턴해줄 것이 없으면 StopIteration 이 나도록 해주면 for loop 에서 빠져나오게 됩니다.


class Counter5:
    LIMIT = 5

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        val = self.num
        self.num += 1
        if self.LIMIT < val:
            raise StopIteration
        return val


counter = Counter5()
for n in counter:
    print(n)
