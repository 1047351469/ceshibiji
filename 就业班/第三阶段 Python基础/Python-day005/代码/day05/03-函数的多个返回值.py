def scoreLevel(score):
    if score >= 90:
        return '优'
    elif score >= 80:
        return '良'

def add2num(a, b):
    result = a + b
    return [a, b, result]

ret = add2num(10, 12)
print(ret[0])
print(ret[1])
print(ret[2])

# 如果返回值是一个元组, 则可以省略小括号
def add2num1(a, b):
    result = a + b
    return a, b, result

ret2 = add2num1(100, 120)
print(type(ret2))
print(ret2[0])
print(ret2[1])
print(ret2[2])
