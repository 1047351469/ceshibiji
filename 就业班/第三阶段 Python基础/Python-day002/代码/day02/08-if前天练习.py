# 情节描述：乘坐公交车外出.
#
# 要求：输入公交卡当前的余额，只要超过2元，就可以上公交车；如果车上有空座位，可以坐下。

money = eval(input('请您输入余额:'))

# 定义一个变量
flag = 1    # 1:True 0:False

if money > 2:
    print('上公交车')
    if flag:
        print('有座位,可以坐下')
    else:
        print('我站会,减肥...')
else:
    print('回去充值')