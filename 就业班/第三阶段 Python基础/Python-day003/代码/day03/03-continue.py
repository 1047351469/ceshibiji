# continue

for i in range(5):
    print(i)
    if i == 3:
        continue
        print('*******')
print('测试')

for i in range(5):
    for x in range(3):
        print(x)
        print(i)
        if x == 1:
            break