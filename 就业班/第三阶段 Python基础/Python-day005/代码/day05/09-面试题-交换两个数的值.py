# a = 1
# b = 2

# 第一种方法
a = 1
b = 2
c = 0

c = a  #    a = 1,
a = b  #    a = 2,
b = c  #    b = 1,
#
# print(a, b)
# 第二种方法
a = 1
b = 2

a = a + b
b = a - b  # a - b = a + b - b = a
a = a - b  # a - b = a + b - a = b

# 第三种方法
# ^: 异或: 二进制:  相同的值得0, 不同的值得1
a = 1
b = 2

a = a^b
b = a^b  #  a^b = a^b^b = a
a = a^b  #  a^b = a^b^a = b


# 第四种方法
a = 8
b = 2

# a = 2
# b = 8
def value(a, b):
    if a > b:
        num = a - b
        a -= num
        b += num
    else:
        num = b - a
        a += num
        b -= num
    return a,b

# 第五种:
a = 1
b = 2
a, b = b, a
# a, b = 1, 2


# 第六种
a = 1
b = 2
def x(a,b):
    print(a)
    print(b)
x(a=b,b=a)









