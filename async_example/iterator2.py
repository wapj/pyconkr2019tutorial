# for num in nums 에서는 무슨일이 일어날까요?
# 실제로는 아래와 같은 형태로 구현되어 있습니다.
# iter 함수로 iterator 를 만들고
# next 를 사용해서 하나씩 꺼내오게 됩니다.
# 더이상 꺼내올 것이 없으면 StopIteration 이 나면서 종료됩니다.

nums = [1, 2, 3, 4, 5]

iter_obj = iter(nums)
while True:
    try:
        el = next(iter_obj)
        print(el)
    except StopIteration:
        break
