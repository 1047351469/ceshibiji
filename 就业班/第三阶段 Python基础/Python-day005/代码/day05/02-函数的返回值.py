# str1 = 'hello world'
#
# num1 = len(str1)
# print(num1)

def add2num(a, b):
    result = a + b
    print(result)
    return result

num1 = add2num(10, 12)
print(num1)

# pi
pi = 3.14159263848328438

def pi_func():
    return 3.14159263848328438

num2 = pi_func()
print(pi_func())
print(num2)

# 需求: 有两个字符串, 需要定义一个函数把这两个字符串
# 进行拼接操作,然后返回
str1 = 'hello '
str2 = 'world'
def str2str(a, b):
    # result = a + ' ' + b
    result = a + b
    return result
    # 换一种写法:
    # return a + b


str3 =  str2str(str1, str2)
print(str3)


# 递归
def deep(num):
    print(num)
    if num == 20:
        return
    num += 1
    return deep(num)

deep(1)

# return:
#   1.返回: return 数据
#   2.结束函数:  return
# 一旦在函数中执行到return以后, 后面的代码不会执行
def print_func():
    print('-=--------------')
    print('hello world')
    return 'hello world'
    print('=================')
    print('****************')
    return 123
    print('44444444444444444')

result = print_func()
print(result)
