class Avg:
    def __init__(self):
        self.nums = []

    def __call__(self, value):
        self.nums.append(value)
        total = sum(self.nums)
        return total / len(self.nums)


avg = Avg()


print(avg(10))
print(avg(11))
print(avg(12))
