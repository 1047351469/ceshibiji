# 需求:根据成绩打印输出 优良中差

# 定义一个变量,存储分数
score = 89

if score >= 90 and score <= 100:
    print('优')
elif score >= 80 and score < 90:
    print('良')
elif score >= 70 and score < 80:
    print('中')
elif score >= 60 and score < 70:
    print('差')
else:
    print('不及格')

if score >= 90 and score <= 100:
    print('优')
elif score >= 80:
    print('良')
elif score >= 70:
    print('中')
elif score >= 60:
    print('差')
else:
    print('不及格')