# x는 글로벌 변수이다.
# foo 함수 내에서 x는 자유 변수이다.
x = 1
def foo():
    print(x)


# outer_func는 지역변수 n이 있다.
# inner_func 에는 지역변수 m 과 n 이 있다.
def outer_func():
    n = 1
    def inner_func():
        m = 2
        print(n)
        print(m)

    return inner_func
func = outer_func()
print(func.__code__.co_freevars)
