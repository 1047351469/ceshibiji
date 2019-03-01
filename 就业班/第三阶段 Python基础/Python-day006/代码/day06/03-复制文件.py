old = open('hm.txt', 'w', encoding = 'utf-8')
str = '''
1:既然你诚心诚意的发问了，
2:那我就大发慈悲的告诉你，
'''
old.write(str)
old.close()

f = open('hm.txt', 'r', encoding = 'utf-8')
content1 = f.read()

new = open ('hm1.txt' , 'w' ,encoding = 'utf-8')
content2 = new.write(content1)

f.close()
new.close()




f = open('hm.txt', 'w', encoding='utf-8')
str = '既然你诚心诚意地问了'
f.write(str)
f.close()

f = open('hm.txt', 'r', encoding='utf-8')
content = f.read()
f.close()

i = open('hm1.txt', 'w', encoding='utf-8')
i.write(content)
i.close()


# 需求：创建一个文件，向里面写入一些东西，然后再创建另一个文件，把上一个文件的内容放在新文件里
file = open('old_file.txt', 'w', encoding='utf-8')
str = '''天行健君子以自强不息

地势坤君子以厚德载物
'''
file.write(str)

file = open('old_file.txt','r',encoding='utf-8')
str1 = file.read()

file_new = open('new_file.txt','w',encoding='utf-8')
file_new.write(str1)

file_new = open('new_file.txt','r',encoding='utf-8')
str2 = file_new.read()
print(str2)
file.close()
file_new.close()