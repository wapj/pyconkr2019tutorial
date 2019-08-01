class Descroptor:

    def __init__(self, name):
        self.name = name

    def __get__(self, instnace, cls):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        return instance.__dict__[self.name] = value
    
    def __delete__(self, instance):
        del instance.__dict__[self.name]

