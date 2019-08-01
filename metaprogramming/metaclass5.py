# meta class 에서는 __init__ 보다는 __new__ 를 사용합니다. 
# 사용법은 아래와 같습니다. 
# __new__ (<클래스자신>, <클래스명>,  (클래스의 부모 클래스), {클래스의 어트리뷰트 딕셔너리} )
# __new__ 가 실행된 다음에 __init__ 가 실행되게 됩니다. 
class Meta(type):
    def __new__(cls, name, bases, attrs):
        print("__new__ 메서드!")
        print(cls, name, bases, attrs)
        return type.__new__(cls, name, bases, attrs)
    
    def __init__(cls, name, bases, attrs):
        print("__init__ 메서드")
        type.__init__(cls, name, bases, attrs)
        

print("=================================")
print("<메타클래스가 초기화 됩니다.>")
class MyClass(metaclass=Meta):
    pass
print("=================================")

# print 로 찍은 값을 보시면 그저 클래스를 정의만 했는데 
# 메타클래스가 어딘가 생성된것을 볼 수 있습니다. 
