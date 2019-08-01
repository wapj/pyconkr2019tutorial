# 클래스의 속성에 validation 을 몇개 추가해봅시다.
# 값을 변경하지 못하도록 하는 ReadOnlyDescriptor
# 100원 단위로만 세팅가능한 HundredWonDescriptor
# 양수만 세팅가능한 PositiveDescriptor 
# True False 만 세팅가능한 BooleanDescriptor 를 만들어 봅시다. 

class ReadOnly(Descriptor):
    # set, delete 시 에러나게 하면 됩니다. 
    def __set__(self, instance, value):
        print(self)
        print(instance)
        print(value)
        raise ValueError("읽기전용입니다.")
        
    def __delete(self, instance):
        raise ValueError("읽기전용입니다.")
        
class Positive(Descriptor):
    def __set__(self, instance, value):
        if isinstance(value, int) and value > 0:
            super().__set__(instance, value)
        else:
            raise ValueError("양수만 세팅가능합니다.")
        
class HundredWon(Descriptor):
    def __set__(self, instance, value):
        if isinstance(value, int) and value % 100 == 0:
            super().__set__(instance, value)
        else:
            raise ValueError("100원 단위로만 세팅가능합니다.")
            
class Boolean(Descriptor):
    def __set__(self, instance, value):
        if isinstance(value, bool):
            super().__set__(instance, value)
        else:
            raise ValueError("True | False 만 세팅가능합니다.")
            