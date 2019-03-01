# print('=-==================')

# 写一个函数打印一条横线
def print_func():
    print('=-==================')

def print_fun1():
    print('-'*40)

# 打印自定义行数的横线
def print_lines(num):
    for i in range(num):
        print('============')


# 嵌套:
def print_lines2(num):
    for i in range(num):
        print_func()

# 计算三个数的和
def sum(a, b, c):
    result = a + b + c
    # print_func(result)
    return result

# 求平均值
def average(a, b, c):
    # result = (a + b + c)/3
    result = sum(a, b, c)
    average = result / 3
    print(average)

average(10, 20, 30)

