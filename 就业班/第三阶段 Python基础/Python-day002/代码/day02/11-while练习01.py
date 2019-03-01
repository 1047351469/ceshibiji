# 计算1~100的累加和（包含1和100）

# 定义一个变量
index = 1

# 定义一个变量, 保存 和
my_sum = 0

while index < 101:
    print(index)
    my_sum = my_sum + index
    index += 1

print(my_sum)


# 2)  计算1~100之间偶数的累加和（包含1和100）