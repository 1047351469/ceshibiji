#
# b = 20
# a = 100
# def func1():
#     c = 300
#     print(a)
#
# def func2(x, y):
#     z = 20
#     print(a)
#
#
# func1()
# func2()



# a = 100
# def func1():
#     a = 200
#     print(a)
#
# func1()
# print(a)

a = 100
def func1():
    global a
    a = 200
    print(a)

func1()
print(a)





