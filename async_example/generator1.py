nums = [1, 2, 3, 4, 5]


def double_nums(nums):
    arr = []
    for n in nums:
        arr.append(n * 2)

    return arr



def double_nums2(nums):

    for n in nums:
        yield (n * 2)



# 모든결과를 메모리에 가지고 있음
print(double_nums(nums))

# 하나의 결과만 가지고 있음
nums_gen = double_nums2(nums)

print (next(nums_gen))
print (next(nums_gen))
print (next(nums_gen))
print (next(nums_gen))
print (next(nums_gen))

# stop iteration : 범위를 벚어났음을 알려줌


nums_gen2 = double_nums2(nums)

for num in nums_gen2:
    print(num)

nums_gen3 = double_nums2(nums)
nums3 = [ n * 2 for n in nums_gen3]

print(nums3)