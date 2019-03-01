# 1)   无参数，无返回值的函数
def print_func():
    print('我还会回来的~~~~~ * ')

print_func()

# 2)  无参数，有返回值的函数
def pi_func():
    return 3.141592628383283838283

print(pi_func())

# 3)  有参数，无返回值的函数
def print_name_func(name):
    print('名字是:%s' % name)

# print_name_func('小明')

list = ['数字工厂', '狼厂', '鹅厂', '鸟厂', '度娘', '马厂']
for value in list:
    print_name_func(value)


# 4) 有参数，有返回值的函数
def sumTo100(num):
    sum = 0
    for i in range(num):
        i += 1
        sum += i
    return sum

sum =  sumTo100(100)
print(sum)


 







