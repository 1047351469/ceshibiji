# 对字符串进行遍历
name = 'itcast'
for c in name:
    print(c)

my_list = [1,2,3,34]
for value in my_list:
    print(value)

# 对元组
my_tuple = (1, 3, 4, 3,14)
for value in my_tuple:
    print(value)

# 对字典进行遍历
my_dict = {'name':'xiaoming', 'age':23, 'no':'23244'}
# for value in my_dict:
#     print(value)
#
# for value in my_dict.values():
#     print(value)

# for key in my_dict.keys():
#     print(key)

for item in my_dict.items():
    print(item)
    print(item[0])
    print(item[1])

for key, value in my_dict.items():
    print(key)
    print(value)
