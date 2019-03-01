# 要求：用键盘输入身高，如果身高没有超过150cm，则进动物园不用买票，否则需要买票。

# height = int(input('请输入身高:'))

height = input('请输入身高:')
height = int(height)

if height <= 150:
    print('直接进入动物园')
else:
    print('买票票')