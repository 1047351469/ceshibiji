class Master(object):
    def __init__(self):
        self.peifang = '古法煎饼果子配方'

    def make_cake(self):
        print('按照%s进行制作...' % self.peifang)

# lishifu = Master()
# lishifu.peifang
# lishifu.make_cake()

class Prentice(Master):
    pass

damao = Prentice()
print(damao.peifang)
damao.make_cake()
