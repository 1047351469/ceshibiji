# 定义一个字符串
# 字符串是不可变的

# a = 'abcdef'

# [起始位:结束位(不包含):步长]
# 步长可以不写, 不写默认是1
# ret = a[0:3]
# print(ret)
# print(type(ret))
# print(a)



a = "abcdef"

# 'abc'   ===>  a[0:3:1] 或者 a[0:3] 或者 a[:3] 或者 a[-6:-3]
# ret1 =  a[0:3:1]
# ret2 = a[0:3]
# ret3 = a[:3]
# ret4 = a[-6:-3]
# print(ret1, ret2, ret3, ret4)

# 'ace'
# ret1 = a[0:5:2]
# ret2 = a[::2]
# print(ret1, ret2)

# a = 'abcdef'
# 'bd'
ret1 = a[1:4:2]
print(ret1)

 # 'fdb'
ret2 = a[-1::-2]
ret3 = a[::-2]
print(ret2, ret3)

 # 'fd'
ret4 = a[:-4:-2]
ret5 = a[:-5:-2]
print(ret4, ret5)
print("测试")
print("helloworld"[-1:-4:-1])


