# 用户输入的内容
person = int(input('请输入: 剪刀(0) 石头(1) 布(2):'))

# 计算机输入的内容
import random

# random.randint(0, 10)   # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 [0, 10]   0<=x<=10
computer = random.randint(0, 2)
print(computer)

# 站在用户的角度上
# 用户赢:
#  0  --> 2    1 ---> 0   2 ---> 1
#  假如说玩家胜利(剪刀 = 布 或者 石头 = 剪刀 或者 布 = 石头)
# 用户和电脑打平:
#  用户和电脑相等
# 用户输:
# 除了上面的那些情况,都是输

if (person == 0 and computer == 2) or (person == 1 and computer == 0) or (person == 2 and computer == 1):
    print('用户赢')
elif person == computer:
    print('用户和电脑打平')
else:
    print('用户输')



