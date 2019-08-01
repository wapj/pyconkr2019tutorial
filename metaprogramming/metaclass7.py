class ModelMeta(type):
    
    def __new__(cls, name, bases, attrs):
        print(cls, name, bases, attrs)
        if 'app_label' not in attrs:
            raise RuntimeError(f"{name} 클래스에 app_label 을 정의해주세요!")
        return type.__new__(cls, name, bases, attrs)
    
class ModelBase(metaclass=ModelMeta):
    app_label = ''

class GoodModel(ModelBase):
    app_label = 'good_app'

m = Model()

print(m.app_label)

# 여기서 에러가 납니다.
class BadModel(ModelBase):
    pass