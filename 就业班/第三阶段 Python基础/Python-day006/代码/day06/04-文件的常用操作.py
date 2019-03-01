# 引入模块
import os

# 1) 文件重命名
# os.rename('hm.txt', 'hmhm.txt')

# 2) 删除文件
# os.remove('hmhm.txt')

# 3) 创建文件夹
# os.mkdir('黑马文件夹')

# 4) 获取当前目录
# path = os.getcwd()
# print(path)

# 5)  改变默认目录
# change directory
# os.chdir('../')
#
# path = os.getcwd()
# print(path)

# 6)  获取目录列表
# os.chdir('黑马文件夹')
# list = os.listdir('./')
# print(list)

# 7)  删除文件夹
# os.mkdir()
# os.remove('新建文本文档.txt')
# os.remove('新建文本文档 (2).txt')
# os.rmdir('黑马文件夹')

# import os
# os.mkdir('黑马')
# os.chdir('黑马')
# for i in range(1,11):
#     f=open('%s.txt'%i,'w')
#     f.close()
# list=os.listdir()
# for i in list:
#     print(i)
#     for x in range(11,21):
#         str = i.replace(i,'%s.txt'%x)
#         os.rename(i,str)