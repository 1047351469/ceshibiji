# 1)  关于开闭区间的总结
import random
random.randint(0, 10) # 0<=x<=10 [0, 10]

range(0, 10)  # 0<=x<10  [0, 10)

a = 'itcast'
# a[起点:终点(不包含):步长]  [0, 10)


name = 'xiaoming'
name1 = 'xiaohong'
result = name + name1
print(result)
print(type(result))


my_list1 = [1, 3]
my_list2 = [2, 4]
result1 = my_list1 + my_list2
print(result1)

print('==========================================')
print('=='*20)

result2 = my_list1*4
print(result2)












# my_tuple = (1, 3, 4, 5, 6)
# ret = my_tuple[0:2]
# print(ret)