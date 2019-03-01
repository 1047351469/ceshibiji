# 编写程序，完成“名片管理器”项目
# - 需要完成的基本功能：
#   1. 添加名片
#   2. 删除名片
#   3. 修改名片
#   4. 查询名片
#   5. 退出系统
# - 程序运行后，除非选择退出系统，否则重复执行功能



# 定义一个字符串
info = '''  1. 添加名片
  2. 删除名片
  3. 修改名片
  4. 查询名片
  5. 退出系统
请您选择要执行的程序序号:
'''
# 定义一个大的字典
all_dict = {}

while True:
    index = input(info)
    if index == '1':
        my_name = input('请您输入要添加的姓名:')
        my_age = input('请您输入要添加的年龄:')
        my_dict = {'name': my_name, 'age': my_age}
        all_dict[my_name] = my_dict
        print('您输入的信息已保存...')
    elif index == '2':
        my_name = input('请您输入要删除的姓名:')
        if my_name in all_dict:
            del all_dict[my_name]
            print('您输入的用户已删除....')
        else:
            print('您输入的信息不存在,请重新输入...')
    elif index == '3':
        my_name = input('请您输入要修改的姓名:')
        if my_name in all_dict:
            my_age = input('请输入需要修改的年龄:')
            all_dict[my_name]['age'] = my_age
            print('您输入的用户信息已修改....')
        else:
            print('您输入的信息不存在,请重新输入...')
    elif index == '4':
        my_name = input('请您输入要查询的姓名:')
        if my_name in all_dict:
            n = all_dict[my_name]['name']
            a = all_dict[my_name]['age']
            print('您查询的姓名是:%s, 年龄是:%s' % (n, a))
            print('查询完成...')
        else:
            print('您输入的信息不存在,请重新输入...')
    elif index == '5':
        print('欢迎下次使用...')
        break

