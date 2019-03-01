try:
    open('hm.txt','r')
    # num = 1
    # print(num)
except Exception as info:
    print('发生错误....')
    print(info)
else:
    print('else')


