class Master(object):
    def __init__(self):
        # 加两个下划线__ 就会变成私有的.
        self.__money = 10000000

    # 定义一个获取私有属性的方法
    def get_money(self):
        return self.__money

    # 修改私有属性
    def set_money(self, new_money):
        if new_money > 0:
            self.__money = new_money
        print(self.__money)

class Prentice(Master):
    pass

damao = Prentice()
money = damao.get_money()
print(money)

damao.set_money(3000)