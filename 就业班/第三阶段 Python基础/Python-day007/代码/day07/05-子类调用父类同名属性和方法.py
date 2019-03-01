class Master(object):
    def __init__(self):
        self.peifang = '古法煎饼果子'

    def make_cake(self):
        print('按照古法煎饼果子制作煎饼果子...')

    def dayangqiang(self):
        print('大烟枪')

class School(object):
    def __init__(self):
        self.peifang = '现代煎饼果子配方'

    def make_cake(self):
        print('按照现代煎饼果子配方制作煎饼果子...')

    def xiaoyangqiang(self):
        print('小烟枪')

class Prentice(Master, School):
    def __init__(self):
        self.peifang = '大猫姜饼果子配方'

    def make_cake(self):
        print('按照%s制作煎饼果子....' % self.peifang)

    def old_make_cake(self):
        Master.make_cake(self)

    def new_make_cake(self):
        School.make_cake(self)

damao = Prentice()
damao.make_cake()

damao.old_make_cake()

damao.new_make_cake()