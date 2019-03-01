def func1():
    print('func1')
    try:
        print(num)
    except:
        print('错误')


def fun2():
    print('func2')
    # try:
    #     func1()
    # except:
    #     print('发生了错误')
    func1()

def func3():
    print('func3')
    fun2()

# try:
#     func3()
# except:
#     print('发生错误了')
func3()