my_str = 'xiaomingxiaohongxiaozhangxiaomei'

# 定义一个列表 (list)
# 列表的格式:  列表名 = [元素一, 元素二, .......]
my_list = ['xiaoming', 'xiaohong', 'xiaozhang', 'xiaomei']
# 列表支持下标索引 (编号)
my_name = my_list[1]
print(my_name)
# 从右往左的索引也支持:
name = my_list[-1]
print(name)


# <class 'list'>
print(type(my_list))

# 空列表定义:
my_list1 = []
my_list2 = list()


name = 'hello world'
list = ['hello', 'world']
for c in name:
    print(c)

for value in list:
    print(value)


my_list3 = ['123', 23, 3.14, True, 23]
for value in my_list3:
    print(value)

print(len(my_list3))