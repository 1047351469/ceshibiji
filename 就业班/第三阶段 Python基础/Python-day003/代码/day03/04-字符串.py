# 字符串就是 有序的字符序列.
name = 'itcast'

# 定义: '字母或者是字符,或者是汉子'   或者 "字符串的东西"

name1 = '''
python
hello

world
nihao
'''
name2 = 'python' \
        'hello' \
        'world' \
        'nihao'

print(name1)
print(type(name1))

print(name2)

# 字符串的另一种定义形式:  '''字符串的内容'''  或者 """字符串的内容"""
# 好处: 能够保留换行  空格  空行

# python 的内置方法: len()
# len() 获取字符串的长度

name = 'xiao ming222!小'
print(len(name))

length = len(name)
print(length)


# 空字符串:  ''  或者 str()
name3 = ''
print(len(name3))
# 空字符串还有另一种写法: str()
name4 = str()
print(len(name4))


# name = "姓名：%s" % age
mystr1 = 'hello world'
ret1 = mystr1.find('mei')
print(ret1)    # -1

count = mystr1.count('mei')
if count > 0:
    ret2 = mystr1.index('mei')
else:
    print(-1)

str = '你好中国'
result = str.lower()
print(result)



