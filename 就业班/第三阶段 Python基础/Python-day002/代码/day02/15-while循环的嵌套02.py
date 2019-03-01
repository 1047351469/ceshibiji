# 九九乘法表

# 定义一个变量
x = 1
while x <= 9:
    # 定义一个变量 列
    y = 1
    while y <= x:
        print('%d * %d = %d\t' % (y, x, x*y), end='')
        y += 1
    # 为了换行
    print('')
    x += 1