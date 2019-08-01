# 파이썬에서는 클래스의 속성들을 동적으로 다루기가 쉽습니다.
# 아래와 같이 매우 직관적입니다.

class B:
    pass

class A(B):
    
    e = 'ee'
    
    def __init__(self, c):
        self.c = c
        
    def d(self):
        return 'dd'
    
a = A('cc')
print(a.c)
print(a.d())
print(a.e)

a.f = 'ff'
print(a.f)

a.g = lambda: 'gg'
print(a.g())
