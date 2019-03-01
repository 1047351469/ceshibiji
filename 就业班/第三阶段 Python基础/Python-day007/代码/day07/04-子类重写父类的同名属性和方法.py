class Master(object):
    def __init__(self):
        self.peifang = '古法煎饼果子'

    def make_cake(self):
        print('按照%s制作煎饼果子...' % self.peifang)

    def dayangqiang(self):
        print('大烟枪')

class School(object):
    def __init__(self):
        self.peifang = '现代煎饼果子配方'

    def make_cake(self):
        print('按照%s制作煎饼果子...' % self.peifang)

    def xiaoyangqiang(self):
        print('小烟枪')

class Prentice(Master, School):
    def __init__(self):
        self.peifang = '大猫姜饼果子配方'

    def make_cake(self):
        print('按照%s制作煎饼果子....' % self.peifang)


damao = Prentice()
print(damao.peifang)
damao.make_cake()

