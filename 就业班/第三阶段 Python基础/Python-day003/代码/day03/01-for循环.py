# 定义一个字符串
name = 'xiaoming'

# i = 0
# while i < 8:
#     print(name[i])
#     i += 1

for c in name:
    print(c)

# range() 范围函数
# 0 - 10  0<=x<10  [0, 10)
for index in range(0, 10):
    print(index)

print('-------------')
# range()有一个简写形式:
# 如果range()默认是从0开始的, 0可以省略不写
for i in range(10):
    print(i)

print('==========================================')
for i in range(10):
    print(i)
else:
    print('else')

print('*******************************************')
for i in range(10):
    print(i)

print('else')