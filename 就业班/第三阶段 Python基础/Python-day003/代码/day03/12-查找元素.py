# 定义一个列表
my_list = ['hello', 23, 3.14, 23, True, 23]

if 231 in my_list:
    print('23在列表中')

if 23 not in my_list:
    print('123不再列表中')

# index count
count = my_list.count(23)
if count > 0:
    index = my_list.index(23)
    print(index)




# print(count)