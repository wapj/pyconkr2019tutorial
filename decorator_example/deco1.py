def decorate(func):
    def decorated():
        print("==" * 20)
        print("before")
        func()
        print("after")

    return decorated


@decorate
def target():
    print("target 함수")


target()

## output
"""
========================================
before
target 함수
after
"""


def target2():
    print("target2 함수 실행함")


target2 = decorate(target2)
target2()

## output
"""

========================================
before
target2 함수 실행함
after
"""
