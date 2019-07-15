nums = [1, 2, 3, 4, 5]

# iter, next 를 직접 호출해서
# 잘 동작하는지 실행해봅시다.
it = iter(nums)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# 여기서 중단됨
print(next(it))
