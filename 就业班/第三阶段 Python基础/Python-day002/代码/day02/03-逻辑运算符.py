# and
name = 'xiaoming'
pswd = '1234567'

# and: 同真为真, 一假为假
if name == 'xiaoming' and pswd == '123456':
    print('用户名和密码正确,可以登录')


# or
# or: 同假则假,一真为真
if name != 'xiaoming' or pswd != '123456':
    print('用户名或密码不对, 不能登录')
    

# not:逻辑非
# not: 非眞则假, 非假则真  (取反)
is_man = False
if not is_man:
    print('男的')