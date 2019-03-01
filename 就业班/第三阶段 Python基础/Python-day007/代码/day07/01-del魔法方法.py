class Hero(object):
    def __init__(self, name, age, no):
        self.name = name
        self.age = age
        self.no = no

    def __del__(self):
        print('再见吧')

huangjiguang = Hero('黄继光', 23, 'bd0111')
# del huangjiguang
# input('程序停止在这里')

# 引用计数
huang1 = huangjiguang
huang2 = huangjiguang
del huangjiguang
del huang1
del huang2
input('程序停止在这里')