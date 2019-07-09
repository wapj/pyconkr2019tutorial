# 변수 범위 규칙
def f1(a):
    print(a)
    print(b)


# 에러남
f1(3)

# 성공
b = 6
f1(3)
