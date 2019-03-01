# 类型
# int 有符号的整形
# float 浮点型
# 布尔(bool)  True  False
# string (字符串)  简写: str

# 需求: 定义一个人的信息: 姓名  年龄  身高  是否是男的
# 姓名:
# 用的字符串类型:  格式:  '内容部分'  或者  "内容部分"
# python里面有一个内置函数, 帮我们检测变量里面存放的数据类型
# type(变量名或者数值)
name = '小明'
# <class 'str'>
print(type(name))

# 年龄
age = 18
# <class 'int'>
print(type(age))

# 身高
height = 178.5
# <class 'float'>
print(type(height))

# 是否是男的
is_man = True
# <class 'bool'>
print(type(is_man))

age = 23
print(type('hello python'))
