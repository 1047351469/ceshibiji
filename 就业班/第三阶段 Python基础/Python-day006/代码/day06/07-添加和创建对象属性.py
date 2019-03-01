class Hero(object):

    # 实例方法
    def eat(self):
        print('吃饭....')

wukong = Hero()
wukong.eat()

wukong.name = '悟空'

wukong.hp = 4000

wukong.atk = 50000

print(wukong.name, wukong.hp, wukong.atk)
