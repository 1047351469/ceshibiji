# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# 定义一个变量
x = 1
while x <= 9:
    if x <= 5:
        y = 1
        while y <= x:
            print('*', end='')
            y += 1
        # 为了换行
        print('')
    else:  # x = 6
        y = 9
        while y >= x:
            print('*',end='')
            y -= 1
        # 换行
        print()
    x += 1
