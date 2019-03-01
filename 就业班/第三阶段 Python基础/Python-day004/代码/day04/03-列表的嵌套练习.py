school = [[], [], []]
teachers = 'ABCDEFGH'
import random
# 0<=x<=2

for teacher in teachers:
    index = random.randint(0, 2)
    school[index].append(teacher)

print(school)

