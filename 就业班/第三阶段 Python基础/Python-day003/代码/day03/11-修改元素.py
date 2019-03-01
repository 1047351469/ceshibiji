# 定义一个列表
my_list = [1, 2, 3, 4]

# print(my_list[1])
my_list[1] = 22
print(my_list)

my_list1 = [1, 2, 3, [11, 22, 33]]
# print(my_list1[3])
my_list2 = my_list1[3]
my_list2[1] = 222
print(my_list1)

# 上式可以简写:
print(my_list1[3][1])
my_list1[3][1] = 22222


my_list2 = [1, 2, 3, [11, ['1', '2', '3'], 33]]
my_list2[0] = '1'
my_list2[1] = '2'
my_list3 = ['111', 'hello', 'wporod']
my_list2 = my_list3
print(my_list2)