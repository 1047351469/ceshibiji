# print(num)
# NameError: name 'num' is notdefined
# NameError:  异常的类型
# name 'num' is notdefined  异常的描述
# NameError
# FileNotFoundError


# 捕获多种异常
# try:
#     open('hm.txt', 'r')
#     print(num)
# except (NameError, FileNotFoundError):
#     print('发生异常了')


# 捕获所有的异常:
# try:
#     # open('hm.txt', 'r')
#     print(num)
# except:
#     print('发生异常了')

try:
    # open('hm.txt', 'r')
    print(num)
except Exception:
    print('发生异常了')