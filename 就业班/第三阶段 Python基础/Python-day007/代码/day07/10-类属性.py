class Person(object):
    # 类属性
    country = '中国'

    def __init__(self, name, age):
        # 实例属性 (对象属性)
        self.name = name
        self.age = age
        # self.country = '中华'

    # 实例方法
    def move(self):
        print('再走....')

xiaoming = Person('小明', 23)

# 访问
# 1. 可以通过对象访问类属性
# 对象名.类属性名
print(xiaoming.country)
# 2. 可以通过类访问类属性
# 类名.类属性名
print(Person.country)

# 修改
# 错误的: 用对象名修改类属性是不可行的
# xiaoming.country = '中华'
# print(xiaoming.country)
# print(Person.country)

# 类名.类属性名 = 新值
Person.country = '中华'
print(Person.country)
print(xiaoming.country)
