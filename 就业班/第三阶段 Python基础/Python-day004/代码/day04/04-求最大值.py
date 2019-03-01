list = [-10, 23, 234, 833, -2438, 29]

# list.sort()
#
# # print(len(list))
# length = len(list)
#
# max = list[length - 1]
#
# print(max)

# 冒泡排序
maxValue = list[0]

for value in list:
    if value > maxValue:
        maxValue = value

print(maxValue)


# 求最小值
minValue = list[0]

for value in list:
    if value < minValue:
        minValue = value

print(minValue)