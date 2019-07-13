# async 를 공부하자고 하는데 좀 쌩뚱맞을 수 있지만
# 간단히 1부터 5까지 표시해주는 for loop 를 만들어봅시다.
# 나중에 이야기 하겠지만, 이 간단한 아이디어에서 async 가 시작되기때문에 그렇습니다.

nums = [1,2,3,4,5]

for num in nums:
    print(num)

# for num in nums 에서는 무슨일이 일어날까요?
# nums 는 iterable 입니다.
# 영어의 뜻을 풀면 반복가능하다는 뜻인데요.
# 파이썬에서는 __iter__() 메서드를 가지고 있다는 뜻입니다.
# dir(nums) 를 실행해서 확인해 봅시다.


print(type(nums))


# [... 중략 '__iter__' ...]
# __iter__ 메서드가 있군요!
#
print(nums.__iter__())

# yield 는 반복자 패턴을 추상화 할 수 있도록 하기위해 python 2.2 에 추가되었다.
# yield 키워드는 제너레이터를 생성할 수 있게 해준다.

print(type(range(10)))

for n in range(10):
    print(n)


