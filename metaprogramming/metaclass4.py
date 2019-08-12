# type으로 클래스를 만들어보자
Water = type("Water", (), {"taste": "무맛", "color": "투명", "state": "liquid"})

print(Water)  # class
print(Water())  # object
print(Water.taste)
print(Water.color)

# 부모클래스도 넣어보자
Cola = type("Cola", (Water,), {"taste": "콜라맛", "color": "black", "price": 500})
print(Cola)
print(Cola())
print(Cola.price)


def is_liquid(self):
    return self.state == "liquid"


SparklingWater = type(
    "SparklingWater", (Water,), {"taste": "탄산맛", "is_liquid": is_liquid, "price": 600}
)

print(hasattr(Cola, "state"))  # true
print(hasattr(SparklingWater, "state"))  # true

spwater = SparklingWater()
print(spwater.is_liquid())


# 동적으로 함수를 추가 할 수도 있어요.
def discount10(self):
    return self.price * 0.9


SparklingWater.discount = discount10
print(hasattr(SparklingWater, "discount"))  # true
