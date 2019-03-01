# # 打开文件
# f = open('hm.txt', 'w')
#
# # r:  如果文件没有 会报错
# # w:  如果文件没有 会创建一个
#
# # 关闭文件
# f.close()


# f = open('hm.txt', 'w', encoding='utf-8')
# str = '''既然你诚心诚意的问了，
# 那我就大发慈悲的告诉你，
# 为了防止世界被破坏，
# 为了守护世界的和平，
# 贯彻爱与真实的邪恶，
# 可爱又迷人的反派角色，
# 白洞，白色的明天在等待着我们！
# 喵~就是这样 ~~~~~~
# '''
# f.write(str)
# f.close()

# f = open('hm.txt', encoding='utf-8')
# content = f.read()
# print(content)
# f.close()

# f = open('hm.txt', encoding='utf-8')
# content = f.read(15)
# print(content)
# print('====='*20)
# content1 = f.read()
# print(content1)
# f.close()


f = open('hm.txt', encoding='utf-8')

lines = f.readlines()
print(lines)

i = 1
for line in lines:
    print('%d===%s' % (i, line))
    i += 1

f.close()