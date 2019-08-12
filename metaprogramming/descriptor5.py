# 두개의 클래스를 상속 받는 Descriptor 를 만들어봅시다.
from metaprogramming.descriptor3 import *


class PositiveHundred(Positive, HundredWon):
    pass


# 시리즈 클래스를 조금 수정해 봅시다.
class SeriesProduct:
    title = ReadOnly("title")
    cost_per_page = PositiveHundred("cost_per_page")  # 여기를 변경했어요.
    is_waitfree = Boolean("is_waitfree")
    author = ReadOnly("author")

    def __init__(self, title, author):
        self.__dict__["title"] = title
        self.__dict__["author"] = author


sp = SeriesProduct("나혼자만 레벨업", "장경락")

try:
    sp.cost_per_page = -100
except ValueError as e:
    print(e)

try:
    sp.cost_per_page = 101
except ValueError as e:
    print(e)

"""

그런데 위의 코드 어디서 많이 본것 같지 않나요?? 
네... 맞습니다. djamgo 의 모델 클래스가 Descriptor 를 열심히 사용하고 있습니다. 
이제 장고의 모델 코드를 보실 때 조금 더 이해가 되시겠죠? 
"""
