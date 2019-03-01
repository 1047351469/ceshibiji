class Hero(object):
    def __init__(self, new_name, new_hp, new_atk):
        self.name = new_name
        self.hp = new_hp
        self.atk = new_atk

    # 实例方法
    def eat(self):
        print('吃饭....')
        # print(self.name, self.hp, self.atk)

wukong = Hero('悟空', 4000, 50000)
wukong.eat()

gailun = Hero('盖伦', 3000, 20000)
gailun.eat()