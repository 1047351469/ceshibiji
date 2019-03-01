# 元组的定义:

my_tuple = (23, 3.14, 'hello',3.14, True)
ret1 = my_tuple[1]
print(ret1)

# 下面的写法是错误的: 元组的元素不可以改变
# my_tuple[1] = 314
# print(my_tuple)

index = my_tuple.index(3.14)
print(index)

count = my_tuple.count(3.14)
print(count)