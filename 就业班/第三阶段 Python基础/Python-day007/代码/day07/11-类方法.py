# class Person(object):
#
#     # 实例方法
#     def move(self):
#         print('走....')
#
#     # 类方法
#     @classmethod
#     def is_moving(self):
#         print('类方法....')
#
# # 类可以调用类方法
# Person.is_moving()
# # 对象能调用类方法
# xiaoming = Person()
# xiaoming.is_moving()



class Person(object):

    # 私有类属性
    __money = 10000

    # cls: 当前类
    @classmethod
    def get_money(cls):
        return cls.__money

    @classmethod
    def set_money(cls, new_money):
        cls.__money = new_money


    # 一般不会定义成实例化方法, 一般会用类方法
    # # 实例化方法访问
    # def get_money(self):
    #     return self.__money
    #
    # # 实例化方法修改
    # def set_money(self, new_money):
    #     self.__money = new_money
