__all__ = ['name']

name = 'xiaoming'


def add2num(a, b):
    return  a + b

class Person(object):
    def move(self):
        print('move...')



def main():
    print(name)

    ret = add2num(10, 20)
    print(ret)


# main()

# 模块中有一个变量    __name__
# print(__name__)

if __name__ == '__main__':
    main()

