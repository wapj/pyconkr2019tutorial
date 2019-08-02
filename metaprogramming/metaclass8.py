class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        if "app_label" not in attrs:
            raise RuntimeError(f"{name} 클래스에 app_label 을 정의해주세요!")
        return type.__new__(cls, name, bases, attrs)

    @classmethod
    def __prepare__(cls, name, bases):

        return {"app_label": name}


class ModelBase(metaclass=ModelMeta):
    app_label = ""


class GoodModel(ModelBase):
    app_label = "good_app"


m = GoodModel()

print(m.app_label)


class NotBadModel(ModelBase):
    pass


m2 = NotBadModel()
print(m2.app_label)
