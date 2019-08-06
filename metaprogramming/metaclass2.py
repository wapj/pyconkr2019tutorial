def make_class(name):
    if name == "daum":
        class Daum:
            pass
        return Daum
    else:
        class Kakao:
            pass
        return Kakao


DaumCls = make_class("daum")
print(DaumCls)
print(DaumCls())


# <class '__main__.make_class.<locals>.Daum'>
# <__main__.make_class.<locals>.Daum object at 0x104149160>