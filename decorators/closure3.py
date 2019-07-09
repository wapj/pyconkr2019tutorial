def make_avg2():
    count = 0
    total = 0

    def func(value):
        nonlocal count, total
        count += 1
        total += value
        return total / count

    return func


avg = make_avg2()


print(avg(10))
print(avg(11))
print(avg(12))
