class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        print(cls, name, bases, attrs)
        if "app_label" not in attrs:
            raise RuntimeError(f"{name} 클래스에 app_label 을 정의해주세요!")
        return type.__new__(cls, name, bases, attrs)


class ModelBase(metaclass=ModelMeta):
    app_label = ""


class GoodModel(ModelBase):
    app_label = "good_app"


m = GoodModel()

print(m.app_label)


# 여기서 에러가 납니다.
class BadModel(ModelBase):
    pass


def func():
    print("hello")


def decorator(fun):
    def decorated():
        # 어떤 처리
        result = fun()
        return result

    return decorated  # 함수를 반환, 혹은 대체


fun2 = decorator(func)


@decorator
def fn2():
    print("helloooo")
