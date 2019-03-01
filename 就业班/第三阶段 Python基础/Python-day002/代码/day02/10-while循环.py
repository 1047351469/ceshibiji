# while循环
# while循环中 如果不对index做操作, 容易造成死循环


# 定义一个变量
index = 9
while index > 5:
    print('旋风冲锋龙卷风~~~~')
    index -= 1


i = 0
while i < 5:
    print("当前是第%d次执行循环" % (i + 1))
    print("i=%d" % i)
    i+=1
