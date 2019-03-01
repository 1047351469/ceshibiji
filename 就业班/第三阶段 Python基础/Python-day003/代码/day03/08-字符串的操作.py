# 15)   lstrip
# Python lstrip() 方法用于截掉字符串左边的空格或指定字符。
# myStr = '  hello world   '
# ret1 = myStr.lstrip('h ')
# print(ret1)

# 16)  rstrip
# Python rstrip() 删除 string 字符串末尾的指定字符（默认为空格）.
# myStr = '  hello world   '
# ret2 = myStr.rstrip(' d r')
# print(ret2)


# 17)  strip
# Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）。
# myStr = '***hello world****'
# ret3 = myStr.strip('*')
# print(ret3)

# 18)  rfind
# Python rfind() 返回字符串最后一次出现的位置(从右向左查询)，如果没有匹配项则返回-1。
myStr = 'hello world python nrihao'
ret3 = myStr.find('r')
print(ret3)

ret4 = myStr.rfind('r')
print(ret4)

# 19)   rindex    没有检索到会崩溃


# 20) partition
# name = 'hello world nihao python itcast'
# ret = name.partition('nihao')
# print(ret)

# 21)   rpartition
#
# 类似于 partition()函数,不过是从右边开始.
name = 'hello world nihao python nihao itcast'
ret = name.rpartition('nihao')
print(ret)

# 22)   splitlines
#
# Python splitlines() 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
myStr1 = '''python  zhongguo
hello
nihao
world
'''
ret5 = myStr1.splitlines()
print(ret5)


# 23)   isalpha
str22 = 'abcABC'
ret6 = str22.isalpha()
print(ret6)

#24)  isdigit
str23 = '123 '
ret7 = str23.isdigit()
print(ret7)



# 25)  isalnum  : is alpha number
# name1 = 'abc123ABC'
# ret7 = name1.isalnum()
# print(ret7)



# 26)  isspace
name1 = '    d   '
ret7 = name1.isspace()
print(ret7)


aStr  =  'haha  nihao  a  \t  heihei   \t  woshi  nide  \t  hao  \n pengyou'
print(aStr)
ret = aStr.split(' \n\t')
print(ret)

ret1 = aStr.split()
print(ret1)








