# 시리즈 클래스를 조금 수정해 봅시다. 
class SeriesProduct:
    title = ReadOnly('title') 
    cost_per_page = HundredWon('cost_per_page') 
    is_waitfree = Boolean("is_waitfree")
    author = ReadOnly("author")
    
    def __init__(self, title, author):
        self.__dict__['title'] = title
        self.__dict__['author'] = author

sp = SeriesProduct('나혼자만 레벨업', '장경락')

print(sp.__dict__)
sp.cost_per_page = 100
sp.is_waitfree = True

print(sp.__dict__)


sp.title = '독고'

# 문제가 하나 있습니다. 
# 음수로 세팅이 가능해요
sp.cost_per_page = -100

print(sp.__dict__)

