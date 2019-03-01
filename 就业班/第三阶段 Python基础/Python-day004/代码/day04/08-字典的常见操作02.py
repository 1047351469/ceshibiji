my_dict = {'name':'meihao', 'age':23, 'no':'2344'}

# 1)  len()
length = len(my_dict)
print(length)


# 2)  keys
keys = my_dict.keys()
# dict_keys(['name', 'age', 'no'])  # 就是一个列表
print(list(keys))

# name = '123'
# int(name)  ===> 123


# 3)  values
names = my_dict.values()
# dict_values(['meihao', 23, '2344'])
print(list(names))



# 4)  items
# [('name', 'meihao'), ('age', 23), ('no', '2344')]
# items: ===> 能够把字典中的所有内容全部获取到,保存在一个列表中, key:value的键值对
# 则是保存在元组中
items = my_dict.items()
# print(list(items))
items1 = list(items)
tuple1 = items1[0]
# print(tuple1)
tuple1[1]

