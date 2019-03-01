# - del：根据下标进行删除, 也可以删除掉整个列表对象,提前释放内存
# - pop：删除最后一个元素,  也可以删除单个指定元素  把删除的元素返回回来
# - remove：根据元素的值进行删除  如果要删除的元素值不再列表,会崩溃
# - clear: 清空这个列表     把列表中的元素删除干净,但是列表还在

# del
my_list = ['hello', 23, 3.14, 23, True, 23]

# print(my_list[2])
del my_list[2]

print(my_list)

# 特殊:
# del my_list
# print(my_list)

# pop
my_list1 = ['hello', 23, 3.14, 23, True]
# ret是删除的元素
ret = my_list1.pop()
print(ret)
print(my_list1)

# 指定删除元素
ret1 = my_list1.pop(2)
print(ret1)
print(my_list1)

# remove
my_list2 = ['hello', 23, 3.14, 23, True]
my_list2.remove(23)
print(my_list2)

# clear
# 清除
my_list3 = ['hello', 23, 3.14, 23, True]
my_list3.clear()
print(my_list3)