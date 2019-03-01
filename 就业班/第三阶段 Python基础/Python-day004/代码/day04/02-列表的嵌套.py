schoolNames = [['北京大学','清华大学'],
               ['南开大学','天津大学','天津师范大学'],
               ['山东大学',['新东方','蓝翔']],'中国汉阳大学']

# 获取蓝翔
my_list = schoolNames[2]
my_list1 = my_list[1]
my_name = my_list1[1]
print(my_name)

# 省略
name = schoolNames[2][1][1]
print(name)

schoolNames[2][1][1] = '吉利大学'
print(schoolNames)