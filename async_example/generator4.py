# 제너레이터로 구구단도 만들어봅시다.
def gugu_gen():
    for x in range(1, 10):
        for y in range(1, 10):
            print(f"{x} * {y} = ", end="")
            yield x * y


gugu = gugu_gen()

for result in gugu:
    print(result)
