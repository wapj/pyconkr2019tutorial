class Person:

    name = property()  # name 속성은 이제 프로퍼티입니다.
    change_count = 0
    max_change = 2

    def __init__(self, name):
        self._name = name

    @name.getter  # 값을 가져오는 동작을 커스터마이징 합니다.
    def name(self):
        print("이름을 가져옵니다...")
        return self._name

    @name.setter  # 값을 변경하는 동작을 커스터마이징 합니다.
    def name(self, tobe_name):
        print("이름 변경")
        if self.change_count >= self.max_change:
            raise ValueError("개명은 3번이상할 수 없습니다.")

        self.change_count += 1
        self._name = tobe_name


me = Person("andy")
me.name = "생구이"
print(me.name)

me.name = "Andy"
print(me.name)

me.name = "Woodie"
