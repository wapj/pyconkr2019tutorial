class MyClass:
    cls_attr = "클래스 속성이예요 인스턴스를 만들지 않고 읽을 수 있죠"

    def __init__(self, param):
        self.param = param


print(MyClass)
print(MyClass.cls_attr)

obj = MyClass("변수1")

print(obj)  # 인스턴스의 주소가 기본적으로 나옵니다.
print(obj.param)  # 인스턴스의 변수의 값입니다.

# vars(obj) 혹은 dir(obj) 를 사용하면 해당 오브젝트의 속성들을 들여다 볼 수 있습니다.
print(vars(MyClass))
print("================================")
print(vars(obj))

# 변수들은 어디있나요?

print("=======================")
print(MyClass.__dict__)
print(obj.__dict__)
