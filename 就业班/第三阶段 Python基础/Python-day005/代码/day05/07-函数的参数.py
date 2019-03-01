# 位置参数
def add3num(a, b, c):
    result = a + b + c
    print(result)

add3num(10, 20, 30)

# 关键字参数
def add3str(str1, str2, str3):
    result =  str1 + (str2  + str3)
    print(result)

# add3str(str2='hello', str3='world', str1='nihao')

add3str('hello', str3='world', str2='nihao')


# 缺省参数 : 缺省参数就是默认值
def print_info(name,  no='2345', age=23):
    new_name = '名字是:%s' % name
    new_no = '学号是:%s' % no
    new_age = '年龄是:%d' % age
    print(new_name, new_no, new_age)

print_info('小明', '2345')
print_info('小红', '2346')
print_info('小张', '2347', 25)

a = 1
b = 2
c = 3

# def add3num(a, b, c):
#     result = a + b + c
#     print(result)

# add3num(1, 2, 3)
# add3num(a, b, c)
def add3num(a, b, c):
    result = a + b + c
    print(result)

add3num(b=2, c=3, a=1)
add3num(1, 2, c=3)

def add3num1(a, b, c=3):
    ret = a + b + c

add3num1(1, 2)


def num3(a,b,c):
    result = a+b+c
    print(result)
num3(10,20,30)
def num3(a,b,c):
    result1 = a+b+c
    print(result1)
num3(10,c=20,b=30)
def num3(a=1,b=1,c=20):
    result2 = a+b+c
    print(result2)
# num3(a=10,b=30)
# num3(a=30,b=10)
num3()
















