# 1)  find
# Python find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。
# mystr = 'hello world'
# ret1 = mystr.find('meihao')
# print(ret1)

# 2)  index
# Python index() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。
# ret2 = mystr.index('meihao')
# print(ret2)


# 3)  count
# Python count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置
# mystr1 = 'hello world hello'
# ret3 = mystr1.count('l')
# print(ret3)


# 4)  replace
# Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
# mystr2 = 'hello world hello'
# ret4 = mystr2.replace('hello', 'nihao', 1)
# print(ret4)


# 5)  split
# Python split()通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串
mystr3 = 'hello world hello'
ret5 = mystr3.split()
# print(ret5)
#
# mystr4 = 'hello world hello'
# ret6 = mystr4.split('l')
# print(ret6)

# 6)  capitalize
# Python capitalize()将字符串的第一个字母变成大写,其他字母变小写。对于 8 位字节编码需要根据本地环境。
# name = 'hello wORld python'
# ret7 =  name.capitalize()
# print(ret7)


# 7)  title
# Python title() 方法返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())。
# name = 'hello wORld python'
# ret8 =  name.title()
# print(ret8)

# 8)  startswith
# Python startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围内检查。
# name = 'hello wORld python'
# ret9 =  name.startswith('hllo ')
# print(ret9)

# 9) endswith
# Python endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。可选参数"start"与"end"为检索字符串的开始与结束位置。
# name = 'hello wORld python'
# ret10 =  name.endswith('python')
# print(ret10)

# 10)   lower
# Python lower() 方法转换字符串中所有大写字符为小写。
# name = 'Hello wORld python'
# ret10 =  name.lower()
# print(ret10)

# 11) upper
# name = 'hello woeifdofojiwfdiwfe'
# ret10 =  name.upper()
# print(ret10)


# 12)  ljust  : left 左  right 右
# name = 'hello python'
# ret10 =  name.ljust(30, '*')
# print(ret10)

# 13) rjust
# name = 'hello python'
# ret10 =  name.rjust(30, '*')
# print(ret10)

# center
name = 'hello'
newName =  name.center(20, '8')
print(newName)






