# 定义一个字符串
num = '123'


# 数据类型转换  str ---> int
num1 = int(num)
# <class 'int'>
print(type(num1))


#定义一个字符串
height = '176.8'

# str ---> float
height1 = float(height)
print(height1)
print(type(height1))

# int ---> str  float ---> str
num3 = 23
num4 = 3.14
str1 = str(num3)
print(type(str1))

str2 = str(num4)
print(type(str2))

# bool类型不能转换


age = '23'
# eval()这个方法能够帮助我们自定识别: 去掉' ' 以后的内容是否是我们的常见类型, 如果是 转化成对应的类型
# eval(age)
# eval()  往往和input()
str3 = input('请输入一个数字')
print(type(eval(str3)))
