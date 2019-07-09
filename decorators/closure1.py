# 함수 본체 안에서 값을 할당하기 때문에 지역변수가 되는 b
b = 6


def f2(a):
    global b
    print('a = ', a)
    print('b = ', b)
    b = 10


f2(1)
