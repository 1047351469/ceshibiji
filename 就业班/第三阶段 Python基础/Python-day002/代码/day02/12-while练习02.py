# 2)  计算1~100之间偶数的累加和（包含1和100）
# 偶数: 能够被2整除的数


i = 1

# 定义一个变量, 保存偶数和
sum = 0

while i < 101:
    # 获取所有的1 -- 100的数
    if i % 2 == 0:
        # 进到这里面,获取所有的偶数
        # 2 + 4 + 6
        sum = sum + i
    i += 1


# 2)  计算1~100之间偶数的累积（包含1和100）
# 定义一个变量
index = 1
# 设一个变量, 保存偶数的累积
result = 1

while index < 101:
    # 获取所有的偶数
    if index % 2 == 0:
        # 这里面的数都是偶数
        result = result * index
    index += 1
