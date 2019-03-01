# sort
a = []

import random


for i in range(6):
    value = random.randint(-10, 50)
    a.append(value)

print(a)

# 排序:
# 升序(从小到大)
a.sort()
print(a)

# 降序
a.reverse()
print(a)

a.sort(reverse=True)
print(a)
