class Person(object):
    # 魔法方法
    # def __new__(cls, *args, **kwargs):
    #     return object.__new__(cls)

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        # print(obj)
        print(id(obj))
        return obj

    def __init__(self, name, age, no):
        self.name = name
        self.age = age
        self.no = no

    def move(self):
        print('move')

xiaoming = Person('小明', 23, '23232')
print(id(xiaoming))
xiaoming.move()

# a = None
# # <class 'NoneType'>
# print(type(a))