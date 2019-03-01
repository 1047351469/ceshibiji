# 需求: 让用户输入编号 --> 查找家长的姓名 ----> 查找学生的姓名 ---> 查找学生的分数 ---> 查找分数的等级
def getNum():
    index = input('请您输入家长的编号(1-3):')
    # 根据家长编号 返回家长姓名
    name = getName(index)
    # 根据家长姓名 返回学生姓名
    childName = getChildName(name)
    score = getScore(childName)
    scoreLevel(score)



def scoreLevel(score):
    if score >= 90:
        print('优')
    elif score >= 80:
        print('良')
    elif score >= 70:
        print('中')
    elif score >= 60:
        print('差')
    else:
        print('不及格')



def getScore(childName):
    if childName == '小王':
        return 98
    elif childName == '小张':
        return 65
    elif childName == '小孙':
        return 78

def getChildName(name):
    if name == '大王':
        return '小王'
    elif name == '老张':
        return '小张'
    elif name == '老孙':
        return '小孙'


def getName(index):
    if index == '1':
        return '大王'
    elif index == '2':
        return '老张'
    elif index == '3':
        return '老孙'

getNum()