# 1)  添加元素
#
# append, extend, insert

# 列表是可变的, 字符串是不可变的

# 定义一个列表
my_list = ['hello', 2.3, 2323, True]
# append
my_list.append('world')
print(my_list)

my_list.append(['1', '2'])
print(my_list)

print('='*40)
# extend
my_list1 = ['hello', 2.3, 2323, True]
my_list1.extend('world')
print(my_list1)

# 下面的用法是错误的: 因为int不能遍历:
# TypeError: 'int' object is not iterable
# my_list1.extend(123)
# print(my_list1)

my_list1.extend(['1', '2'])
print(my_list1)


# insert
my_list2 = ['hello', 2.3, 2323, True]
my_list2.insert(2, 'world')
print(my_list2)

