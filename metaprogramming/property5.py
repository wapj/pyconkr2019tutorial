class UpperCase:
    def __init__(self, name):
        self.name = name

    def __getattribute__(self, name):
        print(name)
        print(self.__dict__)
        if name in self.__dict__:
            return self.name.upper()
        return name.upper()


uc = UpperCase("abc")
print(uc.aa)
