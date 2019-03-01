class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('能吃饭....')

class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.color = '黑色'

    def eat(self):
        print('能吃饭...')

xiaoming = Person('小明', 23)
# print(xiaoming.name, xiaoming.age)
# xiaoming.eat()

wangcai = Dog('旺财', 1)
# print(wangcai.name, wangcai.age)
# wangcai.eat()


def pirnt_func(object):
    print(object.name, object.age)
    object.eat()

pirnt_func(xiaoming)
pirnt_func(wangcai)
