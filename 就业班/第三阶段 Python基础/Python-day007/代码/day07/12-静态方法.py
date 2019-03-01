class Person(object):

    # 实例方法
    def move(self):
        print('走....')

    # 类方法
    @classmethod
    def is_moving(cls):
        print('类方法....')

    # 静态方法
    @staticmethod
    def hello():
        print('静态方法')

xiaoming = Person()
xiaoming.hello()

Person.hello()