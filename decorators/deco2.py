deco2 = []


def register(func):
    print(f'레지스트리에 등록! {func}')
    deco2.append(func)
    return func


@register
def f1():
    print('f1 실행')


@register
def f2():
    print('f2 실행')


@register
def f3():
    print('f3 실행')


def main():
    print('============================')
    print(f'레지스트리에 등록된거 보실? {deco2}')
    f1()
    f2()
    f3()


if __name__ == '__main__':
    main()

"""output
레지스트리에 등록! <function f1 at 0x10cb602f0>
레지스트리에 등록! <function f2 at 0x10cb60378>
레지스트리에 등록! <function f3 at 0x10cb60400>
============================
레지스트리에 등록된거 보실? [<function f1 at 0x10cb602f0>, <function f2 at 0x10cb60378>, <function f3 at 0x10cb60400>]
f1 실행
f2 실행
f3 실행
"""
