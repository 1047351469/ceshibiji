my_list = ['1', '2', '3', '4']
num1, num2, num3, num4 = my_list

num1, num2, num3, num4 = ['1', '2', '3', '4']

def info(a, b):
    a += 1
    b += 1
    return [a, b]

num5, num6 = info(10, 12)
print(num5)
print(num6)