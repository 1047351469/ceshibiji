class Master(object):
    def __init__(self):
        self.peifang = '古法煎饼果子'
        # 加两个下划线__ 就会变成私有的.
        self.__money = 10000000

    def __secret_make_cake(self):
        print('secret_make_cake')

class School(object):
    def __init__(self):
        self.peifang = '现代煎饼果子配方'



class Prentice(Master, School):
    # def __init__(self):
    #     # self.peifang = '大猫的配方...'
    #     pass
    pass

damao = Prentice()
# print(damao.peifang)
# print(damao.money)
damao.__secret_make_cake()