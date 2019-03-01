def fun(a, b):
    return a + b


fun(10, 123)



func1 = lambda a, b: a + b

func1(10, 12)

# def fun1(a, b):
#     print('-----------')
#     fun(a, b)
#     print('==============')

def func(a, b, opt):
    print('a:%d' % a)
    print('b:%d' % b)
    print('result:%d' % opt(a, b))

func(1, 2, lambda x, y : x + y)

opt =  lambda x, y : x + y

opt(x, y)