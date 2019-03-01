#   *
#  ***        1 -->  1
# *****       2 ---> 3
            # 3 ---> 5
#               index =   2y + 1  -(index + 1)
#               2 * index = 2*y
# #
index = 0
while index <= 3:
    y = 0
    while y < 2 * index + 1:
        z = 2 * index + 1 - y
        print('%s' % ('#'*z) ,end='',)
        print('*', end='')
        y += 1
    print()
    index += 1
