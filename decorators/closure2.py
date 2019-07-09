# 고계함수
def make_avg():
    arr = []

    def func(value):
        arr.append(value)
        total = sum(arr)
        return total / len(arr)

    return func


avg = make_avg()


print(avg(10))
print(avg(11))
print(avg(12))
