# 小明今年20岁
# 过了一年  21
# 又过了一年 22

print('小明今年20岁')
#  过了一年
print('小明今年21岁')
# 又过了一年
print('小明今年22岁')

# 小明今年20岁
# 小明今年21岁
# 小明今年22岁

# 定义一个变量
myAge = 20
# d: digit (数字)
print('小明今年%d岁' % myAge)
myAge = myAge + 1
print('小明今年%d岁' % myAge)
myAge = myAge + 1
print('小明今年%d岁' % myAge)

my_name = '小明'
# 名字是:小明
print('名字是:%s' % my_name)

my_height = 187.30
# float
print('身高是:%.2f' % my_height)

is_boy = True
# 如果想要格式化输出bool类型, 我们有两种办法:
# %s   把bool看成字符串类型
# %d   把bool类型看成数字类型
print('是男孩吗:%s' % is_boy)
print('是男孩吗:%d' % is_boy)   # 1就是True 0: False
