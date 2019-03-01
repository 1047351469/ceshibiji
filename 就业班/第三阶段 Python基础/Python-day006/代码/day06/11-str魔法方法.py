class Hero(object):
    def __init__(self, new_name, new_hp, new_atk):
        self.name = new_name
        self.hp = new_hp
        self.atk = new_atk

    # str魔法方法: 没有参数, 只有一个返回值
    # 而且这个返回值必须是一个字符串
    def __str__(self):
        return '%s %s %s' % (self.name, self.hp, self.atk)

    # 实例化方法
    # def info(self):
    #     print(self.name, self.hp, self.atk)

wukong = Hero('悟空', 4000, 50000)
# wukong.info()
print(wukong)
# <__main__.Hero object at 0x0000000001E4E898>
