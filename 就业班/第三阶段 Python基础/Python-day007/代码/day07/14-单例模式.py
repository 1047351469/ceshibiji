class Hero(object):
    # 类属性
    __instance = 0
    __isFirst = True

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, name, age):
        if Hero.__isFirst:
            self.name = name
            self.age = age
            Hero.__isFirst = False

wukong = Hero('悟空', 3000)
wukong1 = Hero('悟空1111', 111)

print(id(wukong))
print(id(wukong1))
print(wukong.name, wukong.age, wukong1.name, wukong1.age)



def func1():
    isTrue = True
    if isTrue:
        print('111111')
        isTrue = False

func1()
func1()
func1()
func1()








# def add2num(a, b):
#     result = a + b
#     return result
#
# add2num(10, 20)
# add2num(20, 30)
