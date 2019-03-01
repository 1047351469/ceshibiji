# 修改元素
my_dict = {'name':'xiaozhang', 'age':23, 'height':192.3}
# print(my_dict['age'])
my_dict['age'] = 24
print(my_dict)


# 2) 添加元素
my_dict['no'] = '123456'
print(my_dict)

# )  删除元素
# - del
# - clear()
my_dict1 = {'name':'xiaozhang', 'age':23, 'height':192.3}
del my_dict1['height']
print(my_dict1)

my_dict1.clear()
print(my_dict1)

