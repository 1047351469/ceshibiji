# #  引入os模块
# import os
#
# # 创建文件夹  hm9
# # os.mkdir('hm9')
# # 改变当前光标路径
# os.chdir('hm9')
# #
# # for i in range(1,9):
# #     f = open('%d.txt' % i,'w',encoding='utf-8')
#
# for i in range(1,9):
#     os.rename('%d.txt' % i,'new_%d.txt' % i)
#
# # 关闭
# # f.close()

# import os

# 创建文件和文件夹
# os.mkdir('黑马文件夹')
#
# os.chdir('黑马文件夹')
#
# for i in range(10):
#     f = open('hm%d.txt' % (i+1), 'w')
#     f.close()

# 修改文件和文件夹
# os.chdir('黑马文件夹')
#
# my_list = os.listdir('./')
#
# # hm1.txt  ==> hm1[新的].txt
# for file_name in my_list:
#     new_file_name = file_name.replace('.txt', '[新的].txt')
#     os.rename(file_name, new_file_name)
