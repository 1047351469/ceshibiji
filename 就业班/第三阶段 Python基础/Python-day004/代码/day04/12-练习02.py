# 6公里(含)内3元;
#
# 6公里至12公里(含)4元;
#
# 12公里至22公里(含)5元;
#
# 22公里至32公里(含)6元;
#
# 32公里以上部分，每增加1元可乘坐20公里。

# 定义一个变量, 保存用户走的公里数
km = 18
# 定义一个变量, 保存用户花费的钱数(单程)
every_money = 0

if km > 0 and km <= 6:
    every_money = 3
elif km > 6 and km <= 12:
    every_money = 4
elif km > 12 and km <= 22:
    every_money = 5
elif km > 22 and km <= 32:
    every_money = 6
elif km > 32:
    # 例如: 50km = (32 + 18) ----> (6 + 1)
    # 例如: 52km = (32 + 20)  --->  (6  +  1)
    # 例如: 53km = (32 + 20 + 1) ---> (6 + 1 + 1)
    temp_km = km - 32
    # 包含32公里以内的 对20能够取整的:
    if temp_km % 20 == 0:
        every_money = 6 +  temp_km/20
    else:
        # 不能够进行整除
        every_money = 6 + int(temp_km/20) + 1

print('单程的价格是:%d' % every_money)


# 使用市政交通一卡通刷卡乘坐轨道交通，
#
# 每自然月内每张卡支出累计满100元以后的乘次，价格给予8折优惠;
#
# 满150元以后的乘次，价格给予5折优惠;
#
# 支出累计达到400元以后的乘次，不再享受打折优惠。
#
# 假设每个月，小明都需要上20天班，每次上班需要来回1次，即每天需要乘坐2次同样路线的地铁
#
# 最终得出这"20"天小明做地铁消费多少钱?

# 定义一个变量 , 保存总金额
total_money = 0

# 循环40次  因为:20天*每天2趟
for i in range(40):
    if total_money <= 100:
        total_money += every_money
    elif total_money > 100 and total_money <= 150:
        total_money += every_money * 0.8
    elif total_money > 150 and total_money <= 400:
        total_money += every_money * 0.5
    elif total_money > 400:
        total_money += every_money

print('小明总共花的钱数:%d' % total_money)







