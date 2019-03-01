# "hello world"

name = 'hello world'

# 数量
# count = name.count('l')
my_list = []
for c in name:
    if c != ' ' and c not in my_list:
        # print(c)
        count = name.count(c)
        my_list.append(c)
        print('%s:%d' % (c, count), end='')