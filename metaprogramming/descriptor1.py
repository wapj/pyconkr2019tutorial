class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        # print("__get__")
        try:
            return instance.__dict__[self.name]
        except KeyError:
            return None

    def __set__(self, instance, value):
        # print("__set__", value)
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        # print("__del__")
        del instance.__dict__[self.name]


# 요렇게 사용합니다.
class User:
    name = Descriptor("name")

u = User()
u.name  # name.__get__(u, User)
u.name = "andy"  # name.__set__(u, "andy")
del u.name  # name.__delete__(name)
